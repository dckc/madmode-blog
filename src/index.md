---
layout: layout.njk
title: Home
---

# Welcome to MadMode

This is Dan Connolly's hacking notebook. Here you'll find my thoughts, experiments, and discoveries in the world of technology and programming.

## Recent Posts

{% for post in collections.posts | reverse %}
1. [{{ post.data.title }}]({{ post.url }}) - {{ post.date | date: "yyyy-MM-dd" }}
{% endfor %}

## Archives

### 2023
{% for post in collections.posts | reverse %}
{% if post.date.getFullYear() == 2023 %}
- [{{ post.data.title }}]({{ post.url }}) - {{ post.date | date: "yyyy-MM-dd" }}
{% endif %}
{% endfor %}

### 2022
{% for post in collections.posts | reverse %}
{% if post.date.getFullYear() == 2022 %}
- [{{ post.data.title }}]({{ post.url }}) - {{ post.date | date("yyyy-MM-dd") }}
{% endif %}
{% endfor %}

### 2021
{% for post in collections.posts | reverse %}
{% if post.date.getFullYear() == 2021 %}
- [{{ post.data.title }}]({{ post.url }}) - {{ post.date | date("yyyy-MM-dd") }}
{% endif %}
{% endfor %}

### 2020
{% for post in collections.posts | reverse %}
{% if post.date.getFullYear() == 2020 %}
- [{{ post.data.title }}]({{ post.url }}) - {{ post.date | date("yyyy-MM-dd") }}
{% endif %}
{% endfor %}
