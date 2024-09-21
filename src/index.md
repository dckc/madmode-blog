---
layout: layout.njk
title: Home
---

# Welcome to MadMode

This is Dan Connolly's hacking notebook. Here you'll find my thoughts, experiments, and discoveries in the world of technology and programming.

## Recent Posts

{% assign sorted_posts = collections.posts | reverse %}
{% for post in sorted_posts %}
1. [{{ post.data.title }}]({{ post.url }}) - {{ post.date | date: "%Y-%m-%d" }}
   {{ post.templateContent | summary }}
{% endfor %}

## Archives

### 2023
{% for post in sorted_posts %}
{% assign post_year = post.date | date: "%Y" %}
{% if post_year == "2023" %}
- [{{ post.data.title }}]({{ post.url }}) - {{ post.date | date: "%Y-%m-%d" }}
{% endif %}
{% endfor %}

### 2022
{% for post in sorted_posts %}
{% assign post_year = post.date | date: "%Y" %}
{% if post_year == "2022" %}
- [{{ post.data.title }}]({{ post.url }}) - {{ post.date | date: "%Y-%m-%d" }}
{% endif %}
{% endfor %}

### 2021
{% for post in sorted_posts %}
{% assign post_year = post.date | date: "%Y" %}
{% if post_year == "2021" %}
- [{{ post.data.title }}]({{ post.url }}) - {{ post.date | date: "%Y-%m-%d" }}
{% endif %}
{% endfor %}

### 2020
{% for post in sorted_posts %}
{% assign post_year = post.date | date: "%Y" %}
{% if post_year == "2020" %}
- [{{ post.data.title }}]({{ post.url }}) - {{ post.date | date: "%Y-%m-%d" }}
{% endif %}
{% endfor %}
