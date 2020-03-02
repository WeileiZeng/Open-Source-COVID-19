---
title: Heroes
---
We try to list all people who contributed to the open source community during COVID-19. This page is under development.

search "COVID" on GitHub, one can see {{ site.data.github_search_COVID.total_count }} repos. The first 30 are

{% for repo in site.data.github_search_COVID.items %}
* ![](https://img.shields.io/github/stars/{{ repo.full_name }}?color=yellow&label=%E2%AD%90%EF%B8%8F&logo\
Color=blue&style=plastic) [{{ repo.full_name }}](https://github.com/{{ repo.full_name }}) {% endfor %}


search "nCoV" on GitHub, one can see {{ site.data.github_search_nCoV.total_count }} repos. The first 30 are

{% for repo in site.data.github_search_nCoV.items %}
* ![](https://img.shields.io/github/stars/{{ repo.full_name }}?color=yellow&label=%E2%AD%90%EF%B8%8F&logo\
Color=blue&style=plastic) [{{ repo.full_name }}](https://github.com/{{ repo.full_name }}) {% endfor %}



<!-- * {{ repo.full_name }} {{ repo.stargazers_count }} -->



<!-- 
{% for hero in site.data.heroes %}
* [{{ hero.name }}](hero.home_page)
{% for repo in hero.repos %}
  * {{ repo.repo_name }} {% endfor %}
{% for project in hero.projects %}
  * {{ project.project_name }} {% endfor %}
{% endfor %}
-->


<!-- { % include page_summary_heroes.md %}  -->

---

{% include footer.md %}