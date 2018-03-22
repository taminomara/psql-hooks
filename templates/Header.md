Unofficial documentation for PostgreSQL hooks.

> *Denial of responsibility:*
> 
> This work is not a part of the official PostgreSQL documentation.
> 
> Contents of this repository were compiled by Begishev Nikita and
> Goncharov Vladimir, neither of whom appear to be a developer or a maintainer
> of the PostgreSQL Database Management System.
>
> Use this documentation at your own risk.
>
> 
> *Copyright notice:*
> 
> This work combines some research made to this repo by all contributors with
> information acquired from the postgres source code, comments and
> documentation. Some contents of this work were copied from source code
> comments as is, others were written from scratch.
> 
> In no way we (Begishev Nikita and Goncharov Vladimir) claim copyright on texts
> that were copied or adapted from the sources described above.
>
> This work is distributed under the terms of the PostgreSQL License, a copy of
> which may be found in the file called 'License.md'.

PostgreSQL hooks are a simple way to extend functionality of the database.
They allow extensions to introspect database state, react to events and
interfere with database operations.

In terms of the programming language, each hook is a pointer to a function
of a specific type, initially set to be `NULL`.

Upon init, database extensions are free to overwrite those function pointers
with their own values. A previous value of the overwritten pointer is usually
stored withing the extension local memory.

During its work, postgres checks whether certain function pointers are not null
and if that's the case, calls them.

See the [detailed description](Detailed.md) for an explanation on
how to implement a hook and an example.
