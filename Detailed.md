# Postgresql hooks documentation

Provide description here.

* [General hooks](#general-hooks)


## General hooks

Provide description here.


<a name="needs_fmgr_hook" href="#needs_fmgr_hook">#</a> <i>bool</i> <b>needs_fmgr_hook</b>(fn_oid) [<>](https://github.com/postgres/postgres/blob/master/src/include/fmgr.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>Oid</i> <b>fn_oid</b> — ...

**Output:**

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="fmgr_hook" href="#fmgr_hook">#</a> <i>void</i> <b>fmgr_hook</b>(event, flinfo, arg) [<>](https://github.com/postgres/postgres/blob/master/src/include/fmgr.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>FmgrHookEventType</i> <b>event</b> — ...
* <i>FmgrInfo *</i> <b>flinfo</b> — ...
* <i>Datum *</i> <b>arg</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="object_access_hook" href="#object_access_hook">#</a> <i>void</i> <b>object_access_hook</b>(access, classId, objectId, subId, arg) [<>](https://github.com/postgres/postgres/blob/master/src/include/catalog/objectaccess.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>ObjectAccessType</i> <b>access</b> — ...
* <i>Oid</i> <b>classId</b> — ...
* <i>Oid</i> <b>objectId</b> — ...
* <i>int</i> <b>subId</b> — ...
* <i>void *</i> <b>arg</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="ExplainOneQuery_hook" href="#ExplainOneQuery_hook">#</a> <i>void</i> <b>ExplainOneQuery_hook</b>(query, cursorOptions, into, es, queryString, params, queryEnv) [<>](https://github.com/postgres/postgres/blob/master/src/include/commands/explain.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>Query *</i> <b>query</b> — ...
* <i>int</i> <b>cursorOptions</b> — ...
* <i>IntoClause *</i> <b>into</b> — ...
* <i>ExplainState *</i> <b>es</b> — ...
* <i>const char *</i> <b>queryString</b> — ...
* <i>ParamListInfo</i> <b>params</b> — ...
* <i>QueryEnvironment *</i> <b>queryEnv</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="explain_get_index_name_hook" href="#explain_get_index_name_hook">#</a> <i>const char *</i> <b>explain_get_index_name_hook</b>(indexId) [<>](https://github.com/postgres/postgres/blob/master/src/include/commands/explain.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>Oid</i> <b>indexId</b> — ...

**Output:**

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="check_password_hook" href="#check_password_hook">#</a> <i>void</i> <b>check_password_hook</b>(username, shadow_pass, password_type, validuntil_time, validuntil_null) [<>](https://github.com/postgres/postgres/blob/master/src/include/commands/user.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>const char *</i> <b>username</b> — ...
* <i>const char *</i> <b>shadow_pass</b> — ...
* <i>PasswordType</i> <b>password_type</b> — ...
* <i>Datum</i> <b>validuntil_time</b> — ...
* <i>bool</i> <b>validuntil_null</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="ExecutorStart_hook" href="#ExecutorStart_hook">#</a> <i>void</i> <b>ExecutorStart_hook</b>(queryDesc, eflags) [<>](https://github.com/postgres/postgres/blob/master/src/include/executor/executor.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>QueryDesc *</i> <b>queryDesc</b> — ...
* <i>int</i> <b>eflags</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="ExecutorRun_hook" href="#ExecutorRun_hook">#</a> <i>void</i> <b>ExecutorRun_hook</b>(queryDesc, direction, count, execute_once) [<>](https://github.com/postgres/postgres/blob/master/src/include/executor/executor.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>QueryDesc *</i> <b>queryDesc</b> — ...
* <i>ScanDirection</i> <b>direction</b> — ...
* <i>uint64</i> <b>count</b> — ...
* <i>bool</i> <b>execute_once</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="ExecutorFinish_hook" href="#ExecutorFinish_hook">#</a> <i>void</i> <b>ExecutorFinish_hook</b>(queryDesc) [<>](https://github.com/postgres/postgres/blob/master/src/include/executor/executor.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>QueryDesc *</i> <b>queryDesc</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="ExecutorEnd_hook" href="#ExecutorEnd_hook">#</a> <i>void</i> <b>ExecutorEnd_hook</b>(queryDesc) [<>](https://github.com/postgres/postgres/blob/master/src/include/executor/executor.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>QueryDesc *</i> <b>queryDesc</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="ExecutorCheckPerms_hook" href="#ExecutorCheckPerms_hook">#</a> <i>bool</i> <b>ExecutorCheckPerms_hook</b>(*, bool) [<>](https://github.com/postgres/postgres/blob/master/src/include/executor/executor.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>List</i> <b>*</b> — ...
* <i></i> <b>bool</b> — ...

**Output:**

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="ClientAuthentication_hook" href="#ClientAuthentication_hook">#</a> <i>void</i> <b>ClientAuthentication_hook</b>(*, int) [<>](https://github.com/postgres/postgres/blob/master/src/include/libpq/auth.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>Port</i> <b>*</b> — ...
* <i></i> <b>int</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="set_rel_pathlist_hook" href="#set_rel_pathlist_hook">#</a> <i>void</i> <b>set_rel_pathlist_hook</b>(root, rel, rti, rte) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/paths.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannerInfo *</i> <b>root</b> — ...
* <i>RelOptInfo *</i> <b>rel</b> — ...
* <i>Index</i> <b>rti</b> — ...
* <i>RangeTblEntry *</i> <b>rte</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="set_join_pathlist_hook" href="#set_join_pathlist_hook">#</a> <i>void</i> <b>set_join_pathlist_hook</b>(root, joinrel, outerrel, innerrel, jointype, extra) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/paths.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannerInfo *</i> <b>root</b> — ...
* <i>RelOptInfo *</i> <b>joinrel</b> — ...
* <i>RelOptInfo *</i> <b>outerrel</b> — ...
* <i>RelOptInfo *</i> <b>innerrel</b> — ...
* <i>JoinType</i> <b>jointype</b> — ...
* <i>JoinPathExtraData *</i> <b>extra</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="join_search_hook" href="#join_search_hook">#</a> <i>RelOptInfo *</i> <b>join_search_hook</b>(root, levels_needed, initial_rels) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/paths.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannerInfo *</i> <b>root</b> — ...
* <i>int</i> <b>levels_needed</b> — ...
* <i>List *</i> <b>initial_rels</b> — ...

**Output:**

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="get_relation_info_hook" href="#get_relation_info_hook">#</a> <i>void</i> <b>get_relation_info_hook</b>(root, relationObjectId, inhparent, rel) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/plancat.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannerInfo *</i> <b>root</b> — ...
* <i>Oid</i> <b>relationObjectId</b> — ...
* <i>bool</i> <b>inhparent</b> — ...
* <i>RelOptInfo *</i> <b>rel</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="planner_hook" href="#planner_hook">#</a> <i>PlannedStmt *</i> <b>planner_hook</b>(parse, cursorOptions, boundParams) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/planner.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>Query *</i> <b>parse</b> — ...
* <i>int</i> <b>cursorOptions</b> — ...
* <i>ParamListInfo</i> <b>boundParams</b> — ...

**Output:**

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="create_upper_paths_hook" href="#create_upper_paths_hook">#</a> <i>void</i> <b>create_upper_paths_hook</b>(root, stage, input_rel, output_rel) [<>](https://github.com/postgres/postgres/blob/master/src/include/optimizer/planner.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannerInfo *</i> <b>root</b> — ...
* <i>UpperRelationKind</i> <b>stage</b> — ...
* <i>RelOptInfo *</i> <b>input_rel</b> — ...
* <i>RelOptInfo *</i> <b>output_rel</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="post_parse_analyze_hook" href="#post_parse_analyze_hook">#</a> <i>void</i> <b>post_parse_analyze_hook</b>(pstate, query) [<>](https://github.com/postgres/postgres/blob/master/src/include/parser/analyze.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>ParseState *</i> <b>pstate</b> — ...
* <i>Query *</i> <b>query</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="row_security_policy_hook_permissive" href="#row_security_policy_hook_permissive">#</a> <i>List *</i> <b>row_security_policy_hook_permissive</b>(cmdtype, relation) [<>](https://github.com/postgres/postgres/blob/master/src/include/rewrite/rowsecurity.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>CmdType</i> <b>cmdtype</b> — ...
* <i>Relation</i> <b>relation</b> — ...

**Output:**

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="row_security_policy_hook_restrictive" href="#row_security_policy_hook_restrictive">#</a> <i>List *</i> <b>row_security_policy_hook_restrictive</b>(cmdtype, relation) [<>](https://github.com/postgres/postgres/blob/master/src/include/rewrite/rowsecurity.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>CmdType</i> <b>cmdtype</b> — ...
* <i>Relation</i> <b>relation</b> — ...

**Output:**

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="shmem_startup_hook" href="#shmem_startup_hook">#</a> <i>void</i> <b>shmem_startup_hook</b>() [<>](https://github.com/postgres/postgres/blob/master/src/include/storage/ipc.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

There are no inputs for this hook. Is there a global state this hook should introspect?
**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="ProcessUtility_hook" href="#ProcessUtility_hook">#</a> <i>void</i> <b>ProcessUtility_hook</b>(pstmt, queryString, context, params, queryEnv, dest, completionTag) [<>](https://github.com/postgres/postgres/blob/master/src/include/tcop/utility.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannedStmt *</i> <b>pstmt</b> — ...
* <i>const char *</i> <b>queryString</b> — ...
* <i>ProcessUtilityContext</i> <b>context</b> — ...
* <i>ParamListInfo</i> <b>params</b> — ...
* <i>QueryEnvironment *</i> <b>queryEnv</b> — ...
* <i>DestReceiver *</i> <b>dest</b> — ...
* <i>char *</i> <b>completionTag</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="emit_log_hook" href="#emit_log_hook">#</a> <i>void</i> <b>emit_log_hook</b>(edata) [<>](https://github.com/postgres/postgres/blob/master/src/include/utils/elog.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>ErrorData *</i> <b>edata</b> — ...

**Output:**

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should thrown an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="get_attavgwidth_hook" href="#get_attavgwidth_hook">#</a> <i>int32</i> <b>get_attavgwidth_hook</b>(relid, attnum) [<>](https://github.com/postgres/postgres/blob/master/src/include/utils/lsyscache.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>Oid</i> <b>relid</b> — ...
* <i>AttrNumber</i> <b>attnum</b> — ...

**Output:**

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="get_relation_stats_hook" href="#get_relation_stats_hook">#</a> <i>bool</i> <b>get_relation_stats_hook</b>(root, rte, attnum, vardata) [<>](https://github.com/postgres/postgres/blob/master/src/include/utils/selfuncs.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannerInfo *</i> <b>root</b> — ...
* <i>RangeTblEntry *</i> <b>rte</b> — ...
* <i>AttrNumber</i> <b>attnum</b> — ...
* <i>VariableStatData *</i> <b>vardata</b> — ...

**Output:**

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


<a name="get_index_stats_hook" href="#get_index_stats_hook">#</a> <i>bool</i> <b>get_index_stats_hook</b>(root, indexOid, indexattnum, vardata) [<>](https://github.com/postgres/postgres/blob/master/src/include/utils/selfuncs.h "Source")

Short description of this hook.
Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

**Inputs:**

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannerInfo *</i> <b>root</b> — ...
* <i>Oid</i> <b>indexOid</b> — ...
* <i>AttrNumber</i> <b>indexattnum</b> — ...
* <i>VariableStatData *</i> <b>vardata</b> — ...

**Output:**

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

**Use-cases:**

It you can think of any use-cases for this hook, spell it out. If no, delete this section.


