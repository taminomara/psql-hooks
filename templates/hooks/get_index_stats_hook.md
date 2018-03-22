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
