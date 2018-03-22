Hook for controlling function execution process.

This hook is intended as support for loadable security policy modules, which may
want to perform additional privilege checks on function entry or exit,
or to do other internal bookkeeping.

It is invoked whenever postgres executes a function which was explicitly
marked as hookable by `needs_fmgr_hook`. For each execution this hook is fired
exactly twice: first time before invoking the function, second time after
the function returns/throws.

Note that there is a change that this hook will be called even if a function
is not of interest of your extension (maybe some other extension made it
hookable via its `needs_fmgr_hook`).

*Inputs:*

* <i>FmgrHookEventType</i> <b>event</b> — event type, can be one of
  `FHET_START`, `FHET_END`, `FHET_ABORT`.
* <i>FmgrInfo *</i> <b>flinfo</b> — function info, including its id and
  arguments specification.
* <i>Datum *</i> <b>arg</b> — function arguments.
