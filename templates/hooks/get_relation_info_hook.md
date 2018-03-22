Hook for altering results of the relation info lookup.

This hook allow plugins to editorialize on the info that was obtained from the
catalogs by the default relation info lookup. Actions might include altering
the assumed relation size, removing an index, or adding a hypothetical
index to the `indexlist`.

*Inputs:*

* <i>PlannerInfo *</i> <b>root</b> — current planner info.
* <i>Oid</i> <b>relationObjectId</b> — id of the relation that we are looking
  info for.
* <i>bool</i> <b>inhparent</b> — if true, all we need to do is set up the attr
  arrays: the `RelOptInfo` actually represents the `appendrel` formed by an
  inheritance tree, and so the parent rel's physical size and index information
  isn't important for it.
* <i>RelOptInfo *</i> <b>rel</b> — relation info that can be adjusted.
