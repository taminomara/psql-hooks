# Postgresql hooks documentation

Provide description here

* [General Hooks](#general-hooks)
* [Security Hooks](#security-hooks)
* [Planner Hooks](#planner-hooks)
* [Executor Hooks](#executor-hooks)
* [PL/pgsql Hooks](#ps-pgsql-hooks)


## [General Hooks](Detailed.md#general-hooks)



* [emit_log_hook](Detailed.md#emit_log_hook) — Short description of this hook.
* [shmem_startup_hook](Detailed.md#shmem_startup_hook) — Short description of this hook.

## [Security Hooks](Detailed.md#security-hooks)



* [check_password_hook](Detailed.md#check_password_hook) — Short description of this hook.
* [ClientAuthentication_hook](Detailed.md#ClientAuthentication_hook) — Short description of this hook.
* [ExecutorCheckPerms_hook](Detailed.md#ExecutorCheckPerms_hook) — Short description of this hook.
* [needs_fmgr_hook](Detailed.md#needs_fmgr_hook) — Short description of this hook.
* [fmgr_hook](Detailed.md#fmgr_hook) — Short description of this hook.
* [object_access_hook](Detailed.md#object_access_hook) — Multi-pass hook to monitor accesses to objects.
* [row_security_policy_hook_permissive](Detailed.md#row_security_policy_hook_permissive) — Short description of this hook.
* [row_security_policy_hook_restrictive](Detailed.md#row_security_policy_hook_restrictive) — Short description of this hook.

## [Planner Hooks](Detailed.md#planner-hooks)



* [explain_get_index_name_hook](Detailed.md#explain_get_index_name_hook) — Short description of this hook.
* [ExplainOneQuery_hook](Detailed.md#ExplainOneQuery_hook) — Short description of this hook.
* [get_attavgwidth_hook](Detailed.md#get_attavgwidth_hook) — Short description of this hook.
* [get_index_stats_hook](Detailed.md#get_index_stats_hook) — Short description of this hook.
* [get_relation_info_hook](Detailed.md#get_relation_info_hook) — Short description of this hook.
* [get_relation_stats_hook](Detailed.md#get_relation_stats_hook) — Short description of this hook.
* [planner_hook](Detailed.md#planner_hook) — Short description of this hook.
* [join_search_hook](Detailed.md#join_search_hook) — Short description of this hook.
* [set_rel_pathlist_hook](Detailed.md#set_rel_pathlist_hook) — Short description of this hook.
* [set_join_pathlist_hook](Detailed.md#set_join_pathlist_hook) — Short description of this hook.
* [create_upper_paths_hook](Detailed.md#create_upper_paths_hook) — Short description of this hook.
* [post_parse_analyze_hook](Detailed.md#post_parse_analyze_hook) — Short description of this hook.

## [Executor Hooks](Detailed.md#executor-hooks)



* [ExecutorStart_hook](Detailed.md#ExecutorStart_hook) — Short description of this hook.
* [ExecutorRun_hook](Detailed.md#ExecutorRun_hook) — Short description of this hook.
* [ExecutorFinish_hook](Detailed.md#ExecutorFinish_hook) — Short description of this hook.
* [ExecutorEnd_hook](Detailed.md#ExecutorEnd_hook) — Short description of this hook.
* [ProcessUtility_hook](Detailed.md#ProcessUtility_hook) — Short description of this hook.

## [PL/pgsql Hooks](Detailed.md#ps-pgsql-hooks)



* [func_setup](Detailed.md#func_setup) — Short description of this hook.
* [func_beg](Detailed.md#func_beg) — Short description of this hook.
* [func_end](Detailed.md#func_end) — Short description of this hook.
* [stmt_beg](Detailed.md#stmt_beg) — Short description of this hook.
* [stmt_end](Detailed.md#stmt_end) — Short description of this hook.

