10,000+ people have contributed to the projects in this list, which have received 10,000+ stars.


{% for group in site.data.wuhan %}
### {{ group.group_name }}
{% for repo in group.repos %}
* {% if repo.repo_name %} ![](https://img.shields.io/github/stars/{{ repo.repo_name }}?color=yellow&label=%E2%AD%90%EF%B8%8F&logoColor=blue&style=plastic) [{{ repo.repo_name }}](https://github.com/{{ repo.repo_name }}) {% endif %} {% if repo.repo2_name %} ![](https://img.shields.io/github/stars/{{ repo.repo2_name }}?color=yellow&label=%E2%AD%90%EF%B8%8F&logoColor=blue&style=plastic) [{{ repo.repo2_name }}](https://github.com/{{ repo.repo2_name }}) {% endif %} {% if repo.web_name %}[{{ repo.web_name }}]({{ repo.web_url }}){% endif %} {% if repo.web2_name %}[{{ repo.web2_name }}]({{ repo.web2_url }}){% endif %} {{ repo.content }} {% endfor %}
{% endfor %}




### 推荐网页 Site recommendation
[武汉开源OpenSourceWuhan](https://weileizeng.github.io/OpenSourceWuhan/)
集结了支援武汉的开源项目，是一个连结各个开源项目的入口。本站持续跟新中。
* 给本站推荐项目请点这里 [Open issue at GitHub](https://github.com/WeileiZeng/OpenSourceWuhan/issues/new?assignees=&labels=&template=------.md&title=%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%E6%8E%A8%E8%8D%90%3A+%E9%A1%B9%E7%9B%AE%E5%90%8D%E7%A7%B0)
* 也可评论或者[Contact me](https://weileizeng.com/news/1992/06/29/contact/)

