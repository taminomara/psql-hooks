Hook for altering index names in explain statements.

Extensions may override the default name generation mechanism
so that plans involving hypothetical indexes can be explained.

*Inputs:*

* <i>Oid</i> <b>indexId</b> — index id.

*Output:*

Name of the index or `NULL`. In the later case, a default name
will be generated.
