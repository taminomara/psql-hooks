Hook to monitor accesses to objects.

Object access hooks are called just before or just after performing certain
actions on an SQL object. This is intended as infrastructure for security
or logging extensions.

There are several types of actions defined in `ObjectAccessType`:

`OAT_POST_CREATE`: hook is invoked just after the object is created.
Typically, this is done after inserting the primary catalog records and
associated dependencies.

`OAT_DROP`: hook is invoked just before deletion of objects.

`OAT_POST_ALTER`: hook is invoked just after the object is altered,
but before the command counter is incremented. An extension using the
hook can use a current MVCC snapshot to get the old version of the tuple,
and can use `SnapshotSelf` to get the new version of the tuple.

`OAT_NAMESPACE_SEARCH`: hook is invoked prior to object name lookup under
a particular namespace. This event is equivalent to usage permission
on a schema under the default access control mechanism.

`OAT_FUNCTION_EXECUTE`: hook is invoked prior to function execution.
This event is almost equivalent to execute permission on functions,
except for the case when execute permission is checked during object
creation or altering, because `OAT_POST_CREATE` or `OAT_POST_ALTER` are
sufficient for extensions to track these kind of checks.

Other types may be added in the future.

*Inputs:*

For different access types, inputs of this hook mean different things.

* <i>ObjectAccessType</i> <b>access</b> — access type.
* <i>Oid</i> <b>classId</b> — id of a relation which contains this object.
  You can determine type of an object by this parameter.
* <i>Oid</i> <b>objectId</b> — object that is being accessed.
* <i>int</i> <b>subId</b> — subitem within object (e.g. column), or 0.
* <i>void *</i> <b>arg</b> — access type specific argument.

For `OAT_POST_CREATE`, `arg` is a pointer to `ObjectAccessPostCreate`
structure, which contain a single field, namely `is_internal`. This field
describes whether the context of this creation is invoked by user's
operations, or not. As for `subId`, I've counted two cases when it's non-zero.
The first is when creating a column, and the second one is when creating
a default expression on a column. In either case, `subId` is
an `AttrNumber` of a column.

For `OAT_DROP` type, `arg` is a pointer to `ObjectAccessPostCreate` structure.
It contains a single field called `dropflags`. They inform extensions the
context of this deletion.

For `OAT_POST_ALTER` type, `arg` is a pointer to `ObjectAccessPostAlter`
structure. It contains an `is_internal` flag (see `OAT_POST_CREATE`) and an
`auxiliary_id`. The latter is used when system catalog takes two IDs to
identify a particular tuple of the catalog. It is only used when the caller want
to identify an entry of pg_inherits, pg_db_role_setting or pg_user_mapping.
Elsewhere, InvalidOid is be set.

For `OAT_NAMESPACE_SEARCH` type, `subId` is unused, `classId` is always
`NamespaceRelationId`, and `arg` is a pointer to `ObjectAccessNamespaceSearch`.

`ObjectAccessNamespaceSearch` structure contain two fields. The first one,
`ereport_on_violation`, indicates that the hook should raise an error when
permission to search this schema is denied. The second one, `result`, is in fact
an out parameter. Core code should initialize this to true, and any extension
that wants to deny access should reset it to false. But an extension should be
careful never to store a true value here, so that in case there are multiple
extensions access is only allowed if all extensions agree.

For `OAT_FUNCTION_EXECUTE` type, `subId` and `arg` are unused, and
`classId` is always `ProcedureRelationId`.
