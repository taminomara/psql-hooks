Hook for enforcing password constraints and performing action on password change.

This hook is called whenever a new role is created via the `CREATE ROLE`
statement or a password for an existing role is changed via the `ALTER ROLE`
statement. Given a shadow password and some additional info, this hook can
raise an error using the standard `ereport` mechanism if the password
isn't strong enough.

*Inputs:*

* <i>const char *</i> <b>username</b> — name of the created/altered role.
* <i>const char *</i> <b>shadow_pass</b> — a shadow pass, i.e. a plain password
  or a password hash.
* <i>PasswordType</i> <b>password_type</b> — type of the password.
  `PASSWORD_TYPE_MD5` for an md5-encrypted password,
  `PASSWORD_TYPE_SCRAM_SHA_256` for a sha-256-encrypted password,
  `PASSWORD_TYPE_PLAINTEXT` for a plaintext password.
* <i>Datum</i> <b>validuntil_time</b> — date upon which this password expires.
* <i>bool</i> <b>validuntil_null</b> — a flag that is true if and only if
  the `validuntil_time` parameter is not set (i.e. a null date is passed).
