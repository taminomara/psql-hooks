Hook for adding additional security checks on the per-relation level.

Given a relations list, this hook should return `true` if access is granted.
`false`, if access is not granted and `abort` is `false`. If `abort` is `true`
and access is not granted, it should throw an appropriate error.

This hook is not called if the standard permission check procedure denies
access to relation. Therefore, there is no way to actually
raise user privileges.

Theoretically, only plain-relation RTEs need to be checked in this hook.
Function RTEs are checked during the function preparation procedure.
Join, subquery, and special RTEs need no checks.

*Inputs:*

* <i>List *</i> <b>rangeTabls</b> — list of `RangeTblEntry` objects that needs
  checking.
* <i>bool</i> <b>abort</b> — it `true`, raise `aclcheck_error` instead of
  returning `false` from the hook.

*Output:*

`true` if user have privileges to access given relations, `false` or raise an
error otherwise, depending on the `abort` flag.
