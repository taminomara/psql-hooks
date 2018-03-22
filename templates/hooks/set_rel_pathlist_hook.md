Called at the end of building access paths for a base relation.

The hook can apply changes to set of paths by adding new paths or deleting them. 

*Inputs:*

* <i>PlannerInfo *</i> <b>root</b>
* <i>RelOptInfo *</i> <b>rel</b> - relation info.
* <i>Index</i> <b>rti</b> - range table index.
* <i>RangeTblEntry *</i> <b>rte</b> range table entry.