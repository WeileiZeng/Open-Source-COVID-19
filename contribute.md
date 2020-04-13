## Contribution guide
The primary purpose of this project is to collect useful open source projects and display them by categories and region. I use github pages (jekyll) for the website, hence all data are saved in yaml format. Some python scripts are added for postprocessing.

### Data format
All data are saved in three files in _data folder.
* global.yml
  * projects applying to global scale. used in homepage index.md
* areas.yml
  * projects focusing on some countries or areas. used in countries/areas page, area.md
* china.yml
  * data entries for the projects in china.md
  
Each project make up one entry in the file. An entry is defined in [meta.yml](https://github.com/WeileiZeng/Open-Source-COVID-19/blob/master/_data/meta.yml) Add entries in those files, and the website will render it and display automatically.

### where to find projects
* from your own experience
* search on github and web
* http://open-source-covid-19.weileizeng.com/search use this page. It updates once a day.
* from issues and pull request
* etc

Usually when I add a project, I open an issue as a feedback, with the following title and content. This step is optional.

### Added to Open Source COVID-19

Thanks for your work to help the people in need! Your site has been added to the Open-Source-COVID-19 page, which collects open source projects related to COVID-19, including maps, data, news, api, analysis, medical and supply information, etc. Please share to anyone who might need the information in the list, or will possibly contribute to some of those projects. You are also welcome to recommend more projects.

http://open-source-covid-19.weileizeng.com/

Cheers!


### render logic
After adding an entry (and push to the origin), these steps will be done automatically (at every push). They would took one min in total.
* src/tags.py collect tags in the three data file and save it into tags.yml and tags_projects.yml. These two files are used for the tag page.
* src/shields.py. generate shields for each project. A shield is an svg picture showing the number of stars.
* github page rebuild the website

### local test
If you fork it, you can test it by turning on github pages "setting -> github pages -> master banch"

To do a local test. You need to install jekyll first, and then install gems for the project.
* install ruby environment
* gem install jekyll bundler
* bundle install
* bundle exec jekyll serve

A guide is [here](https://github.com/github/personal-website), see the installation section.


#### [返回首页](./)

