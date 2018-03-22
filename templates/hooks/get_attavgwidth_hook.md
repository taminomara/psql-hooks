Hook for controlling an algorithm for predicting the average width of entries in the column.

This hook, if set, should return the average width of entries in the column.
If returned value is greater than `0`, it is returned to the planner.
Otherwise, the default algorithm is invoked.

*Inputs:*

* <i>Oid</i> <b>relid</b> — relation id.
* <i>AttrNumber</i> <b>attnum</b> — column number.

*Output:*

Average width of entries in the given column of the given relation or zero
to fall back to the default algorithm.
