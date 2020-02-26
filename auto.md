10,000+ people have contributed to the projects in this list, which have received 10,000+ stars.


{% for group in site.data.projects %}
### {{ group.group_name }}
{% for repo in group.repos %}
* {% if repo.repo_name %} ![](https://img.shields.io/github/stars/{{ repo.repo_name }}?color=yellow&label=%E2%AD%90%EF%B8%8F&logoColor=blue&style=plastic) [{{ repo.repo_name }}](https://github.com/{{ repo.repo_name }}) {% endif %} {% if repo.repo2_name %} ![](https://img.shields.io/github/stars/{{ repo.repo2_name }}?color=yellow&label=%E2%AD%90%EF%B8%8F&logoColor=blue&style=plastic) [{{ repo.repo2_name }}](https://github.com/{{ repo.repo2_name }}) {% endif %} {% if repo.web_name %}[{{ repo.web_name }}]({{ repo.web_url }}){% endif %} {% if repo.web2_name %}[{{ repo.web2_name }}]({{ repo.web2_url }}){% endif %} {{ repo.content }} {% endfor %}
{% endfor %}




### 综合平台 Integrated platform
{% include repo.md repo-name='wuhan2020/wuhan2020' content=' [新型冠状病毒防疫信息收集平台](https://wh.opensource-service.cn/#/)' %}
{% include repo.md repo-name='wuhan-support/wuhan.support' content='[面向疫区内外民众和医疗机构的多维度信息整合平台](https://feiyan.help)' %}
{% include repo.md content='[全国抗击新冠肺炎防护物资信息交流平台](http://charity.foodblockchain.com.cn/?from=timeline&isappinstalled=0) (未开源)' %}
* [全国抗击新冠肺炎防护物资信息交流平台](http://charity.foodblockchain.com.cn/?from=timeline&isappinstalled=0) (未开源)


###  疫情信息 Data collection and visualization
* ⭐️   317   [shfshanyue/2019-ncov](https://github.com/shfshanyue/2019-ncov)
[全国新型冠状病毒，肺炎疫情实时省市地图](https://ncov.shanyue.tech)
*  ⭐️  677   [BlankerL/DXY-2019-nCoV-Crawler](https://github.com/BlankerL/DXY-2019-nCoV-Crawler) ⭐️   393     [BlankerL/DXY-2019-nCoV-Data](https://github.com/BlankerL/DXY-2019-nCoV-Data) [全国新型肺炎疫情实时数据API接口](https://lab.isaaclin.cn/nCoV/)
* [cuihua/2019_nCov](https://github.com/cuihuan/2019_nCov) [2019-nCov 武汉新型冠状病毒可视化](http://cuihuan.net/wuhan/news.html)

* [肺炎疫情实时动态 · 北美](https://coronavirus.1point3acres.com/?from=timeline&isappinstalled=0) （未开源）
* [sangyx/nCoV-Map](https://github.com/sangyx/nCoV-Map) [nCoV-Map：新型肺炎疫情地图](http://106.13.58.203:4000/) 包含地级市疫情
* [Programming-With-Love/2019-nCoV](https://github.com/Programming-With-Love/2019-nCoV) This repo holds the code for crawling the latest news on the pneumonia virus from Clove doctor's website
* ⭐️  291       [lispczz/pneumonia](https://github.com/lispczz/pneumonia) [中国新型冠状病毒肺炎地级市疫情图](https://lispczz.github.io/pneumonia/)
*   ⭐     320  [globalcitizen/2019-wuhan-coronavirus-data](https://github.com/globalcitizen/2019-wuhan-coronavirus-data) This public repository archives data over time from various public sources on the web.
* ⭐️   172        [nextstrain/ncov](https://github.com/nextstrain/ncov) This is a Nextstrain build for novel coronavirus (nCoV), visible at [nextstrain.org/ncov](nextstrain.org/ncov).
* ⭐️     181 [veaba/ncov](https://github.com/veaba/ncov) [2020-nCov感染可视化(科学上网)](http://2020-ncov.datav.ai/) [2019-nCov新版可视化(全实时通信)](http://2019-ncov.datav.ai/) 关注武汉肺炎2019新型冠状病毒（2019-nCoV），数据可视化感染人群热点图、迁徙扩散轨迹，以提供帮助分析疫情。 愿世界安好。
* [839Studio/Novel-Coronavirus-Updates](https://github.com/839Studio/Novel-Coronavirus-Updates) 新增确诊新型冠状病毒肺炎统计数据（每日更新）
* [pzhaonet/ncov](https://github.com/pzhaonet/ncov) [新型冠状病毒疫情信息](https://ncov2020.org/) [pzhaonet/ncovr](https://github.com/pzhaonet/ncovr) R 语言包获取新型冠状病毒（2019-nCoV）数据
* [Moyck/2019NCOV](https://github.com/Moyck/2019NCOV) 一个武汉肺炎的可视化APP
* [JackieZheng/2019-nCoV/](https://github.com/JackieZheng/2019-nCoV/) [全国新型肺炎疫情每日数据动态](https://jackiezheng.github.io/2019-nCoV/web/index.html)
* ⭐️     154         [fluttercandies/ncov_2019](https://github.com/fluttercandies/ncov_2019) 获取新肺炎实时动态App，支持Android和IOS。
* [GuangchuangYu/nCov2019](https://github.com/GuangchuangYu/nCov2019) [query stats of infected coronavirus cases](https://mp.weixin.qq.com/s/_0D8ENb-4lGm4UV16Ok28A)
* [canghailan/Wuhan-2019-nCoV](https://github.com/canghailan/Wuhan-2019-nCoV) 2019-nCoV 新冠状病毒 2019-12-01至今国家、省、市三级每日统计数据（支持接口读取）
* [green512/2019nCoV](https://github.com/green512/2019nCoV) 2019-nCoV 疫情可视化 [疫情散点图](http://nwatch.top:8085/2019ncov/index.html)、 [疫情时空图](http://nwatch.top:8085/2019ncov/heatmaps.html)


### 救助信息 People in need
* [个人求助整理](https://shimo.im/docs/vKV3tRCdkYkqykHv/read)
* [新冠肺炎互助手册](https://shimo.im/docs/XYjcX9XxJJtxTDpr/read) 新闻资讯、互助信息、求援、咨询等  <!-- [受困的人](https://shimo.im/docs/9dj9dWYd3HH3CXPR/read) 原项目为子条目，更新后删除-->
* [wuhancrisis/wuhancrisis.github.io](https://github.com/wuhancrisis/wuhancrisis.github.io) [武汉同胞口罩下的呐喊](https://www.wuhancrisis.com) 收集自二月三日起微博开设的 _肺炎患者求助_ 超级话题中内累计出现过的几千份来自疫区的患者求助.
* [A2N-新型冠状病毒最新疫情信息合集](https://shimo.im/docs/9qrcKpDxHGttRkvP/read)

### 导航网页 Navigation page
* [wertycn/nCoV](https://github.com/wertycn/nCoV)   [2019-nCoV 武汉新冠状病毒肺炎疫情信息导航](http://nav.werty.cn/)
* [WeileiZeng/OpenSourceWuhan](https://github.com/WeileiZeng/OpenSourceWuhan) [武汉开源OpenSourceWuhan](https://weileizeng.github.io/OpenSourceWuhan/)
A collection of all Open Source project for defending Wuhan during 2019-nCoV 支援武汉开源项目汇总
* [byrwiki/jiayou](https://github.com/byrwiki/jiayou) [为2020新型肺炎疫情所做专题信息整合站点](http://jiayou.beiyouren.cn/jiayou)


### 实用工具 Handy applications
* ⭐️       1.4k [KikiLetGo/VirusBroadcast](https://github.com/KikiLetGo/VirusBroadcast) [计算机仿真程序告诉你为什么现在还没到出门的时候！！！](https://www.bilibili.com/video/av86478875)
* [TheWanderingCoel/WuhanPneumoniaBotTelegram](https://github.com/TheWanderingCoel/WuhanPneumoniaBotTelegram) A telegram bot for WuhanPneumonia Status

### 技术组件 Techniquel tools
* [laomocode/yiqin](https://github.com/laomocode/yiqin) [疫情地图](https://wuhan.zw2s.ltd/) 可嵌入网页
* [guanyilun/wuhan_viz](https://github.com/guanyilun/wuhan_viz) [武汉肺炎疫情可视化](http://ncov.firslov.cn/)
* [hack-fang/nCov](https://github.com/hack-fang/nCov) [2019新型肺炎疫情地图(全国、安徽、河北、湖北、浙江)](https://yiqing.ahusmart.com/)

### 新闻舆论 News
* ⭐️          4.4k  [2019ncovmemory/nCovMemory](https://github.com/2019ncovmemory/nCovMemory) 2020新冠肺炎记忆：传媒报道与非虚构写作（持续更新）Memory of 2020 nCov: Media reports and Non-fiction Writings (Continuously updating)
* ⭐️   110     [jiayiliujiayi/2020nCov_individual_archives](https://github.com/jiayiliujiayi/2020nCov_individual_archives) Every individual matters. Every individual has a role to play. 备份普通人在疫情期间的记录。
* [Mainland News Outlets Coverage on 2019-nCoV](https://docs.google.com/document/d/1RqYvfEbLhcyH8rhw0xLpjc2w0JqPBQINzj3ORE-Jka0/edit?usp=sharing)
* [SaveWuhan/NewsCoverageOnWuhan](https://github.com/SaveWuhan/NewsCoverageOnWuhan) 对媒体报道进行脚本抓取的markdown存档，可通过[GitBook](https://freewuhan2020.gitbook.io/wuhan2020/) 浏览
* [lestweforget/wuhan2019](https://github.com/lestweforget/wuhan2019) 本项目主要就中国国内媒体对新冠肺炎（2019.12-）的报道进行备份、存档。
* [疫情之下的劳动者——中文媒体报道收集](https://note.youdao.com/ynoteshare1/index.html?id=eee7c8c3d7b8b054dc94d8abd1a211d8&type=note)
* [Anti404 - 2019nCov信息ICU(外)](https://shimo.im/docs/onq7MwVO6pf4FjA9/read) 旨在保存舆情线索，记录个体遭遇，分专题编排。
* [2020新型冠状病毒报道汇总](https://shimo.im/sheets/QjTYy6rgVV3WDRkh/MODOC/) 分为媒体报道、自媒体评论或报道、热门微博。
* [公众号文章存档: 2019-nCoV](https://2019-ncov.sogiecn.com/) 收录微信公众号上的文章，含原文链接、网页存档、截图存档。
<!-- * [Telegram频道：2019肺炎疫情新闻赛博坟场](https://t.me/wuhancensored) 记录网上曾被消失、篡改的内容。 weilei comments: 经人举报有不合时宜的政治行为，相关内容请查看邮件-->
*   [chinatimeline/chinatimeline.github.io](https://github.com/chinatimeline/chinatimeline.github.io) [时代透镜 武汉肺炎疫情](https://chinatimeline.github.io/wuhan-coronavirus/)
* ⭐️    408         [Pratitya/wuhan2020-timeline](https://github.com/Pratitya/wuhan2020-timeline)    记录自2019年12月起武汉新冠肺炎疫情进展的时间线
* [Internet Archive for 2019 nCov](https://www.notion.so/Internet-Archive-of-2019-nCoV-49f563331d4145c1865f6cc8f0c05132)
* ⭐️   96      [Academic-nCoV/2019-nCoV](https://github.com/Academic-nCoV/2019-nCoV) [关心2019-nCoV疫情，同步国外（学术、正式组织、有影响力的媒体）信息](https://github.com/Academic-nCoV/2019-nCoV/wiki)
* [WeileiZeng/red-cross](https://github.com/WeileiZeng/red-cross) [湖北/武汉红十字 云监工平台](https://weileizeng.github.io/red-cross/) 官网公示数据收集与可视化
* [武汉市新冠肺炎疫情防控指挥部发放捐赠物资统计](https://caysnuts.github.io/monitor/index.html) 物资发放数据可视化，数据来自武汉红会
* [2019新冠肺炎-全球报道](https://2019ncptoday.news.blog/) 网站收录、翻译全球范围内对于2019新冠病毒的英文、西语、德语等其他语种的客观报道

<!-- ### 暂未分类 -->


### 推荐网页 Site recommendation
[武汉开源OpenSourceWuhan](https://weileizeng.github.io/OpenSourceWuhan/)
集结了支援武汉的开源项目，是一个连结各个开源项目的入口。本站持续跟新中。
* 给本站推荐项目请点这里 [Open issue at GitHub](https://github.com/WeileiZeng/OpenSourceWuhan/issues/new?assignees=&labels=&template=------.md&title=%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%E6%8E%A8%E8%8D%90%3A+%E9%A1%B9%E7%9B%AE%E5%90%8D%E7%A7%B0)
* 也可评论或者[Contact me](https://weileizeng.com/news/1992/06/29/contact/)


<div id="fb-root"></div>
<script async defer crossorigin="anonymous" src="https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v6.0"></script>

<div class="fb-comments" data-href="https://weileizeng.github.io/OpenSourceWuhan/" data-width="100%" data-numposts="1"></div>
