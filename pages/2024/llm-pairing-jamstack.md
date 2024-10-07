---
title: rebuilding madmode on 11ty using aider
summary: pair programming with an LLM to get over blogging analysis paralysis
published: true
date: 2024-09-28
tags:
  - generative-ai
  - jamstack
  - llm
  - pair-programming
  - collaboration
  - productivity
---

[Generative AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence) can
definitely be a productivity booster... "I'm kinda scared of my python site builder now,"
I wrote way back in 2016. I've been sort of stuck since then.

Then I learned about [aider](https://aider.chat/), "pair programming in your terminal".
It took just 2 and 1/2 hrs to re-created the features of my blog with modern JavaScript tooling.

<img src="https://github.com/user-attachments/assets/82f6fedb-5b3d-4053-b657-156b8b2668ef" alt="MadMode blog screenshot" width="600" />

After setting up billing, we start start it with `aider --sonnet`.
Then literally type **Create an 11ty blog called MadMode with the subtitle "Dan Connolly's hacking notebook"**.
And whoosh:

<a href="https://asciinema.org/a/678026?t=60" target="_blank"><img src="https://asciinema.org/a/678026.svg" /></a>

Not only that, but `aider` makes a git commit out of what it did. No more copying and pasting code
between the LLM chat window and your text editor.

 - 2024-09-21 11:53 850441f feat: Create an 11ty blog called MadMode with the subtitle "Dan Connolly's hacking notebook"

Its first try had a bug. So I typed **fix it**. And it did.

 - 2024-09-21 11:54 7fc1488 fix: resolve template render error in layout.njk

`aider` offers to run the command to start the site in dev mode, and I agreed. The initial site looks like this:

![Screenshot at 2024-09-28 02-56-10](https://github.com/user-attachments/assets/c68799f3-0997-4b47-8743-b54ddf808659)

Retrofitting the file structure to my existing content is something that usually trips me up
when trying to migrate to a different blog engine. It was pretty much automatic with these tools:

 - 2024-09-21 11:57 44d680e feat: move the source of the posts to pages/YYYY

It borked the footer code now and then. I was about to give up in frustration, but
since **fix it** generally works, I just moved on without worrying about it too much.

 - 2024-09-21 12:03 d93752d fix: Remove Liquid escaping from copyright footer

Tags took a couple tries:

 - 2024-09-21 12:07 152ff32 feat: Add 'writing' tag to first post
 - 2024-09-21 12:09 804eb5a feat: Add navigation and improve layout

Between those two, I said **I don't see the new "writing" tag. how do tags work in 11ty?**

With an LLM, we don't have to settle for Lorem Ipsum. I
made a **make up a dozen posts going back several years** wish, and lo...

 - 2024-09-21 12:12 591e119 feat: Add a dozen new blog posts and update index page with archives

Next wish: **under Recent Posts, each item should include the post summary. if the post has no explicit summary, use the 1st 135 characters**

 - 2024-09-21 12:35 5123baa feat: Add post summary to Recent Posts section

**each post should show the date and tags at the bottom**

 - 2024-09-21 12:39 4a9cf7f feat: add date and tags to post layout

**add a tag index; that is: a list of the tags, each linked to a list of all the posts with that tag**

 - 2024-09-21 12:42 46e57da feat: Add tag index pages

**good. but can you change the url structure from /tags/foo/ to /search/label/foo/ ?**

 - 2024-09-21 12:43 f9dc1d0 feat: Change URL structure from /tags/foo/ to /search/label/foo/

**good! now change the tags index from a list to a tag cloud; that is: tags with more posts are bigger**

 - 2024-09-21 12:45 45afb88 feat: Implement tag cloud in tags index

![image](https://github.com/user-attachments/assets/705b710c-dcd8-4578-8ddd-d6eb6e0c8d9d)

I did a little research to figure out which search library I wanted to use, and then
asked it to **add search using minisearch**:

 - 2024-09-21 13:08 4f8d01b feat: Add search functionality using MiniSearch

Then I started playing around with style:

 - 2024-09-21 13:25 55e0f22 feat: use serif fonts
 - 2024-09-21 13:27 26e7149 feat: Add blockquote styles with italics and large quotation mark
 - 2024-09-21 14:21 6ae305a feat: Add laboratory notebook style to background

And finally:

 - 2024-09-28 03:37 472793c feat: Move the Welcome section to the bottom and rename it to "About MadMode"

move-section-down.cast 
    https://asciinema.org/a/678027

aider wrote 7% of its own code
in the most recent release, it wrote 70% https://github.com/paul-gauthier/aider/releases/tag/v0.57.0

It can definitely make something _good enough to criticize_... not
a finished product, but something that's close enough to go "no, not like that, but..." and now
you have a better sense of what you _do_ want.




