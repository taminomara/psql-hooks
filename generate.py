from collections import namedtuple

import os

import jinja2

HookType = namedtuple('HookType', 'name output inputs')
HookInput = namedtuple('HookInput', 'type name')
Hook = namedtuple('Hook', 'type name source_link')
HookSection = namedtuple('HookSection', 'name slug short_desc long_desc hooks')


def link(path):
    return 'https://github.com/postgres/postgres/blob/master/' + path


set_rel_pathlist_hook_type = HookType(
    name='set_rel_pathlist_hook_type',
    output='void',
    inputs=[
        HookInput('PlannerInfo *', 'root'),
        HookInput('RelOptInfo *', 'rel'),
        HookInput('Index', 'rti'),
        HookInput('RangeTblEntry *', 'rte'),
    ]
)
set_join_pathlist_hook_type = HookType(
    name='set_join_pathlist_hook_type',
    output='void',
    inputs=[
        HookInput('PlannerInfo *', 'root'),
        HookInput('RelOptInfo *', 'joinrel'),
        HookInput('RelOptInfo *', 'outerrel'),
        HookInput('RelOptInfo *', 'innerrel'),
        HookInput('JoinType', 'jointype'),
        HookInput('JoinPathExtraData *', 'extra'),
    ]
)
needs_fmgr_hook_type = HookType(
    name='needs_fmgr_hook_type',
    output='bool',
    inputs=[
        HookInput('Oid', 'fn_oid'),
    ]
)
fmgr_hook_type = HookType(
    name='fmgr_hook_type',
    output='void',
    inputs=[
        HookInput('FmgrHookEventType', 'event'),
        HookInput('FmgrInfo *', 'flinfo'),
        HookInput('Datum *', 'arg'),
    ]
)
object_access_hook_type = HookType(
    name='object_access_hook_type',
    output='void',
    inputs=[
        HookInput('ObjectAccessType', 'access'),
        HookInput('Oid', 'classId'),
        HookInput('Oid', 'objectId'),
        HookInput('int', 'subId'),
        HookInput('void *', 'arg'),
    ]
)
ExplainOneQuery_hook_type = HookType(
    name='ExplainOneQuery_hook_type',
    output='void',
    inputs=[
        HookInput('Query *', 'query'),
        HookInput('int', 'cursorOptions'),
        HookInput('IntoClause *', 'into'),
        HookInput('ExplainState *', 'es'),
        HookInput('const char *', 'queryString'),
        HookInput('ParamListInfo', 'params'),
        HookInput('QueryEnvironment *', 'queryEnv'),
    ]
)
explain_get_index_name_hook_type = HookType(
    name='explain_get_index_name_hook_type',
    output='const char *',
    inputs=[
        HookInput('Oid', 'indexId'),
    ]
)
check_password_hook_type = HookType(
    name='check_password_hook_type',
    output='void',
    inputs=[
        HookInput('const char *', 'username'),
        HookInput('const char *', 'shadow_pass'),
        HookInput('PasswordType', 'password_type'),
        HookInput('Datum', 'validuntil_time'),
        HookInput('bool', 'validuntil_null'),
    ]
)
ExecutorStart_hook_type = HookType(
    name='ExecutorStart_hook_type',
    output='void',
    inputs=[
        HookInput('QueryDesc *', 'queryDesc'),
        HookInput('int', 'eflags'),
    ]
)
ExecutorRun_hook_type = HookType(
    name='ExecutorRun_hook_type',
    output='void',
    inputs=[
        HookInput('QueryDesc *', 'queryDesc'),
        HookInput('ScanDirection', 'direction'),
        HookInput('uint64', 'count'),
        HookInput('bool', 'execute_once'),
    ]
)
ExecutorFinish_hook_type = HookType(
    name='ExecutorFinish_hook_type',
    output='void',
    inputs=[
        HookInput('QueryDesc *', 'queryDesc'),
    ]
)
ExecutorEnd_hook_type = HookType(
    name='ExecutorEnd_hook_type',
    output='void',
    inputs=[
        HookInput('QueryDesc *', 'queryDesc'),
    ]
)
ExecutorCheckPerms_hook_type = HookType(
    name='ExecutorCheckPerms_hook_type',
    output='bool',
    inputs=[
        HookInput('List *', 'rangeTabls'),
        HookInput('bool', 'abort'),
    ]
)
ClientAuthentication_hook_type = HookType(
    name='ClientAuthentication_hook_type',
    output='void',
    inputs=[
        HookInput('Port *', 'port'),
        HookInput('int', 'status'),
    ]
)
join_search_hook_type = HookType(
    name='join_search_hook_type',
    output='RelOptInfo *',
    inputs=[
        HookInput('PlannerInfo *', 'root'),
        HookInput('int', 'levels_needed'),
        HookInput('List *', 'initial_rels'),
    ]
)
get_relation_info_hook_type = HookType(
    name='get_relation_info_hook_type',
    output='void',
    inputs=[
        HookInput('PlannerInfo *', 'root'),
        HookInput('Oid', 'relationObjectId'),
        HookInput('bool', 'inhparent'),
        HookInput('RelOptInfo *', 'rel'),
    ]
)
planner_hook_type = HookType(
    name='planner_hook_type',
    output='PlannedStmt *',
    inputs=[
        HookInput('Query *', 'parse'),
        HookInput('int', 'cursorOptions'),
        HookInput('ParamListInfo', 'boundParams'),
    ]
)
create_upper_paths_hook_type = HookType(
    name='create_upper_paths_hook_type',
    output='void',
    inputs=[
        HookInput('PlannerInfo *', 'root'),
        HookInput('UpperRelationKind', 'stage'),
        HookInput('RelOptInfo *', 'input_rel'),
        HookInput('RelOptInfo *', 'output_rel'),
    ]
)
post_parse_analyze_hook_type = HookType(
    name='post_parse_analyze_hook_type',
    output='void',
    inputs=[
        HookInput('ParseState *', 'pstate'),
        HookInput('Query *', 'query'),
    ]
)
row_security_policy_hook_type = HookType(
    name='row_security_policy_hook_type',
    output='List *',
    inputs=[
        HookInput('CmdType', 'cmdtype'),
        HookInput('Relation', 'relation'),
    ]
)
shmem_startup_hook_type = HookType(
    name='shmem_startup_hook_type',
    output='void',
    inputs=[
    ]
)
ProcessUtility_hook_type = HookType(
    name='ProcessUtility_hook_type',
    output='void',
    inputs=[
        HookInput('PlannedStmt *', 'pstmt'),
        HookInput('const char *', 'queryString'),
        HookInput('ProcessUtilityContext', 'context'),
        HookInput('ParamListInfo', 'params'),
        HookInput('QueryEnvironment *', 'queryEnv'),
        HookInput('DestReceiver *', 'dest'),
        HookInput('char *', 'completionTag'),
    ]
)
emit_log_hook_type = HookType(
    name='emit_log_hook_type',
    output='void',
    inputs=[
        HookInput('ErrorData *', 'edata'),
    ]
)
get_attavgwidth_hook_type = HookType(
    name='get_attavgwidth_hook_type',
    output='int32',
    inputs=[
        HookInput('Oid', 'relid'),
        HookInput('AttrNumber', 'attnum'),
    ]
)
get_relation_stats_hook_type = HookType(
    name='get_relation_stats_hook_type',
    output='bool',
    inputs=[
        HookInput('PlannerInfo *', 'root'),
        HookInput('RangeTblEntry *', 'rte'),
        HookInput('AttrNumber', 'attnum'),
        HookInput('VariableStatData *', 'vardata'),
    ]
)
get_index_stats_hook_type = HookType(
    name='get_index_stats_hook_type',
    output='bool',
    inputs=[
        HookInput('PlannerInfo *', 'root'),
        HookInput('Oid', 'indexOid'),
        HookInput('AttrNumber', 'indexattnum'),
        HookInput('VariableStatData *', 'vardata'),
    ]
)
func_hook_type = HookType(
    name='func_hook_type',
    output='void',
    inputs=[
        HookInput('PLpgSQL_execstate *', 'estate'),
        HookInput('PLpgSQL_function *', 'func'),
    ]
)
stmt_hook_type = HookType(
    name='stmt_hook_type',
    output='void',
    inputs=[
        HookInput('PLpgSQL_execstate *', 'estate'),
        HookInput('PLpgSQL_stmt *', 'stmt'),
    ]
)

