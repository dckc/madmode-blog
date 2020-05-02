title: re-discovering dotfiles
date: 2006-03-18
tags: []
published: true

<b>re-discovering dotfiles</b>

<p> <p> I thought I understood how .profile, .bashrc, .login worked, but it has evidently faded from memory. After years of relying on sensible defaults in debian etc., I'm using mercurial/hg for <a href="http://del.icio.us/connolly/scm">source code management</a>. A big advantage of mercurial is that it does <em>not</em> need to be centrally managed; I can install it in ~/bin. But then I want to use it across an ssh connection, so $PATH has to get setup somehow. I've got that working, using .bashrc.

<p> <p> But I have to manually <tt>. ~/.bashrc</tt> before I can use mercurial in interactive logins. That's tolerable, but I have to remember to do it <em>before</em> I start up emacs, or else I get the dreaded:

<p> <p> <pre>
Traceback (most recent call last):
  File "/Users/connolly/bin/hg", line 10, in ?
    from mercurial import commands
ImportError: No module named mercurial
</pre>

<p> <p> when I try to use hg/emacs integration. I rely heavily on emacs/cvs integration, and working this out will be critical to moving to hg, for me.

<p> <b>update:</b> Well, I got it working by symlinking .bash_profile to .bashrc; I would have thought I could do it within POSIX-standard facilities, but I can't see how. I guess I can rely on bash being on all the machines I use.