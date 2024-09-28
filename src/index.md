---
layout: layout.njk
title: Home
---

## Recent Posts

{% assign sorted_posts = collections.posts | reverse %}
{% for post in sorted_posts %}
1. [{{ post.data.title }}]({{ post.url }}) - {{ post.date | date: "%Y-%m-%d" }}
   
   Tags: {% for tag in post.data.tags %}{% if tag != "posts" %}{{ tag }}{% if not loop.last %}, {% endif %}{% endif %}{% endfor %}
   
   {{ post.templateContent | summary }}
{% endfor %}

## [View All Archives](/archives/)

## About MadMode

This is Dan Connolly's hacking notebook. Here you'll find my thoughts, experiments, and discoveries in the world of technology and programming.
