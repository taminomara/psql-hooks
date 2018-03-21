Hook to add policies which are enforced, regardless of other policies.

See `row_security_policy_hook_permissive` for a detailed description.

Unlike for permissive policies, postgres guarantees that restrictive policies
will be executed in a predefined order. That is, first postgres executes the
default policies sorted by their name, than postgres executes custom policies,
also sorted by their name.
