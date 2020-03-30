
{% assign projects_sorted = projects | sort: "group_name" %}
{% for group in projects_sorted %}
## {{ group.group_name }}
{% for repo in group.repos %}
* {% if repo.repo_name %}{% assign repo_name = repo.repo_name %} {% include github_icon_with_name.md %}{% endif %} {% if repo.repo2_name %}{% assign repo_name = repo.repo2_name %} {% include github_icon_with_name.md %}{% endif %} {% if repo.web_name %}<a href="{{ repo.web_url }}" target="blank">{{ repo.web_name }}</a>{% endif %} {% if repo.web2_name %}<a href="{{ repo.web2_url }}" target="blank">{{ repo.web2_name }}</a>{% endif %} {{ repo.content }} {% for tag in repo.tags %} <em style="color:#C68C10"> {{ tag }}</em> {% endfor %} {% endfor %}
<button  type="button" onclick='myFunction("top")'>back to top</button>
{% endfor %}


