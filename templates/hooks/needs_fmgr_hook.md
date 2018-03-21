Auxiliary hook which decides whether `fmgr_hook` should be called.

Given a function id, decide whether 

The result of this hook should be combined with the result of a previously
registered `needs_fmgr_hook` via the `OR` clause. This is required to ensure
that other plugins can hook function even though this very plugin does
not hook them. Such behavior is vital for proper work of the security plugins.

*Inputs:*

* <i>Oid</i> <b>fn_oid</b> — id of a function which needs hooking.

*Output:*

Return `true` if you want to hook enter/exit event for this function.
