'''
save data to data_heroes/heroes.json
file structure
[
 {
   full_name:
   contributors:
   [
   {
    login:
    id:
    contributions:
   }
   ]
 }
]
'''
import requests
import json

def save(api_content,username):
    with open('data_heroes/'+username.replace('/','.')+'.json','w') as f:
        f.write(
            json.dumps(api_content, sort_keys=True, indent=4)
        )


def get_list_of_repos():
    #search those keywords and save response to files
    searching_keywords=['COVID','nCoV','covid19']

    #combine the lists and remove duplicates
    repos=[]
    duplicates={}
    for k in searching_keywords:
        with open('github_search_'+k+'.json','r') as f:
            items=json.load(f)['items']
            #check
            for i in items:
                try:
                    print( duplicates[i['full_name']] + '--->duplicates')
                except KeyError:
                    duplicates[i['full_name']]=i['full_name']
                    repos.append(i)
                #print(i['full_name'])
            #repos = repos + items
            #print(len(repos))
    print('after removing duplicates, we got a list of size')  
    print(len(repos))
    return repos
    # now check the list to remove duplicates and forks

get_list_of_repos()
exit()
    
keyword="COVID"
keyword="nCoV"
keyword="covid19" # a lot of repos start with that name

#response=requests.get("https://api.github.com/search/repositories?q="+keyword+"&sort=stars&order=desc")


heroes=[]

#res = response.json()
f = open('github_search_COVID.json','r')
res = json.load(f)
f.close()
#information keys to save
contributor_keys=['login','id','contributions']
repo_keys=['id','full_name','fork']
for repo in res['items']:
  #print(repo)
  repo2={}
  for k in repo_keys:
      repo2[k]=repo[k]
  contributors = requests.get(repo['contributors_url']).json()
  #print(contributors)
  #break
  repo_heroes=[]
  for contributor in contributors:
      #save(contributor, contributor.login)      
      #print(json.dumps(contributor,indent=2))
      hero={}
      for k in contributor_keys:
          hero[k]=contributor[k]
      repo_heroes.append(hero)
  repo2['contributors']=repo_heroes
  #print(json.dumps(repo_heroes, indent = 2))  
  heroes.append(repo2)
  print(json.dumps(heroes, indent = 2))
  
with open('list_heroes.json','w') as f:
    f.write(json.dumps(heroes, indent = 2))
    
