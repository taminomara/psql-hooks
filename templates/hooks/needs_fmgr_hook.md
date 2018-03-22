Auxiliary hook which decides whether `fmgr_hook` should be applied to a function.

Given a function id, decide whether `fmgr_hook` should be called upon executing
this function.

The result of this hook should be combined with the result of a previously
registered `needs_fmgr_hook` via the `OR` clause. This is required to ensure
that other extensions can hook function even though this very extension does
not hook them. Such behavior is vital for proper work of the security extensions.

Note that hooked functions are not inlined.

*Inputs:*

* <i>Oid</i> <b>fn_oid</b> — id of a function which needs hooking.

*Output:*

Return `true` if you want to hook enter/exit event for this function.
