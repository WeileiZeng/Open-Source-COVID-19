---
title: Search
---

Search some keywords to see repos which are not includes in my list. Some of them may show up here due to changing of repo name
<br>
Current keywords used: COVID, nCoV, covid19
<br>
Total number of repos: {{ site.data.github_search | size }}. We only show 200 of them here.

| stars | forks | name | description | homepage | easy_copy|
|-|-|-|{% for repo in site.data.github_search limit: 200 %}
| {{ repo.stargazers_count }}  | {{ repo.forks }} | <a href="https://github.com/{{ repo.full_name }}" target="_blank">{{ repo.full_name }}</a> | {{ repo.description }}| {{ repo.homepage }} | - repo_name: {{repo.full_name}}<br>web_url: {{repo.homepage}}<br>content: {{repo.description}} | {% endfor %}