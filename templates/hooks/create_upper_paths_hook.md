Called when postprocess of the path of set operations occurs.

It's a possibility for extensions to contribute path in relation. 

*Inputs:*

* <i>PlannerInfo *</i> <b>root</b> — query plan root.
* <i>UpperRelationKind</i> <b>stage</b>
* <i>RelOptInfo *</i> <b>input_rel</b>
* <i>RelOptInfo *</i> <b>output_rel</b>