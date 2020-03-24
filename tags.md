---
comments: true
---

{% include navigation.md %}

<a name="top"></a>
{% include page_summary_total.md %}


All tags: {% for tag in site.data.tags %}
<button type="button" class="btn" style="background-color:#83E583;color=#F392F3">[{{tag}}](#{{tag | downcase}})</button> {% endfor %}


{% assign projects = site.data.tags_projects %}

{% include tags_projects.md %}

