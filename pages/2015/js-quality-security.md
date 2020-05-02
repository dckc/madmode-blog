title: On Modern JavaScript
published: false
date: 2015-03-25
tags: [javascript, web, programming, security, quality]


@@flycheck-mode, emacs, atom, IntelliJ

@@BE on latent static types... and flowtype

testing atom preview update. quite nice! what was the AaronSw thingy that did this?

> Dynamic languages are popular in large part because programmers can
> keep types latent in the code, with type checking done imperfectly
> (yet often more quickly and expressively) in the programmers’ heads
> and unit tests

https://brendaneich.com/2010/08/static-analysis-ftw/

 * [Java Script Client][1]  
   Stiegler, Marc to [cap-talk]
   Wed May 28 04:51:50 PDT 2014

[1]: http://www.eros-os.org/pipermail/cap-talk/2014-May/016111.html


> So, when the question about secure practices for JavaScript apps in
> the browser first showed up, I thought it was originally a question
> from Dean, so I just sent him a reply. But that was an incorrect
> interpretation, and he urged me to repost my secure practices
> below. So here they are:
>
>  --marcs
>
>So, the way I got this was a little confusing. Dean, you are the
>requestor for this info, correct?
>
> Interestingly, I know of no docs to point you to for javascript
> security in the browser, though surely someone has written one. But
> here are my observations:
>
> The big thing, as alan said, is "use strict".
>
> Use Object.freeze in your object constructors.
>
> I recommend the object pattern of E style function-based object,
> which allows private variables, rather than prototype-based objects,
> which do not, and which allow putting Object.freeze in the
> constructor naturally:
>
>     var makePoint(x,y) {
>        return Object.freeze({
>           getX: function() {return x;}
>           getY: function() {return y;}
>     }
>
>  Use JSLint or JSHint. Some editors have one built in. Use such an editor.
>
>  I have been playing with TypeScript. Not perfect, but I like it. Do
>  not use the 'class' or 'module' keywords they offer, instead, use
>  the object-constructor pattern I described above, and use
>  TypeScript interfaces to declare their signatures.
>
>
> If you are going to load untrusted third party code, trap it with
> Caja or put it in a separate IFrame. There is an attribute on the
> IFrame you should set to actually get isolation.
>
> Given these rules, you have about as much safety as you can get from
> the programming language (unless Haskell is an alternative). Your
> real problem is not the language, it is the
> browser/html/cookies/etcetera.
>
> Use meta referrer never.
>
> Before displaying to the screen, for any data that is not a static
> part of the page, escape the dangerous characters; I have a list,
> and a little function that will do it for you. Or put the text into
> a TextNode. Using Jquery, it is easy to create text nodes.
>
> Never put authority information in a cookie. Put it in the link or
> put it in a hidden field on the page.  On the server side, always
> use prepared queries to access the SQL database.