sections = [
    HookSection(
        'General Hooks',
        'general-hooks',
        '',
        '',
        [
            Hook(
                emit_log_hook_type,
                'emit_log_hook',
                link('src/include/utils/elog.h#L375')
            ),
            Hook(
                shmem_startup_hook_type,
                'shmem_startup_hook',
                link('src/include/storage/ipc.h#L77')
            ),
        ]
    ),
    HookSection(
        'Security Hooks',
        'security-hooks',
        '',
        '',
        [
            Hook(
                check_password_hook_type,
                'check_password_hook',
                link('src/include/commands/user.h#L25')
            ),
            Hook(
                ClientAuthentication_hook_type,
                'ClientAuthentication_hook',
                link('src/include/libpq/auth.h#L27')
            ),
            Hook(
                ExecutorCheckPerms_hook_type,
                'ExecutorCheckPerms_hook',
                link('src/include/executor/executor.h#L90')
            ),
            Hook(
                object_access_hook_type,
                'object_access_hook',
                link('src/include/catalog/objectaccess.h#L127')
            ),
            Hook(
                row_security_policy_hook_type,
                'row_security_policy_hook_permissive',
                link('src/include/rewrite/rowsecurity.h#L40')
            ),
            Hook(
                row_security_policy_hook_type,
                'row_security_policy_hook_restrictive',
                link('src/include/rewrite/rowsecurity.h#L42')
            ),
        ]
    ),
    HookSection(
        'Function Manager Hooks',
        'function-manager-hooks',
        '',
        '',
        [
            Hook(
                needs_fmgr_hook_type,
                'needs_fmgr_hook',
                link('src/include/fmgr.h#L727')
            ),
            Hook(
                fmgr_hook_type,
                'fmgr_hook',
                link('src/include/fmgr.h#L728')
            ),
        ]
    ),
    HookSection(
        'Planner Hooks',
        'planner-hooks',
        '',
        '',
        [
            Hook(
                explain_get_index_name_hook_type,
                'explain_get_index_name_hook',
                link('src/include/commands/explain.h#L62')
            ),
            Hook(
                ExplainOneQuery_hook_type,
                'ExplainOneQuery_hook',
                link('src/include/commands/explain.h#L58')
            ),
            Hook(
                get_attavgwidth_hook_type,
                'get_attavgwidth_hook',
                link('src/include/utils/lsyscache.h#L62')
            ),
            Hook(
                get_index_stats_hook_type,
                'get_index_stats_hook',
                link('src/include/utils/selfuncs.h#L151')
            ),
            Hook(
                get_relation_info_hook_type,
                'get_relation_info_hook',
                link('src/include/optimizer/plancat.h#L25')
            ),
            Hook(
                get_relation_stats_hook_type,
                'get_relation_stats_hook',
                link('src/include/utils/selfuncs.h#L146')
            ),
            Hook(
                planner_hook_type,
                'planner_hook',
                link('src/include/optimizer/planner.h#L25')
            ),
            Hook(
                join_search_hook_type,
                'join_search_hook',
                link('src/include/optimizer/paths.h#L48')
            ),
            Hook(  # TODO: does it really belong to this section?
                set_rel_pathlist_hook_type,
                'set_rel_pathlist_hook',
                link('src/include/optimizer/paths.h#L33')
            ),
            Hook(  # TODO: does it really belong to this section?
                set_join_pathlist_hook_type,
                'set_join_pathlist_hook',
                link('src/include/optimizer/paths.h#L42')
            ),
            Hook(  # TODO: does it really belong to this section?
                create_upper_paths_hook_type,
                'create_upper_paths_hook',
                link('src/include/optimizer/planner.h#L32')
            ),
            Hook(  # TODO: does it really belongs to this section
                post_parse_analyze_hook_type,
                'post_parse_analyze_hook',
                link('src/include/parser/analyze.h#L22')
            ),
        ]
    ),
    HookSection(
        'Executor Hooks',
        'executor-hooks',
        '',
        '',
        [
            Hook(
                ExecutorStart_hook_type,
                'ExecutorStart_hook',
                link('src/include/executor/executor.h#L71')
            ),
            Hook(
                ExecutorRun_hook_type,
                'ExecutorRun_hook',
                link('src/include/executor/executor.h#L78')
            ),
            Hook(
                ExecutorFinish_hook_type,
                'ExecutorFinish_hook',
                link('src/include/executor/executor.h#L82')
            ),
            Hook(
                ExecutorEnd_hook_type,
                'ExecutorEnd_hook',
                link('src/include/executor/executor.h#L86')
            ),
            Hook(
                ProcessUtility_hook_type,
                'ProcessUtility_hook',
                link('src/include/tcop/utility.h#L32')
            ),
        ]
    ),
    HookSection(
        'PL/pgsql Hooks',
        'plpgsql-hooks',
        '',
        '',
        [
            Hook(
                func_hook_type,
                'func_setup',
                link('src/pl/plpgsql/src/plpgsql.h#L1071')
            ),
            Hook(
                func_hook_type,
                'func_beg',
                link('src/pl/plpgsql/src/plpgsql.h#L1072')
            ),
            Hook(
                func_hook_type,
                'func_end',
                link('src/pl/plpgsql/src/plpgsql.h#L1073')
            ),
            Hook(
                stmt_hook_type,
                'stmt_beg',
                link('src/pl/plpgsql/src/plpgsql.h#L1074')
            ),
            Hook(
                stmt_hook_type,
                'stmt_end',
                link('src/pl/plpgsql/src/plpgsql.h#L1075')
            ),
        ]
    ),
]


