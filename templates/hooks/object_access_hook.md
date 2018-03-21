Multi-pass hook to monitor accesses to objects.

Can be triggered by the following entrypoints:\
[RunFunctionExecuteHook()](https://doxygen.postgresql.org/objectaccess_8c.html#a41ee35a449248c380c9a8fb0529bd4af)\
[RunNamespaceSearchHook()](https://doxygen.postgresql.org/objectaccess_8c.html#a6e3676b4278836b87b28148eb9d666fc)\
[RunObjectDropHook()](https://doxygen.postgresql.org/objectaccess_8c.html#a1b20ed6ac04157d8453802a07254ca90)\
[RunObjectPostAlterHook()](https://doxygen.postgresql.org/objectaccess_8c.html#a3250abdee32af9fcb65c2a5fc1a1b496)\
[RunObjectPostCreateHook()](https://doxygen.postgresql.org/objectaccess_8c.html#acba44450c8b47e3fe01ff1df9eb1e409)

*Inputs:*

* <i>ObjectAccessType</i> <b>access</b> — access event type ([ref](https://doxygen.postgresql.org/objectaccess_8h.html#a9b9ef77e618c4d2025e0413a6fe214a0))
* <i>Oid</i> <b>classId</b>
* <i>Oid</i> <b>objectId</b>
* <i>int</i> <b>subId</b>
* <i>void *</i> <b>arg</b> — entrypoint-specific argument (optional)

*Output:*

Hook should not produce any output.

*Use-cases:*

Useful for security and logging extensions.
