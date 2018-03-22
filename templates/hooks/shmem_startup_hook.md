Hook for extensions to initialize their shared memory.

This hook is called by postmaster or by a standalone backend
right after postgres initializes its shared memory and semaphores
so that extensions have chance to initialize their shared state.

It also may be called by a backend forked from the postmaster.
In this situation, the shared memory segment already exists, so you only have
to initialize the local memory state (check `!IsUnderPostmaster`
to determine if that's the case).

Note that you can bind a callback for shared state teardown
via `on_shmem_exit`.

Check out the `pg_stat_statements` code to get the idea on how to implement
this hook correctly.
