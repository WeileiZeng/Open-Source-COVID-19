#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

#search on github to get some information


# save api requests to files
def save(api_content,repo_name):
    with  open( 'json_api/'+repo_name.replace('/','.')+'.json','w') as f:
        f.write(
            json.dumps(api_content, sort_keys=True, indent=4)
        )

    
import json
# print a json object or a dictionary
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    #print(text)
    return text



# set up requests
import requests
requests_session= requests.Session()
headers = { "Authorization":"token c58787df512215bf52cd71268a9272f60a46a568"} # change github api rate limit from 60/hour to 5000/hour
requests_session.headers.update(headers)




def get_repos_by_keyword(requests_session, keyword):
    response=requests_session.get("https://api.github.com/search/repositories?q="+keyword+"&sort=stars&order=desc&per_page=100")
    rj = response.json()
    #print(rj['total_count'])
    total_count=rj['total_count']
    limit = 1000
    max_count=  total_count if total_count < limit  else limit 
    print('max_count = '+ str(max_count))
    iteration = (max_count-1) // 100 + 1
    repos=rj['items']
    for i in range(2,iteration+1):
        print('now getting result starting index '+str((i-1)*100+1) + ', keyword = '+ keyword)
        response=requests_session.get("https://api.github.com/search/repositories?q="+keyword+"&sort=stars&order=desc&per_page=100&page="+str(i))
        rj = response.json()
        repos=repos + rj['items']

    # now all repos in repos
    #print(len(repos))
    return repos

    
def remove_duplicates(repos_raw):
    #remove duplicate in repos
    repos=[]
    duplicates={}
    for i in repos_raw:
                try:
                    print( duplicates[i['full_name']] + '--->duplicates')
                except KeyError:
                    duplicates[i['full_name']]=i['full_name']
                    repos.append(i)

    print('after removing duplicates, we got a list of size')
    print(len(repos))
    return repos

def get_current_repos():
    repos=[]
    repos=repos+get_repo_by_filename('../../_data/china.yml')
    repos=repos+get_repo_by_filename('../../_data/global.yml')
    repos=repos+get_repo_by_filename('../../_data/areas.yml')
    return repos
    
import yaml
def get_repo_by_filename(file_name):
    stream = open(file_name,'r')
    # data is a json object
    data=yaml.full_load(stream)
    shields_repo_name=[]
    stream.close()

    for country in data:
        print( '   --- processing the current group/country: ', country['group_name'] )
        for repo in country['repos']:
            try:
                repo_name=repo['repo_name']
                shields_repo_name.append(repo_name)
            except KeyError:
                print('no repo for this project')
            #some may have two repo
            try:
                repo_name=repo['repo2_name']
                shields_repo_name.append(repo_name)
                print('got repo2: '+repo_name)
            except KeyError:
                #print('no repo2')
                pass
    return shields_repo_name
        

def remove_existed(repos, my_repos):
    # my_repos: repo already listed in website
    repos2=[]

    for r in repos:
        full_name = r['full_name']
        if full_name in my_repos:
            print( 'existed: '+ full_name)
        else:
            repos2.append(r)
    print('raw size: '+ str(len(repos)))
    print('after removed: '+ str(len(repos2)))
    return repos2       

def reduce_repo_size(repos,min_stars):
    # only remain necessary infor
    keys=['full_name','stargazers_count','description','fork','forks','homepage']
    repos_short=[]
    for repo in repos:
        if repo['stargazers_count'] > min_stars :
            repo_temp={}
            for k in keys:
                repo_temp[k]=repo[k]
            repos_short.append(repo_temp)
    return repos_short


my_repos = get_current_repos()

keywords=['COVID','nCoV','covid19','corona','sars-cov-2','coronavirus']
#keywords=['COVID']
repos=[]
for k in keywords:
    repos = repos + get_repos_by_keyword(requests_session, k)

repos = remove_duplicates(repos)    

repos2 = remove_existed(repos, my_repos)

# at least 10 stars
repos3=reduce_repo_size(repos2, 10)
#now save data

with open("../../_data/github_search.yml","w") as f:
    yaml.dump(repos3,f)
print("done")
