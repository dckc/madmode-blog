title: "Installing a web IDE for postgress: three hours of woe"
published: true
date: 2015-04-05
tags: [data, quality, sysadmin]
summary: I want to like postgres over mysql, but this experience was dreadful.

<blockquote class="twitter-tweet" lang="en"> <p>finally! after 3
hours, got phpPgAdmin working. I want to like postgres over mysql, but
the initial experience is dreadful.</p>&mdash; Dan Connolly (@dckc) <a
href="https://twitter.com/dckc/status/584229649535737856">April 4,
2015</a></blockquote>
		
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" lang="en"><p><a
href="https://twitter.com/dckc">@dckc</a> I (and some others in the
community) would be interested in a more detailed writeup if you were
willing.</p>&mdash; Robert Treat (@robtreat2) <a
href="https://twitter.com/robtreat2/status/584523279056162816">April
5, 2015</a></blockquote>

<!-- hide the 1st tweet if js is turned on? -->

OK, I'm willing.

My goal that evening was: give peers in a multi-site research project
a web-based IDE to access to a postgres database underneath a jboss app
running on CentOS on AWS.

We've been using ssh tunnels and public keys, but creating those
accounts, not to mention using them, is tedious. We'd like to delegate
account provisioning to Jenkins, but we don't give jenkins blanket
root access. I realized that something like phpMyAdmin would obviate
the need for unix accounts altogether.

Is there such a thing for postgres?  yes: [phpPgAdmin][]

[phpPgAdmin]: http://phppgadmin.sourceforge.net/doku.php

I downloaded it and checked the [INSTALL][] doc:

> 1. Unpack your download ...
> 2. Configure phpPgAdmin - edit phpPgAdmin/conf/config.inc.php ...
> 3. Ensure the statistics collector is enabled in
>    PostgreSQL. phpPgAdmin will display table, index performance, and
>    usage statistics if you have enabled the PostgreSQL statistics
>    collector. While this is normally enabled by default, ...
> 4. Browse to the phpPgAdmin installation using a web browser.
> 5. **IMPORTANT - SECURITY**  
>    PostgreSQL by default does not require you to use a password to
>    log in. We STRONGLY recommend that you enable md5 passwords for
>    local connections in your pg_hba.conf, and set a password for
>    the default superuser account.  
>    Due to the large number of phpPgAdmin installations that have
>    not set passwords on local connections, there is now a
>    configuration file option called 'extra_login_security', which
>    is TRUE by default. &#160;While this option is enabled, you
>    will be unable to log in to phpPgAdmin as the 'root',
>    'administrator', 'pgsql' or 'postgres' users and empty
>    passwords will not work.  
>    Once you are certain you have properly secured your database
>    server, you can then disable 'extra_login_security' so that you
>    can log in as your database administrator using the
>    administrator password.

[INSTALL]: https://raw.githubusercontent.com/phppgadmin/phppgadmin/master/INSTALL

I don't know why step 2 is there. The defaults look OK as far as I can
tell, so I'm already not sure I'm doing it right. *If the defaults are
OK in typical cases, move step 2 to an troubleshooting FAQ section
later. Likewise step 3, since (a) the statistics collector is on by
default, and (b) statistics doesn't seem like a critical
"getting started" feature.*

The fact that the security step comes *after*
the service is available on the net threw me. I immediately tried
to figure out what was going on there.

The reference to "your **pg_hba.conf**" was frustrating. I tried to
find it with **locate**. No joy. From `rpm -qa | grep postgres` I
recall the main package is **postgresql91**. But `rpm -ql
postgresql91|grep pg_hba` turns up empty. I get as far as `pg_config
--sysconfdir` says **/etc/sysconfig/pgsql** but nope; empty too.

Some relevant-looking docs were easy enough to find with a quick web
search: [19.1. The pg_hba.conf File][191] says:

> A default pg_hba.conf file is installed when the data directory is
> initialized by initdb.

[191]: http://www.postgresql.org/docs/9.1/static/auth-pg-hba-conf.html
  

