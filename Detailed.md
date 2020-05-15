# Postgresql hooks documentation

PostgreSQL hooks are a simple way to extend functionality of the database.
They allow extensions to introspect database state, react to events and
interfere with database operations.

Every hook is a pointer to a function, initially set to `NULL`.

When postgres wants to call a hook, it checks whether the pointer fot that
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

## Table of contents

* [General Hooks](#general-hooks)
* [Security Hooks](#security-hooks)
* [Function Manager Hooks](#function-manager-hooks)
* [Planner Hooks](#planner-hooks)
* [Executor Hooks](#executor-hooks)
* [PL/pgsql Hooks](#plpgsql-hooks)


## General Hooks




<a name="emit_log_hook" href="#emit_log_hook">#</a> <i>void</i> <b>emit_log_hook</b>(edata) [<>](https://github.com/postgres/postgres/blob/master/src/include/utils/elog.h#L375 "Source")

Hook for intercepting messages before they are sent to the server log.

This hook is called just before sending an error message to the server log
and to the client. The purpose of this hook is to invoke an additional
logic and possibly prevent this error message from being added to the
server log.

This hook is useful for implementing custom logging process.

*Inputs:*

* <i>ErrorData *</i> <b>edata</b> — a structure which holds a complete info
  about the error message. Despite `edata` is a non-const pointer, the only
  supported change in the given structure is setting `output_to_server` to
  `false`. That is, any other change, including setting `output_to_server` to
  `true`, considered not supported.

Note: despite any other changes to the edata are not officially supported
(as per comment [on line 1455 of the elog.c][emit_log_hook_1])),
postgres actually checks for both `output_to_server` and `output_to_client`
flags.

[emit_log_hook_1]: https://github.com/postgres/postgres/blob/master/src/backend/utils/error/elog.c#L1456


<a name="shmem_startup_hook" href="#shmem_startup_hook">#</a> <i>void</i> <b>shmem_startup_hook</b>() [<>](https://github.com/postgres/postgres/blob/master/src/include/storage/ipc.h#L77 "Source")

Hook for extensions to initialize their shared memory.

This hook is called by postmaster or by a standalone backend
right after postgres initializes its shared memory and semaphores
so that extensions have chance to initialize their shared state.

It also may be called by a backend forked from the postmaster.
In this situation, the shared memory segment already exists, so you only have
to initialize the local memory state (check `!IsUnderPostmaster`
to determine if that's the case).

Note that you can bind a callback for shared state teardown
via `on_shmem_exit`.

Check out the `pg_stat_statements` code to get the idea on how to implement
this hook correctly.


## Security Hooks




<a name="check_password_hook" href="#check_password_hook">#</a> <i>void</i> <b>check_password_hook</b>(username, shadow_pass, password_type, validuntil_time, validuntil_null) [<>](https://github.com/postgres/postgres/blob/master/src/include/commands/user.h#L25 "Source")

Hook for enforcing password constraints and performing action on password change.

This hook is called whenever a new role is created via the `CREATE ROLE`
statement or a password for an existing role is changed via the `ALTER ROLE`
statement. Given a shadow password and some additional info, this hook can
raise an error using the standard `ereport` mechanism if the password
isn't strong enough.

*Inputs:*

* <i>const char *</i> <b>username</b> — name of the created/altered role.
* <i>const char *</i> <b>shadow_pass</b> — a shadow pass, i.e. a plain password
  or a password hash.
* <i>PasswordType</i> <b>password_type</b> — type of the password.
  `PASSWORD_TYPE_MD5` for an md5-encrypted password,
  `PASSWORD_TYPE_SCRAM_SHA_256` for a sha-256-encrypted password,
  `PASSWORD_TYPE_PLAINTEXT` for a plaintext password.
* <i>Datum</i> <b>validuntil_time</b> — date upon which this password expires.
* <i>bool</i> <b>validuntil_null</b> — a flag that is true if and only if
  the password have no expiration date (i.e. a null date is passed).


<a name="ClientAuthentication_hook" href="#ClientAuthentication_hook">#</a> <i>void</i> <b>ClientAuthentication_hook</b>(port, status) [<>](https://github.com/postgres/postgres/blob/master/src/include/libpq/auth.h#L27 "Source")

Hook for controlling the authentication process.

Called after finishing user authentication (regardless of whether authentication
succeed or not).

This hook will be called for every connection that passed authentication.
However, it is not guaranteed to be called if there are issues with the
connection itself. For example, SSL verification failure or pg_hba.conf
check failure will close the connection without calling this hook.

*Inputs:*

* <i>Port *</i> <b>port</b> — full info about the connection and
  the connected user.
* <i>int</i> <b>status</b> — a standard status code. `STATUS_OK` (`0`)
  if authentication successful.


<a name="ExecutorCheckPerms_hook" href="#ExecutorCheckPerms_hook">#</a> <i>bool</i> <b>ExecutorCheckPerms_hook</b>(rangeTabls, abort) [<>](https://github.com/postgres/postgres/blob/master/src/include/executor/executor.h#L90 "Source")

Hook for adding additional security checks on the per-relation level.

Given a relations list, this hook should return `true` if access is granted.
`false`, if access is not granted and `abort` is `false`. If `abort` is `true`
and access is not granted, it should throw an appropriate error.

This hook is not called if the standard permission check procedure denies
access to any relation in the list. Therefore, there is no way to actually
raise user privileges.

Theoretically, only plain-relation RTEs need to be checked in this hook.
Function RTEs are checked during the function preparation procedure.
Join, subquery, and special RTEs need no checks.

*Inputs:*

* <i>List *</i> <b>rangeTabls</b> — list of `RangeTblEntry` objects that needs
  checking.
* <i>bool</i> <b>abort</b> — if `true`, raise `aclcheck_error` instead of
  returning `false` from the hook.

*Output:*

`true` if user have privileges to access given relations, `false` or raise an
error otherwise, depending on the `abort` flag.


<a name="object_access_hook" href="#object_access_hook">#</a> <i>void</i> <b>object_access_hook</b>(access, classId, objectId, subId, arg) [<>](https://github.com/postgres/postgres/blob/master/src/include/catalog/objectaccess.h#L127 "Source")

Hook to monitor accesses to objects.

Object access hooks are called just before or just after performing certain
actions on an SQL object. This is intended as infrastructure for security
or logging extensions.

There are several types of actions defined in `ObjectAccessType`:

`OAT_POST_CREATE`: hook is invoked just after the object is created.
Typically, this is done after inserting the primary catalog records and
associated dependencies.

`OAT_DROP`: hook is invoked just before deletion of objects.

`OAT_POST_ALTER`: hook is invoked just after the object is altered,
but before the command counter is incremented. An extension using the
hook can use a current MVCC snapshot to get the old version of the tuple,
and can use `SnapshotSelf` to get the new version of the tuple.

`OAT_NAMESPACE_SEARCH`: hook is invoked prior to object name lookup under
a particular namespace. This event is equivalent to usage permission
on a schema under the default access control mechanism.

`OAT_FUNCTION_EXECUTE`: hook is invoked prior to function execution.
This event is almost equivalent to execute permission on functions,
except for the case when execute permission is checked during object
creation or altering, because `OAT_POST_CREATE` or `OAT_POST_ALTER` are
sufficient for extensions to track these kind of checks.

Other types may be added in the future.

*Inputs:*

For different access types, inputs of this hook mean different things.

* <i>ObjectAccessType</i> <b>access</b> — access type.
* <i>Oid</i> <b>classId</b> — id of a relation which contains this object.
  You can determine type of an object by this parameter.
* <i>Oid</i> <b>objectId</b> — object that is being accessed.
* <i>int</i> <b>subId</b> — subitem within object (e.g. column), or 0.
* <i>void *</i> <b>arg</b> — access type specific argument.

For `OAT_POST_CREATE`, `arg` is a pointer to `ObjectAccessPostCreate`
structure, which contain a single field, namely `is_internal`. This field
describes whether the context of this creation is invoked by user's
operations, or not. As for `subId`, I've counted two cases when it's non-zero.
The first is when creating a column, and the second one is when creating
a default expression on a column. In either case, `subId` is
an `AttrNumber` of a column.

For `OAT_DROP` type, `arg` is a pointer to `ObjectAccessPostCreate` structure.
It contains a single field called `dropflags`. They inform extensions the
context of this deletion.

For `OAT_POST_ALTER` type, `arg` is a pointer to `ObjectAccessPostAlter`
structure. It contains an `is_internal` flag (see `OAT_POST_CREATE`) and an
`auxiliary_id`. The latter is used when system catalog takes two IDs to
identify a particular tuple of the catalog. It is only used when the caller want
to identify an entry of pg_inherits, pg_db_role_setting or pg_user_mapping.
Elsewhere, InvalidOid is be set.

For `OAT_NAMESPACE_SEARCH` type, `subId` is unused, `classId` is always
`NamespaceRelationId`, and `arg` is a pointer to `ObjectAccessNamespaceSearch`.

`ObjectAccessNamespaceSearch` structure contain two fields. The first one,
`ereport_on_violation`, indicates that the hook should raise an error when
permission to search this schema is denied. The second one, `result`, is in fact
an out parameter. Core code should initialize this to true, and any extension
that wants to deny access should reset it to false. But an extension should be
careful never to store a true value here, so that in case there are multiple
extensions access is only allowed if all extensions agree.

For `OAT_FUNCTION_EXECUTE` type, `subId` and `arg` are unused, and
`classId` is always `ProcedureRelationId`.


<a name="row_security_policy_hook_permissive" href="#row_security_policy_hook_permissive">#</a> <i>List *</i> <b>row_security_policy_hook_permissive</b>(cmdtype, relation) [<>](https://github.com/postgres/postgres/blob/master/src/include/rewrite/rowsecurity.h#L40 "Source")

Hook to add policies which are combined with the other permissive policies.

This hook, along with the `row_security_policy_hook_restrictive`, allows adding
custom security policies. It is called to build a list of policies for the given
command applied to the given relation.

Access is granted to an object if and only if no restrictive policies deny
access and any permissive policy grant access.

*Inputs:*

* <i>CmdType</i> <b>cmdtype</b> — command type.
* <i>Relation</i> <b>relation</b> — relation id.

*Output:*

List of additional permissive policies that will be added to the list of
default permissive policies.


<a name="row_security_policy_hook_restrictive" href="#row_security_policy_hook_restrictive">#</a> <i>List *</i> <b>row_security_policy_hook_restrictive</b>(cmdtype, relation) [<>](https://github.com/postgres/postgres/blob/master/src/include/rewrite/rowsecurity.h#L42 "Source")

Hook to add policies which are enforced, regardless of other policies.

See `row_security_policy_hook_permissive` for a detailed description.

Unlike for permissive policies, postgres guarantees that restrictive policies
will be executed in a predefined order. That is, first postgres executes the
default policies sorted by their name, than postgres executes custom policies,
also sorted by their name.

*Inputs:*

* <i>CmdType</i> <b>cmdtype</b> — command type.
* <i>Relation</i> <b>relation</b> — relation id.


## Function Manager Hooks




<a name="needs_fmgr_hook" href="#needs_fmgr_hook">#</a> <i>bool</i> <b>needs_fmgr_hook</b>(fn_oid) [<>](https://github.com/postgres/postgres/blob/master/src/include/fmgr.h#L727 "Source")

Auxiliary hook which decides whether `fmgr_hook` should be applied to a function.

Given a function id, decide whether `fmgr_hook` should be called upon executing
this function.

The result of this hook should be combined with the result of a previously
registered `needs_fmgr_hook` via the `OR` clause. This is required to ensure
that other extensions can hook function even though this very extension does
not hook them. Such behavior is vital for proper work of the security extensions.

Note that hooked functions are not inlined.

*Inputs:*

* <i>Oid</i> <b>fn_oid</b> — id of a function which needs hooking.

*Output:*

Return `true` if you want to hook enter/exit event for this function.


<a name="fmgr_hook" href="#fmgr_hook">#</a> <i>void</i> <b>fmgr_hook</b>(event, flinfo, arg) [<>](https://github.com/postgres/postgres/blob/master/src/include/fmgr.h#L728 "Source")

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


## Planner Hooks




<a name="explain_get_index_name_hook" href="#explain_get_index_name_hook">#</a> <i>const char *</i> <b>explain_get_index_name_hook</b>(indexId) [<>](https://github.com/postgres/postgres/blob/master/src/include/commands/explain.h#L62 "Source")

Hook for altering index names in explain statements.

Extensions may override the default name generation mechanism
so that plans involving hypothetical indexes can be explained.

*Inputs:*

* <i>Oid</i> <b>indexId</b> — index id.

*Output:*

Name of the index or `NULL`. In the later case, a default name
will be generated.


<a name="ExplainOneQuery_hook" href="#ExplainOneQuery_hook">#</a> <i>void</i> <b>ExplainOneQuery_hook</b>(query, cursorOptions, into, es, queryString, params, queryEnv) [<>](https://github.com/postgres/postgres/blob/master/src/include/commands/explain.h#L58 "Source")

Hook for overriding explain procedure for a single query.

This hook, if present, should generate explanation for the given query
using other `Explain*` functions and modifying the explain state.

The default behaviour is to plan query using `pg_plan_query()` and than
delegate printing to the `ExplainOnePlan()` function.

*Inputs:*

* <i>Query *</i> <b>query</b> — query that needs explanation.
* <i>int</i> <b>cursorOptions</b> — cursor options in form of a per-bit enum.
  See `CURSOR_OPT_*` macros for detailed documentations.
* <i>IntoClause *</i> <b>into</b> — target information for `SELECT INTO`,
  `CREATE TABLE AS`, and `CREATE MATERIALIZED VIEW`. `NULL` unless
  explaining the contents of a `CreateTableAsStmt`.
* <i>ExplainState *</i> <b>es</b> — current explain state. The hook is free to
  modify it in order to produce output.
* <i>const char *</i> <b>queryString</b> — an actual query string.
* <i>ParamListInfo</i> <b>params</b> — plan parameters.
* <i>QueryEnvironment *</i> <b>queryEnv</b> — context-specific values.

*Output:*

This hook does not produce any output.



<a name="get_attavgwidth_hook" href="#get_attavgwidth_hook">#</a> <i>int32</i> <b>get_attavgwidth_hook</b>(relid, attnum) [<>](https://github.com/postgres/postgres/blob/master/src/include/utils/lsyscache.h#L62 "Source")

Hook for controlling an algorithm for predicting the average width of entries in the column.

This hook, if set, should return the average width of entries in the column.
If returned value is greater than `0`, it is returned to the planner.
Otherwise, the default algorithm is invoked.

*Inputs:*

* <i>Oid</i> <b>relid</b> — relation id.
* <i>AttrNumber</i> <b>attnum</b> — column number.

*Output:*

Average width of entries in the given column of the given relation or zero
to fall back to the default algorithm.


<a name="get_index_stats_hook" href="#get_index_stats_hook">#</a> <i>bool</i> <b>get_index_stats_hook</b>(root, indexOid, indexattnum, vardata) [<>](https://github.com/postgres/postgres/blob/master/src/include/utils/selfuncs.h#L151 "Source")

Hook for overriding index stats lookup.

Given the planner state and an index, the hook should decide if it can provide
any useful stats. If yes, it should supply a `statsTuple` and a `freefunc` and
return `true`. If no, it should return `false`.

Note that `freefunc` must be set if `statsTuple` is set.

Note also that `vardata` should not be changed if `false` is returned.
Postgres will not check whether `statsTuple` and `freefunc` are set.
It will simply overwrite them.

*Inputs:*

* <i>PlannerInfo *</i> <b>root</b> — current planner info.
* <i>Oid</i> <b>indexOid</b> — id of the index that we are looking stats for.
* <i>AttrNumber</i> <b>indexattnum</b> — index column.
* <i>VariableStatData *</i> <b>vardata</b> — container for the return value.


<a name="get_relation_info_hook" href="#get_relation_info_hook">#</a> <i>void</i> <b>get_relation_info_hook</b>(root, relationObjectId, inhparent, rel) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/plancat.h#L25 "Source")

Hook for altering results of the relation info lookup.

This hook allow plugins to editorialize on the info that was obtained from the
catalogs by the default relation info lookup. Actions might include altering
the assumed relation size, removing an index, or adding a hypothetical
index to the `indexlist`.

*Inputs:*

* <i>PlannerInfo *</i> <b>root</b> — current planner info.
* <i>Oid</i> <b>relationObjectId</b> — id of the relation that we are looking
  info for.
* <i>bool</i> <b>inhparent</b> — if true, all we need to do is set up the attr
  arrays: the `RelOptInfo` actually represents the `appendrel` formed by an
  inheritance tree, and so the parent rel's physical size and index information
  isn't important for it.
* <i>RelOptInfo *</i> <b>rel</b> — relation info that can be adjusted.


<a name="get_relation_stats_hook" href="#get_relation_stats_hook">#</a> <i>bool</i> <b>get_relation_stats_hook</b>(root, rte, attnum, vardata) [<>](https://github.com/postgres/postgres/blob/master/src/include/utils/selfuncs.h#L146 "Source")

Hook for overriding relation stats lookup.

Similar to `get_index_stats_hook`, this hook should either return `false`
or take control over relation stats lookup, write output the the `vardata`
container, and return `true`.

See `get_index_stats_hook` for more details.

*Inputs:*

* <i>PlannerInfo *</i> <b>root</b> — current planner info.
* <i>Oid</i> <b>indexOid</b> — id of the index that we are looking stats for.
* <i>AttrNumber</i> <b>indexattnum</b> — index column.
* <i>VariableStatData *</i> <b>vardata</b> — container for the return value.


<a name="planner_hook" href="#planner_hook">#</a> <i>PlannedStmt *</i> <b>planner_hook</b>(parse, cursorOptions, boundParams) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/planner.h#L25 "Source")

Called in query optimizer entry point.

If set, replaces standard planner. Consider inclusion of the standard planner to hook 
if this hook assuming just pre-process or post-process for builtin planner.

*Inputs:*

* <i>Query *</i> <b>parse</b> — query text.
* <i>int</i> <b>cursorOptions</b>
* <i>ParamListInfo</i> <b>boundParams</b>


<a name="join_search_hook" href="#join_search_hook">#</a> <i>RelOptInfo *</i> <b>join_search_hook</b>(root, levels_needed, initial_rels) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/paths.h#L48 "Source")

Called when optimiser chooses order for join relations.

When the hook is set, replaces GEQO or standard join search. 

*Inputs:*

* <i>PlannerInfo *</i> <b>root</b> — query plan root.
* <i>int</i> <b>levels_needed</b> — the number of child joinlist nodes.
* <i>List *</i> <b>initial_rels</b> — list of join relations.


<a name="set_rel_pathlist_hook" href="#set_rel_pathlist_hook">#</a> <i>void</i> <b>set_rel_pathlist_hook</b>(root, rel, rti, rte) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/paths.h#L33 "Source")

Called at the end of building access paths for a base relation.

The hook can apply changes to set of paths by adding new paths or deleting them. 

*Inputs:*

* <i>PlannerInfo *</i> <b>root</b>
* <i>RelOptInfo *</i> <b>rel</b> - relation info.
* <i>Index</i> <b>rti</b> - range table index.
* <i>RangeTblEntry *</i> <b>rte</b> range table entry.


<a name="set_join_pathlist_hook" href="#set_join_pathlist_hook">#</a> <i>void</i> <b>set_join_pathlist_hook</b>(root, joinrel, outerrel, innerrel, jointype, extra) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/paths.h#L42 "Source")

Called at the end of the process of joinrel modification to contain the best paths.

The hook can manipulate path list to perform a postprocess for best paths.

*Inputs:*

* <i>PlannerInfo *</i> <b>root</b> — query plan root.
* <i>RelOptInfo *</i> <b>joinrel</b> — list of paths.
* <i>RelOptInfo *</i> <b>outerrel</b> - list of outer relation paths.
* <i>RelOptInfo *</i> <b>innerrel</b> - list of inner relation paths.
* <i>JoinType</i> <b>jointype</b> - the type of a join.
* <i>JoinPathExtraData *</i> <b>extra</b>


<a name="create_upper_paths_hook" href="#create_upper_paths_hook">#</a> <i>void</i> <b>create_upper_paths_hook</b>(root, stage, input_rel, output_rel) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/planner.h#L32 "Source")

Called when postprocess of the path of set operations occurs.

It's a possibility for extensions to contribute path in relation. 

*Inputs:*

* <i>PlannerInfo *</i> <b>root</b> — query plan root.
* <i>UpperRelationKind</i> <b>stage</b>
* <i>RelOptInfo *</i> <b>input_rel</b>
* <i>RelOptInfo *</i> <b>output_rel</b>


<a name="post_parse_analyze_hook" href="#post_parse_analyze_hook">#</a> <i>void</i> <b>post_parse_analyze_hook</b>(pstate, query) [<>](https://github.com/postgres/postgres/blob/master/src/include/parser/analyze.h#L22 "Source")

Called when parse analyze goes, right after performing transformTopLevelStmt().

Used in several internal methods: 
[pg_analyze_and_rewrite_params()](https://github.com/postgres/postgres/blob/src/backend/tcop/postgres.c#L686), 
[parse_analyze()](https://github.com/postgres/postgres/blob/src/backend/parser/analyze.c#L100).

*Inputs:*

* <i>ParseState *</i> <b>pstate</b> — parse state filled by query_string and queryEnv.  
* <i>Query *</i> <b>query</b> — output result of the transformTopLevelStmt().


## Executor Hooks




<a name="ExecutorStart_hook" href="#ExecutorStart_hook">#</a> <i>void</i> <b>ExecutorStart_hook</b>(queryDesc, eflags) [<>](https://github.com/postgres/postgres/blob/master/src/include/executor/executor.h#L71 "Source")

Called at the beginning of any execution of any query plan.

Note: when it set, replaces the [standard_ExecutorStart()](https://github.com/postgres/postgres/blob/src/backend/executor/execMain.c#L149), 
which contains a lot of predefined logic. 
Consider inclusion of the standard executor to the hook handler 
if you assume adding your logic atop.

*Inputs:*

* <i>QueryDesc *</i> <b>queryDesc</b> — created by CreateQueryDesc, 
tupDesc field of the QueryDesc is filled in to describe the tuples that will be 
returned, and the internal fields (estate and planstate) are set up.
* <i>int</i> <b>eflags</b> — contains flag bits as described in executor.h.


<a name="ExecutorRun_hook" href="#ExecutorRun_hook">#</a> <i>void</i> <b>ExecutorRun_hook</b>(queryDesc, direction, count, execute_once) [<>](https://github.com/postgres/postgres/blob/master/src/include/executor/executor.h#L78 "Source")

Called at any plan execution, after ExecutorStart.

Replaces [standard_ExecutorRun()](https://github.com/postgres/postgres/blob/src/backend/executor/execMain.c#L308)

*Inputs:*

* <i>QueryDesc *</i> <b>queryDesc</b> — query descriptor from the traffic cop.
* <i>ScanDirection</i> <b>direction</b> - if value is NoMovementScanDirection then nothing is done 
except to start up/shut down the destination.
* <i>uint64</i> <b>count</b> — count = 0 is interpreted as no portal limit, i.e., 
run to completion.  Also note that the count limit is only applied to 
retrieved tuples, not for instance to those inserted/updated/deleted by a ModifyTable plan node.
* <i>bool</i> <b>execute_once</b> — becomes equal to true after first execution.

*Output:*

This hook should not provide any output. However output tuples (if any) are sent to 
the destination receiver specified in the QueryDesc. 
The number of tuples processed at the top level can be found in estate->es_processed.


<a name="ExecutorFinish_hook" href="#ExecutorFinish_hook">#</a> <i>void</i> <b>ExecutorFinish_hook</b>(queryDesc) [<>](https://github.com/postgres/postgres/blob/master/src/include/executor/executor.h#L82 "Source")

Called after the last ExecutorRun call

Replaces [standard_ExecutorFinish()](https://github.com/postgres/postgres/blob/src/backend/executor/execMain.c#L408)

*Inputs:*

* <i>QueryDesc *</i> <b>queryDesc</b> — query descriptor from the traffic cop.


<a name="ExecutorEnd_hook" href="#ExecutorEnd_hook">#</a> <i>void</i> <b>ExecutorEnd_hook</b>(queryDesc) [<>](https://github.com/postgres/postgres/blob/master/src/include/executor/executor.h#L86 "Source")

Called at the end of execution of any query plan.

* <i>QueryDesc *</i> <b>queryDesc</b> — query descriptor from the traffic cop.


<a name="ProcessUtility_hook" href="#ProcessUtility_hook">#</a> <i>void</i> <b>ProcessUtility_hook</b>(pstmt, queryString, context, params, queryEnv, dest, completionTag) [<>](https://github.com/postgres/postgres/blob/master/src/include/tcop/utility.h#L32 "Source")

Hook for the ProcessUtility.

Replaces [standard_ProcessUtility()](https://github.com/postgres/postgres/blob/src/backend/tcop/utility.c#L375)

This hook should not provide any output.

*Inputs:*

* <i>PlannedStmt *</i> <b>pstmt</b> — PlannedStmt wrapper for the utility statement
* <i>const char *</i> <b>queryString</b> — original source text of command, 
may be passed multiple times when processing a query string
containing multiple semicolon-separated statements. pstmt->stmt_location and pstmt->stmt_len 
indicates the substring containing the current statement.
* <i>ProcessUtilityContext</i> <b>context</b> — identifies source of statement 
(toplevel client command, non-toplevel client command, subcommand of a larger utility command)
* <i>ParamListInfo</i> <b>params</b> — parameters of an execution.
* <i>QueryEnvironment *</i> <b>queryEnv</b> — execution environment, optional, can be NULL.
* <i>DestReceiver *</i> <b>dest</b> — results receiver.
* <i>char *</i> <b>completionTag</b> — points to a buffer of size COMPLETION_TAG_BUFSIZE 
in which to store a command completion status string


## PL/pgsql Hooks




<a name="func_setup" href="#func_setup">#</a> <i>void</i> <b>func_setup</b>(estate, func) [<>](https://github.com/postgres/postgres/blob/master/src/pl/plpgsql/src/plpgsql.h#L1071 "Source")

Hook for intercepting PLpgSQL function pre-init phase. 

This hook is called when we start a function before we've initialized 
the local variables defined by the function.
Can be useful for time measuring of а function initialization in tandem 
with [func_beg()](Detailed.md#func_beg) and for measuring total execution time 
with the help of [func_end()](Detailed.md#func_end).

Before any call to func_setup, PLpgSQL fills in the error_callback 
and assign_expr fields with pointers to its own plpgsql_exec_error_callback 
and exec_assign_expr functions.

*Inputs:*

* <i>PLpgSQL_execstate *</i> <b>estate</b> — runtime execution data.
* <i>PLpgSQL_function *</i> <b>func</b> — PLpgSQL compiled function.


<a name="func_beg" href="#func_beg">#</a> <i>void</i> <b>func_beg</b>(estate, func) [<>](https://github.com/postgres/postgres/blob/master/src/pl/plpgsql/src/plpgsql.h#L1072 "Source")

Hook for intercepting post-init phase. 

This hook is called when we start PLpgSQL function, after we've initialized 
the local variables.
The hook can be used for pre-validation of a function arguments. 

*Inputs:*

* <i>PLpgSQL_execstate *</i> <b>estate</b> — runtime execution data.
* <i>PLpgSQL_function *</i> <b>func</b> — PLpgSQL compiled function.


<a name="func_end" href="#func_end">#</a> <i>void</i> <b>func_end</b>(estate, func) [<>](https://github.com/postgres/postgres/blob/master/src/pl/plpgsql/src/plpgsql.h#L1073 "Source")

Hook for intercepting end of a function. 

This hook is called at the end of PLpgSQL function.
Can be used as a function callback.

*Inputs:*

* <i>PLpgSQL_execstate *</i> <b>estate</b> — runtime execution data.
* <i>PLpgSQL_function *</i> <b>func</b> — PLpgSQL compiled function.


<a name="stmt_beg" href="#stmt_beg">#</a> <i>void</i> <b>stmt_beg</b>(estate, stmt) [<>](https://github.com/postgres/postgres/blob/master/src/pl/plpgsql/src/plpgsql.h#L1074 "Source")

Called before each statement of a function.

*Inputs:*

* <i>PLpgSQL_execstate *</i> <b>estate</b> — runtime execution data.
* <i>PLpgSQL_stmt *</i> <b>stmt</b> — execution node.


<a name="stmt_end" href="#stmt_end">#</a> <i>void</i> <b>stmt_end</b>(estate, stmt) [<>](https://github.com/postgres/postgres/blob/master/src/pl/plpgsql/src/plpgsql.h#L1075 "Source")

Called after each statement of a function.

*Inputs:*

* <i>PLpgSQL_execstate *</i> <b>estate</b> — runtime execution data.
* <i>PLpgSQL_stmt *</i> <b>stmt</b> — execution node.


