title: Rust-Sqlite3 -- Rustic bindings for sqlite3
date: 2014-08-13
tags: [programming, rust, data, quality, collaboration, capabilities]
published: true

I was looking into [sandstorm][], a personal cloud platform with an
architecture based on the wonderful [capability security][capsec]
paradigm, and I found a rust application, [acronymy][], that uses the
native API rather than the traditional POSIX environment.

[sandstorm]: https://sandstorm.io/
[capsec]: http://www.erights.org/elib/capability/ode/ode-capabilities.html
[acronymy]: https://github.com/dwrensha/acronymy

I started poring over the code and followed the dependency link to
linuxfood's [rustsqlite][]. I started working on a [memory safety
issue][92] etc. but soon found a number of large-scale API design
issues that I wasn't sure how to approach with the upstream
developers. I was also inspired by `FromSql`, `ToSql` and such
from sfackler's [rust-postgres] API.

So I started from scratch, using [bindgen][], `Result` (sum types) etc.

[rustsqlite]: https://github.com/linuxfood/rustsqlite
[92]: https://github.com/linuxfood/rustsqlite/issues/92
[rust-postgres]: https://github.com/sfackler/rust-postgres
[bindgen]: https://github.com/crabtw/rust-bindgen

Thanks to **apoelstra** and others in the [rust community][rust] IRC
channel, I'm making pretty good progress.  The API isn't stable yet;
testing continues to turn up issues at a pretty high rate. But it's
getting there.

[rust]: http://www.rust-lang.org/

Open source collaboration and QA tools are great these days. Not only do
we have [rust-sqlite3 on github][vcs], but every time I push there:

  - [rust-sqlite3 on travis-ci][ci] runs all the tests and builds the
    docs an pushes them to
  - [rust-sqlite3 on rust-ci][docs], where docs are published.

[vcs]: https://github.com/dckc/rust-sqlite3
[ci]: http://www.rust-ci.org/dckc/rust-sqlite3
[docs]: http://www.rust-ci.org/dckc/rust-sqlite3/doc/sqlite3/
