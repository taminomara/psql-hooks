# Postgresql hooks documentation

Unofficial documentation for PostgreSQL hooks.

> *Denial of responsibility:*
> 
> This work is not a part of the official PostgreSQL documentation.
> 
> Contents of this repository were compiled by Begishev Nikita and
> Goncharov Vladimir, neither of whom appear to be a developer or a maintainer
> of the PostgreSQL Database Management System.
>
> Use this documentation at your own risk.
>
> 
> *Copyright notice:*
> 
> This work combines some research made to this repo by all contributors with
> information acquired from the postgres source code, comments and
> documentation. Some contents of this work were copied from source code
> comments as is, others were written from scratch.
> 
> In no way we (Begishev Nikita and Goncharov Vladimir) claim copyright on texts
> that were copied or adapted from the sources described above.
>
> This work is distributed under the terms of the PostgreSQL License, a copy of
> which may be found in the file called 'License.md'.

PostgreSQL hooks are a simple way to extend functionality of the database.
They allow extensions to introspect database state, react to events and
interfere with database operations.

In terms of the programming language, each hook is a pointer to a function
of a specific type, initially set to be `NULL`.

Upon init, database extensions are free to overwrite those function pointers
with their own values. A previous value of the overwritten pointer is usually
stored withing the extension local memory.

During its work, postgres checks whether certain function pointers are not null
and if that's the case, calls them.

See the [detailed description](Detailed.md) for an explanation on
how to implement a hook and an example.

* [General Hooks](#general-hooks)
* [Security Hooks](#security-hooks)
* [Function Manager Hooks](#function-manager-hooks)
* [Planner Hooks](#planner-hooks)
* [Executor Hooks](#executor-hooks)
* [PL/pgsql Hooks](#plpgsql-hooks)


## [General Hooks](Detailed.md#general-hooks)



* [emit_log_hook](Detailed.md#emit_log_hook) — hook for intercepting messages before they are sent to the server log.
* [shmem_startup_hook](Detailed.md#shmem_startup_hook) — hook for extensions to initialize their shared memory.

## [Security Hooks](Detailed.md#security-hooks)



* [check_password_hook](Detailed.md#check_password_hook) — hook for enforcing password constraints and performing action on password change.
* [ClientAuthentication_hook](Detailed.md#ClientAuthentication_hook) — hook for controlling the authentication process.
* [ExecutorCheckPerms_hook](Detailed.md#ExecutorCheckPerms_hook) — hook for adding additional security checks on the per-relation level.
* [object_access_hook](Detailed.md#object_access_hook) — hook to monitor accesses to objects.
* [row_security_policy_hook_permissive](Detailed.md#row_security_policy_hook_permissive) — hook to add policies which are combined with the other permissive policies.
* [row_security_policy_hook_restrictive](Detailed.md#row_security_policy_hook_restrictive) — hook to add policies which are enforced, regardless of other policies.

## [Function Manager Hooks](Detailed.md#function-manager-hooks)



* [needs_fmgr_hook](Detailed.md#needs_fmgr_hook) — auxiliary hook which decides whether `fmgr_hook` should be applied to a function.
* [fmgr_hook](Detailed.md#fmgr_hook) — hook for controlling function execution process.

## [Planner Hooks](Detailed.md#planner-hooks)



* [explain_get_index_name_hook](Detailed.md#explain_get_index_name_hook) — hook for altering index names in explain statements.
* [ExplainOneQuery_hook](Detailed.md#ExplainOneQuery_hook) — hook for overriding explain procedure for a single query.
* [get_attavgwidth_hook](Detailed.md#get_attavgwidth_hook) — hook for controlling an algorithm for predicting the average width of entries in the column.
* [get_index_stats_hook](Detailed.md#get_index_stats_hook) — hook for overriding index stats lookup.
* [get_relation_info_hook](Detailed.md#get_relation_info_hook) — hook for altering results of the relation info lookup.
* [get_relation_stats_hook](Detailed.md#get_relation_stats_hook) — hook for overriding relation stats lookup.
* [planner_hook](Detailed.md#planner_hook) — called in query optimizer entry point.
* [join_search_hook](Detailed.md#join_search_hook) — called when optimiser chooses order for join relations.
* [set_rel_pathlist_hook](Detailed.md#set_rel_pathlist_hook) — called at the end of building access paths for a base relation.
* [set_join_pathlist_hook](Detailed.md#set_join_pathlist_hook) — called at the end of the process of joinrel modification to contain the best paths.
* [create_upper_paths_hook](Detailed.md#create_upper_paths_hook) — called when postprocess of the path of set operations occurs.
* [post_parse_analyze_hook](Detailed.md#post_parse_analyze_hook) — called when parse analyze goes, right after performing transformTopLevelStmt().

## [Executor Hooks](Detailed.md#executor-hooks)



* [ExecutorStart_hook](Detailed.md#ExecutorStart_hook) — called at the beginning of any execution of any query plan.
* [ExecutorRun_hook](Detailed.md#ExecutorRun_hook) — called at any plan execution, after ExecutorStart.
* [ExecutorFinish_hook](Detailed.md#ExecutorFinish_hook) — called after the last ExecutorRun call
* [ExecutorEnd_hook](Detailed.md#ExecutorEnd_hook) — called at the end of execution of any query plan.
* [ProcessUtility_hook](Detailed.md#ProcessUtility_hook) — hook for the ProcessUtility.

## [PL/pgsql Hooks](Detailed.md#plpgsql-hooks)



* [func_setup](Detailed.md#func_setup) — hook for intercepting PLpgSQL function pre-init phase.
* [func_beg](Detailed.md#func_beg) — hook for intercepting post-init phase.
* [func_end](Detailed.md#func_end) — hook for intercepting end of a function.
* [stmt_beg](Detailed.md#stmt_beg) — called before each statement of a function.
* [stmt_end](Detailed.md#stmt_end) — called after each statement of a function.

