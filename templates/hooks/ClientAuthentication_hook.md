Hook for controlling the authentication process.

Called after finishing user authentication (regardless of whether authentication
succeed or not).

This hook will be called for every connection that passed authentication.
However, it is not guaranteed to be called if there are issues with the
connection itself. For example, SSL verification failure or pg_hba.conf
check failure will close the connection without calling this hook.

*Inputs:*

* <i>Port *</i> <b>port</b> — full info about the connection and
  the connected user.
* <i>int</i> <b>status</b> — a standard status code. `STATUS_OK` (`0`)
  if authentication successful.