def make_short_description(hook):
    path = 'templates/hooks/' + hook.name + '.md'

    if not os.path.exists(path):
        return ''

    with open(path, encoding='utf-8') as hook_text:
        for line in hook_text:
            line = line.strip()
            if line:
                return line[0].lower() + line[1:]


def move_before_generation(output_path):
    if not os.path.exists(output_path):
        return

    path, ext = os.path.splitext(output_path)

    i = 1
    while os.path.exists(path + '.old.' + str(i) + ext):
        i += 1

    os.rename(output_path, path + '.old.' + str(i) + ext)


def write_template(template_path, output_path, **context):
    with open(template_path, encoding='utf-8') as template_text:
        environment = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
        environment.globals['make_short_description'] = make_short_description
        template = environment.from_string(template_text.read())
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template.render(**context))


def main():
    for section in sections:
        for hook in section.hooks:
            path = 'templates/hooks/' + hook.name + '.md'
            if os.path.exists(path):
                continue
            write_template('templates/Hook.md', path, hook=hook)

    move_before_generation('Readme.md')
    write_template('templates/Readme.md', 'Readme.md', sections=sections)

    move_before_generation('Detailed.md')
    write_template('templates/Detailed.md', 'Detailed.md', sections=sections)


if __name__ == '__main__':
    main()
