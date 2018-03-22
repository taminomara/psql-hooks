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
