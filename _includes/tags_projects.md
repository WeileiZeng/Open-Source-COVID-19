
{% assign projects_sorted = projects | sort: "group_name" %}
{% for group in projects_sorted %}
## {{ group.group_name }}
{% for repo in group.repos %}
* {% if repo.repo_name %} {{ repo.repo_name }} <object alt="github" data="assets/shields/{{ repo.repo_name | split: '/' | join: '-' }}.svg" type="image/svg+xml" align="top"></object> {% endif %} {% if repo.repo2_name %} {{ repo.repo2_name }} <object alt="github" data="assets/shields/{{ repo.repo2_name | split: '/' | join: '-' }}.svg" type="image/svg+xml" align="top"></object> {% endif %} {% if repo.web_name %}<a href="{{ repo.web_url }}" target="blank">{{ repo.web_name }}</a>{% endif %} {% if repo.web2_name %}<a href="{{ repo.web2_url }}" target="blank">{{ repo.web2_name }}</a>{% endif %} {{ repo.content }} {% for tag in repo.tags %} <em style="color:#D0CE3B"> {{ tag }}</em> {% endfor %} {% endfor %}
<button type="button" class="hvr-radial-out" style="background-color:#83E583;color=#F392F3" onclick='myFunction("top")'>back to top</button>
{% endfor %}


