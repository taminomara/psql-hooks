PostgreSQL hooks are a simple way to extend functionality of the database.
They allow extensions to introspect database state, react to events and
interfere with database operations.

Every hook is a pointer to a function, initially set to `NULL`.

When postgres wants to call a hook, it checks whether the pointer for that
hook is not null and if that's the case, calls the registered function.

Extensions can update these pointers during the init procedure
in order to register a new handler for a hook.

That is, when extension is loaded, postgres calls its `_PG_init` function.
Once called, it can alter hook variables which are a part of the public binary
interface.

A usual setup would include saving the previous value of the hook variable
and writing pointer to a handler defined by extension.

Saving the previous value is important because another extension could've
registered its own hook handler. If that's the case, we'd like to call it in
our hook so that this extension can operate without errors. Any well-designed
plugin will do such hook chaining.

To pop the state of the hook created by one extension `_PG_fini` function must be implemented, 
which is basically recovers hook to it's value before `_PG_init`.

A standard example on how to use hooks is the `auth_delay` plugin.
This plugin delays error report in case of user authentication failure,
which is useful to block password brute-forcing.

```c
// We store previously assigned hook pointer in a global variable.
static ClientAuthentication_hook_type original_client_auth_hook = NULL;

// Our hook implementation.
static void auth_delay_checks(Port *port, int status)
{
    // If any other extension registered its own hook handler,
    // call it before performing our own logic.
    if (original_client_auth_hook)
        original_client_auth_hook(port, status);

    // If authentication failed, we wait for one second before returning
    // control to the caller.
    if (status != STATUS_OK)
    {
        pg_usleep(1000000L);
    }
}

// Called upon extension load.
void _PG_init(void)
{
    // Save the original hook value.
    original_client_auth_hook = ClientAuthentication_hook;
    // Register our handler.
    ClientAuthentication_hook = auth_delay_checks;
}

// Called with extension unload.
void _PG_fini(void)
{
    // Return back the original hook value.
    ClientAuthentication_hook = original_client_auth_hook;
}

```