Ah&#8230; `initdb`&#8230; that seems familiar. So I pore over notes
from setting up the database, and I find it: in
**/var/lib/pgsql/9.1/data/pg_hba.conf**. A google search for that path
turns up 5,840 results, but it's not there in section 19.1 of the
official documentation, nor do I win if I follow the link to
[18.2. File Locations][182]. **Before you tell me "It is
possible to place the authentication configuration file elsewhere
&#8230;" how about you tell me, in concrete, literal terms,
where it typically is?!?!?!?**

[182]: http://www.postgresql.org/docs/9.1/static/runtime-config-file-locations.html#GUC-HBA-FILE

Now that I found it, I don't understand what exactly I'm supposed to
change. "We STRONGLY recommend that you enable md5 passwords for local
connections in your pg_hba.conf, and set a password for the default
superuser account." But not so strongly as to spell out how to
do it nor cite documentation on how to do it. More on that below.

The current configuration seems fail-safe, though, so I go ahead with
step 4 and try to browse.  Bzzzt:

>  Your PHP installation does not support PostgreSQL. You need to
>  recompile PHP using the `--with-pgsql` configure option.

Then I vaguely remember php's mysql support is packaged separately, so
I got hunting, and surprise!  CentOS actually supports phpPgAdmin
itself:

    $ yum search php | grep -i postgres
    php-pear-MDB2-Driver-pgsql.noarch : PostgreSQL MDB2 driver
    php-pgsql.x86_64 : A PostgreSQL database module for PHP
    phpPgAdmin.noarch : Web-based PostgreSQL administration

So...

    $ sudo yum install phpPgAdmin
    Installed:
    phpPgAdmin.noarch 0:5.1-1.rhel6
    Dependency Installed:
    php-pdo.x86_64 0:5.3.3-40.el6_6                   
    php-pgsql.x86_64 0:5.3.3-40.el6

and try to browse. No joy: some sort of HTTP forbidden error.


`rpm -ql` turns up **/etc/httpd/conf.d/phpPgAdmin.conf**, where we
find "By default this application is only accessible from the local
host." OK, fair enough. I tweak that apache config file and now I see
a phpPgAdmin web page showing one server, PostgreSQL. Hmm. I choose it
and I get username/password prompt. I enter my linux credentials. No
joy. "Login failed".

So I go looking for clues in apache log files (`ssl_error_log`,
`error_log`, `access_log`), linux/CentOS log files
(`/var/log/messages`), and postgres log files
(`/var/lib/pgsql/9.1/data/pg_log/postgresql-Fri.log`). None to be
had. Is the `php.ini` config supressing them? Not as far as I can
tell.

So I begin guessing what the problem is.

Between `phpPgAdmin/conf/config.inc.php` and `pg_hba.conf`, I must
have tried a dozen combinations. In several cases, postgres wouldn't
start at all. In **no case** were there **any relevant diagnostics**
in **any log file** that I could find.  I found logs of SQL syntax errors
from ordinary select statements, but no connection error logs.

That `phpPgAdmin/conf/config.inc.php` file
says:

            // Hostname or IP address for server.  Use '' for UNIX domain socket
            // use 'localhost' for TCP/IP connection on this computer
    $conf['servers'][0]['host']  = '';

but what worked was changing the `auth-method` in **pg_hba.conf** for `host`
127.0.0.1 to `md5`.

Meanwhile, problems setting up passwords undermined my confidence in
setting up md5 authentication.  Stackoverflow discussion or something
suggested the **createuser** utility, but it kept giving me "already
exists" errors. I stumbled across the `-e` flag, which spit out the
`CREATE ROLE &#8230;` SQL; I changed that to `ALTER ROLE &#8230;` and
it worked.

[Section 19.1][191] presents an exhaustive enumeration of the
authentication methods of postgres where I would have appreciated
successive elaboration: start with the simplest, most typical setup,
which seems to be peer. Then have sections in increasing complexity,
where the complexity is motivated by related issues; e.g. "md5 for
local connections," "passwords with SSL," and then LDAP, and then
rocket-science like kerberos and such. In each section, show one
complete worked example ending with an actual SQL query that worked,
even if that worked example doesn't exercise all of the options. The
less typical options can be explained reference style without an
example.

The root of many of the problems I ran into is perhaps not with
postgres itself but the way it's packaged for CentOS, the phpPgAdmin
documentation, or even apache or php logging configuration. But the
community around mysql is such that concretely documented solutions to
these integration issues are, at most, a web search away.
