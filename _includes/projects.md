
{% for group in projects %}
## {{ group.group_name }}
{% for repo in group.repos %}
* {% if repo.repo_name %} <a href="https://github.com/{{ repo.repo_name }}" target="blank"><img src="https://img.shields.io/github/stars/{{ repo.repo_name }}?color=yellow&label={{ repo.repo_name }}&logoColor=blue&style=social" align="top"></a>{% endif %} {% if repo.repo2_name %} <a href="https://github.com/{{ repo.repo2_name }}" target="blank"><img src="https://img.shields.io/github/stars/{{ repo.repo2_name }}?color=yellow&label={{ repo.repo2_name }}&logoColor=blue&style=social" align="top"></a> {% endif %} {% if repo.web_name %}<a href="{{ repo.web_url }}" target="blank">{{ repo.web_name }}</a>{% endif %} {% if repo.web2_name %}<a href="{{ repo.web2_url }}" target="blank">{{ repo.web2_name }}</a>{% endif %} {{ repo.content }} {% endfor %}
{% endfor %}


