---
title: World
comments: true
---
As nCoV/COVID-19 spreads over the world, so as the support from open source community. Here lists the projects supporting different areas all over the world.
See also [projects for Wuhan, China](index)



{% for country in site.data.world %}
## {{ country.country }}
{% for repo in country.repos %}
* {% if repo.repo_name %} ![](https://img.shields.io/github/stars/{{ repo.repo_name }}?color=yellow&label=%E2%AD%90%EF%B8%8F&logoColor=blue&style=plastic) [{{ repo.repo_name }}](https://github.com/{{ repo.repo_name }}) {% endif %} {% if repo.repo2_name %} ![](https://img.shields.io/github/stars/{{ repo.repo2_name }}?color=yellow&label=%E2%AD%90%EF%B8%8F&logoColor=blue&style=plastic) [{{ repo.repo2_name }}](https://github.com/{{ repo.repo2_name }}) {% endif %} {% if repo.web_name %}[{{ repo.web_name }}]({{ repo.web_url }}){% endif %} {% if repo.web2_name %}[{{ repo.web2_name }}]({{ repo.web2_url }}){% endif %} {{ repo.content }} {% endfor %}
{% endfor %}




### Site recommendation
[Open Source COVID-19](https://weileizeng.github.io/Open-Source-COVID-19/) collects all open source sites related to  nCoV/COVID-19. It is hosted on [GitHub](https://github.com/WeileiZeng/Open-Source-COVID-19). You are welcome to recommend a site by
* [openning issue at GitHub](https://github.com/WeileiZeng/Open-Source-COVID-19/issues/)
* or [contact me](https://weileizeng.com/news/1992/06/29/contact/)


<!--
<div id="fb-root"></div>
<script async defer crossorigin="anonymous" src="https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v6.0"></script>

<div class="fb-comments" data-href="https://weileizeng.github.io/OpenSourceWuhan/" data-width="100%" data-numposts="1"></div>

-->



{% include page_summary_world.md %}

{% include footer.md %}