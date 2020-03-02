---
title: World
---
As nCoV spreads over the world, so as the support from open source community. Here lists the projects support different areas all over the world.
See also [projects for Wuhan, China](index)



{% for country in site.data.world %}
## {{ country.country }}
{% for repo in country.repos %}
* {% if repo.repo_name %} ![](https://img.shields.io/github/stars/{{ repo.repo_name }}?color=yellow&label=%E2%AD%90%EF%B8%8F&logoColor=blue&style=plastic) [{{ repo.repo_name }}](https://github.com/{{ repo.repo_name }}) {% endif %} {% if repo.repo2_name %} ![](https://img.shields.io/github/stars/{{ repo.repo2_name }}?color=yellow&label=%E2%AD%90%EF%B8%8F&logoColor=blue&style=plastic) [{{ repo.repo2_name }}](https://github.com/{{ repo.repo2_name }}) {% endif %} {% if repo.web_name %}[{{ repo.web_name }}]({{ repo.web_url }}){% endif %} {% if repo.web2_name %}[{{ repo.web2_name }}]({{ repo.web2_url }}){% endif %} {{ repo.content }} {% endfor %}
{% endfor %}




### Site recommendation
[OpenSourceWuhan](https://weileizeng.github.io/OpenSourceWuhan/) collects all open source sites that support Wuhan and other places against nCoV/CoVid. It is hosted on [GitHub](https://github.com/WeileiZeng/OpenSourceWuhan). You are welcome to recommend a site through
* [Open issue at GitHub](https://github.com/WeileiZeng/OpenSourceWuhan/issues/)
* or [Contact me](https://weileizeng.com/news/1992/06/29/contact/)


<!--
<div id="fb-root"></div>
<script async defer crossorigin="anonymous" src="https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v6.0"></script>

<div class="fb-comments" data-href="https://weileizeng.github.io/OpenSourceWuhan/" data-width="100%" data-numposts="1"></div>

-->



{% include page_summary_world.md %}

{% include footer.md %}