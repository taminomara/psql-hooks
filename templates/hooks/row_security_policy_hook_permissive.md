Hook to add policies which are combined with the other permissive policies, using OR.

This hook, along with the `row_security_policy_hook_restrictive`, allows adding
custom security policies. It is called to build a list of policies for the given
command applied to the given relation.

*Inputs:*

* <i>CmdType</i> <b>cmdtype</b> — command type.
* <i>Relation</i> <b>relation</b> — relation id.

*Output:*

List of additional permissive policies that will be added to the list of
default permissive policies.
