# Postgresql hooks documentation

Provide description here.

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

Hook for plugins to initialize their shared memory.

This hook is called by postmaster or by a standalone backend
right after postgres initializes its shared memory and semaphores
so that plugins have chance to initialize their shared state.

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

Hook for plugins to control the authentication process.

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

Multi-pass hook to monitor accesses to objects.

Can be triggered by the following entrypoints:\
[RunFunctionExecuteHook()](https://doxygen.postgresql.org/objectaccess_8c.html#a41ee35a449248c380c9a8fb0529bd4af)\
[RunNamespaceSearchHook()](https://doxygen.postgresql.org/objectaccess_8c.html#a6e3676b4278836b87b28148eb9d666fc)\
[RunObjectDropHook()](https://doxygen.postgresql.org/objectaccess_8c.html#a1b20ed6ac04157d8453802a07254ca90)\
[RunObjectPostAlterHook()](https://doxygen.postgresql.org/objectaccess_8c.html#a3250abdee32af9fcb65c2a5fc1a1b496)\
[RunObjectPostCreateHook()](https://doxygen.postgresql.org/objectaccess_8c.html#acba44450c8b47e3fe01ff1df9eb1e409)

*Inputs:*

* <i>ObjectAccessType</i> <b>access</b> — access event type ([ref](https://doxygen.postgresql.org/objectaccess_8h.html#a9b9ef77e618c4d2025e0413a6fe214a0))
* <i>Oid</i> <b>classId</b>
* <i>Oid</i> <b>objectId</b>
* <i>int</i> <b>subId</b>
* <i>void *</i> <b>arg</b> — entrypoint-specific argument (optional)

*Output:*

Hook should not produce any output.

*Use-cases:*

Useful for security and logging extensions.


<a name="row_security_policy_hook_permissive" href="#row_security_policy_hook_permissive">#</a> <i>List *</i> <b>row_security_policy_hook_permissive</b>(cmdtype, relation) [<>](https://github.com/postgres/postgres/blob/master/src/include/rewrite/rowsecurity.h#L40 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>CmdType</i> <b>cmdtype</b> — ...
* <i>Relation</i> <b>relation</b> — ...

*Output:*

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="row_security_policy_hook_restrictive" href="#row_security_policy_hook_restrictive">#</a> <i>List *</i> <b>row_security_policy_hook_restrictive</b>(cmdtype, relation) [<>](https://github.com/postgres/postgres/blob/master/src/include/rewrite/rowsecurity.h#L42 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>CmdType</i> <b>cmdtype</b> — ...
* <i>Relation</i> <b>relation</b> — ...

*Output:*

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


## Function Manager Hooks




<a name="needs_fmgr_hook" href="#needs_fmgr_hook">#</a> <i>bool</i> <b>needs_fmgr_hook</b>(fn_oid) [<>](https://github.com/postgres/postgres/blob/master/src/include/fmgr.h#L727 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>Oid</i> <b>fn_oid</b> — ...

*Output:*

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="fmgr_hook" href="#fmgr_hook">#</a> <i>void</i> <b>fmgr_hook</b>(event, flinfo, arg) [<>](https://github.com/postgres/postgres/blob/master/src/include/fmgr.h#L728 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>FmgrHookEventType</i> <b>event</b> — ...
* <i>FmgrInfo *</i> <b>flinfo</b> — ...
* <i>Datum *</i> <b>arg</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


## Planner Hooks




<a name="explain_get_index_name_hook" href="#explain_get_index_name_hook">#</a> <i>const char *</i> <b>explain_get_index_name_hook</b>(indexId) [<>](https://github.com/postgres/postgres/blob/master/src/include/commands/explain.h#L62 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>Oid</i> <b>indexId</b> — ...

*Output:*

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="ExplainOneQuery_hook" href="#ExplainOneQuery_hook">#</a> <i>void</i> <b>ExplainOneQuery_hook</b>(query, cursorOptions, into, es, queryString, params, queryEnv) [<>](https://github.com/postgres/postgres/blob/master/src/include/commands/explain.h#L58 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>Query *</i> <b>query</b> — ...
* <i>int</i> <b>cursorOptions</b> — ...
* <i>IntoClause *</i> <b>into</b> — ...
* <i>ExplainState *</i> <b>es</b> — ...
* <i>const char *</i> <b>queryString</b> — ...
* <i>ParamListInfo</i> <b>params</b> — ...
* <i>QueryEnvironment *</i> <b>queryEnv</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="get_attavgwidth_hook" href="#get_attavgwidth_hook">#</a> <i>int32</i> <b>get_attavgwidth_hook</b>(relid, attnum) [<>](https://github.com/postgres/postgres/blob/master/src/include/utils/lsyscache.h#L62 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>Oid</i> <b>relid</b> — ...
* <i>AttrNumber</i> <b>attnum</b> — ...

*Output:*

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="get_index_stats_hook" href="#get_index_stats_hook">#</a> <i>bool</i> <b>get_index_stats_hook</b>(root, indexOid, indexattnum, vardata) [<>](https://github.com/postgres/postgres/blob/master/src/include/utils/selfuncs.h#L151 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannerInfo *</i> <b>root</b> — ...
* <i>Oid</i> <b>indexOid</b> — ...
* <i>AttrNumber</i> <b>indexattnum</b> — ...
* <i>VariableStatData *</i> <b>vardata</b> — ...

*Output:*

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="get_relation_info_hook" href="#get_relation_info_hook">#</a> <i>void</i> <b>get_relation_info_hook</b>(root, relationObjectId, inhparent, rel) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/plancat.h#L25 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannerInfo *</i> <b>root</b> — ...
* <i>Oid</i> <b>relationObjectId</b> — ...
* <i>bool</i> <b>inhparent</b> — ...
* <i>RelOptInfo *</i> <b>rel</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="get_relation_stats_hook" href="#get_relation_stats_hook">#</a> <i>bool</i> <b>get_relation_stats_hook</b>(root, rte, attnum, vardata) [<>](https://github.com/postgres/postgres/blob/master/src/include/utils/selfuncs.h#L146 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannerInfo *</i> <b>root</b> — ...
* <i>RangeTblEntry *</i> <b>rte</b> — ...
* <i>AttrNumber</i> <b>attnum</b> — ...
* <i>VariableStatData *</i> <b>vardata</b> — ...

*Output:*

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="planner_hook" href="#planner_hook">#</a> <i>PlannedStmt *</i> <b>planner_hook</b>(parse, cursorOptions, boundParams) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/planner.h#L25 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>Query *</i> <b>parse</b> — ...
* <i>int</i> <b>cursorOptions</b> — ...
* <i>ParamListInfo</i> <b>boundParams</b> — ...

*Output:*

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="join_search_hook" href="#join_search_hook">#</a> <i>RelOptInfo *</i> <b>join_search_hook</b>(root, levels_needed, initial_rels) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/paths.h#L48 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannerInfo *</i> <b>root</b> — ...
* <i>int</i> <b>levels_needed</b> — ...
* <i>List *</i> <b>initial_rels</b> — ...

*Output:*

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="set_rel_pathlist_hook" href="#set_rel_pathlist_hook">#</a> <i>void</i> <b>set_rel_pathlist_hook</b>(root, rel, rti, rte) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/paths.h#L33 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannerInfo *</i> <b>root</b> — ...
* <i>RelOptInfo *</i> <b>rel</b> — ...
* <i>Index</i> <b>rti</b> — ...
* <i>RangeTblEntry *</i> <b>rte</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="set_join_pathlist_hook" href="#set_join_pathlist_hook">#</a> <i>void</i> <b>set_join_pathlist_hook</b>(root, joinrel, outerrel, innerrel, jointype, extra) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/paths.h#L42 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannerInfo *</i> <b>root</b> — ...
* <i>RelOptInfo *</i> <b>joinrel</b> — ...
* <i>RelOptInfo *</i> <b>outerrel</b> — ...
* <i>RelOptInfo *</i> <b>innerrel</b> — ...
* <i>JoinType</i> <b>jointype</b> — ...
* <i>JoinPathExtraData *</i> <b>extra</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="create_upper_paths_hook" href="#create_upper_paths_hook">#</a> <i>void</i> <b>create_upper_paths_hook</b>(root, stage, input_rel, output_rel) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/planner.h#L32 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannerInfo *</i> <b>root</b> — ...
* <i>UpperRelationKind</i> <b>stage</b> — ...
* <i>RelOptInfo *</i> <b>input_rel</b> — ...
* <i>RelOptInfo *</i> <b>output_rel</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="post_parse_analyze_hook" href="#post_parse_analyze_hook">#</a> <i>void</i> <b>post_parse_analyze_hook</b>(pstate, query) [<>](https://github.com/postgres/postgres/blob/master/src/include/parser/analyze.h#L22 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>ParseState *</i> <b>pstate</b> — ...
* <i>Query *</i> <b>query</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


## Executor Hooks




<a name="ExecutorStart_hook" href="#ExecutorStart_hook">#</a> <i>void</i> <b>ExecutorStart_hook</b>(queryDesc, eflags) [<>](https://github.com/postgres/postgres/blob/master/src/include/executor/executor.h#L71 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>QueryDesc *</i> <b>queryDesc</b> — ...
* <i>int</i> <b>eflags</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="ExecutorRun_hook" href="#ExecutorRun_hook">#</a> <i>void</i> <b>ExecutorRun_hook</b>(queryDesc, direction, count, execute_once) [<>](https://github.com/postgres/postgres/blob/master/src/include/executor/executor.h#L78 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>QueryDesc *</i> <b>queryDesc</b> — ...
* <i>ScanDirection</i> <b>direction</b> — ...
* <i>uint64</i> <b>count</b> — ...
* <i>bool</i> <b>execute_once</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="ExecutorFinish_hook" href="#ExecutorFinish_hook">#</a> <i>void</i> <b>ExecutorFinish_hook</b>(queryDesc) [<>](https://github.com/postgres/postgres/blob/master/src/include/executor/executor.h#L82 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>QueryDesc *</i> <b>queryDesc</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="ExecutorEnd_hook" href="#ExecutorEnd_hook">#</a> <i>void</i> <b>ExecutorEnd_hook</b>(queryDesc) [<>](https://github.com/postgres/postgres/blob/master/src/include/executor/executor.h#L86 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>QueryDesc *</i> <b>queryDesc</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="ProcessUtility_hook" href="#ProcessUtility_hook">#</a> <i>void</i> <b>ProcessUtility_hook</b>(pstmt, queryString, context, params, queryEnv, dest, completionTag) [<>](https://github.com/postgres/postgres/blob/master/src/include/tcop/utility.h#L32 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannedStmt *</i> <b>pstmt</b> — ...
* <i>const char *</i> <b>queryString</b> — ...
* <i>ProcessUtilityContext</i> <b>context</b> — ...
* <i>ParamListInfo</i> <b>params</b> — ...
* <i>QueryEnvironment *</i> <b>queryEnv</b> — ...
* <i>DestReceiver *</i> <b>dest</b> — ...
* <i>char *</i> <b>completionTag</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


## PL/pgsql Hooks




<a name="func_setup" href="#func_setup">#</a> <i>void</i> <b>func_setup</b>(estate, func) [<>](https://github.com/postgres/postgres/blob/master/src/pl/plpgsql/src/plpgsql.h#L1071 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PLpgSQL_execstate *</i> <b>estate</b> — ...
* <i>PLpgSQL_function *</i> <b>func</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="func_beg" href="#func_beg">#</a> <i>void</i> <b>func_beg</b>(estate, func) [<>](https://github.com/postgres/postgres/blob/master/src/pl/plpgsql/src/plpgsql.h#L1072 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PLpgSQL_execstate *</i> <b>estate</b> — ...
* <i>PLpgSQL_function *</i> <b>func</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="func_end" href="#func_end">#</a> <i>void</i> <b>func_end</b>(estate, func) [<>](https://github.com/postgres/postgres/blob/master/src/pl/plpgsql/src/plpgsql.h#L1073 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PLpgSQL_execstate *</i> <b>estate</b> — ...
* <i>PLpgSQL_function *</i> <b>func</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="stmt_beg" href="#stmt_beg">#</a> <i>void</i> <b>stmt_beg</b>(estate, stmt) [<>](https://github.com/postgres/postgres/blob/master/src/pl/plpgsql/src/plpgsql.h#L1074 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PLpgSQL_execstate *</i> <b>estate</b> — ...
* <i>PLpgSQL_stmt *</i> <b>stmt</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="stmt_end" href="#stmt_end">#</a> <i>void</i> <b>stmt_end</b>(estate, stmt) [<>](https://github.com/postgres/postgres/blob/master/src/pl/plpgsql/src/plpgsql.h#L1075 "Source")

Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PLpgSQL_execstate *</i> <b>estate</b> — ...
* <i>PLpgSQL_stmt *</i> <b>stmt</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


