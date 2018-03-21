Hook for intercepting messages before they are sent to the server log.

This hook is called just before sending an error message to the server log
and to the client. The purpose of this hook is to invoke an additional
logic and possibly prevent this error message from being added to the
server log.

This hook is useful for implementing custom logging process.

*Inputs:*

* <i>ErrorData *</i> <b>edata</b> — a structure which holds a complete info
  about the error message. Despite `edata` is a non-const pointer, the only
  supported change in the given structure is setting `output_to_server` to
  `false`. That is, any other change, including setting `output_to_server` to
  `true`, considered not supported.

Note: despite any other changes to the edata are not officially supported
(as per comment [on line 1455 of the elog.c][emit_log_hook_1])),
postgres actually checks for both `output_to_server` and `output_to_client`
flags.

[emit_log_hook_1]: https://github.com/postgres/postgres/blob/master/src/backend/utils/error/elog.c#L1456
