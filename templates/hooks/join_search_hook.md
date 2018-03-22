Called when optimiser chooses order for join relations.

When the hook is set, replaces GEQO or standard join search. 

*Inputs:*

* <i>PlannerInfo *</i> <b>root</b> — query plan root.
* <i>int</i> <b>levels_needed</b> — the number of child joinlist nodes.
* <i>List *</i> <b>initial_rels</b> — list of join relations.