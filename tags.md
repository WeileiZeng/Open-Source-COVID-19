---
comments: true
---

{% include navigation.md %}

<a name="top" id="top"></a>
{% include page_summary_total.md %}

Here lists all projects classified by tags. A project may appear under multiple tags. Help me to add [more.](https://github.com/WeileiZeng/Open-Source-COVID-19/issues/68)
{% assign tags_sorted = site.data.tags | sort %}{% for tag in tags_sorted %}
<button type="button" style="background-color:#83E583;color=#F392F3" onclick='myFunction("{{ tag | downcase }}")'>{{tag}}</button> {% endfor %}


{% assign projects = site.data.tags_projects %}

{% include tags_projects.md %}

<script>
function myFunction(tag_name) {
  console.log("hello world");
  console.log(tag_name);
  console.log(document.getElementById(tag_name));
  var ele=document.getElementById(tag_name);	
  var position = ele.offsetTop-20;
  //  document.getElementById(tag_name).innerHTML="Hello";
  // var position = document.getElementById(tag_name).offset().top - 190;
  //  var position = 600;
  $("html, body").animate({scrollTop: position}, 400);
}


</script>