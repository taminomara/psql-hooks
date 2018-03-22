Called at the end of the process of joinrel modification to contain the best paths.

The hook can manipulate path list to perform a postprocess for best paths.

*Inputs:*

* <i>PlannerInfo *</i> <b>root</b> — query plan root.
* <i>RelOptInfo *</i> <b>joinrel</b> — list of paths.
* <i>RelOptInfo *</i> <b>outerrel</b> - list of outer relation paths.
* <i>RelOptInfo *</i> <b>innerrel</b> - list of inner relation paths.
* <i>JoinType</i> <b>jointype</b> - the type of a join.
* <i>JoinPathExtraData *</i> <b>extra</b>
