---
layout: layout.njk
title: Home
---

# Welcome to MadMode

This is Dan Connolly's hacking notebook. Here you'll find my thoughts, experiments, and discoveries in the world of technology and programming.

## Recent Posts

{% for post in collections.posts | reverse %}
1. [{{ post.data.title }}]({{ post.url }}) - {{ post.date | date: "%Y-%m-%d" }}
{% endfor %}
