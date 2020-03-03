#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# use Github API to get the data of repos, including star_counts
# do some post processing like statistics of all stars and all forks.


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
    print(text)
    return text




# set up requests
import requests
requests_session= requests.Session()
headers = { "Authorization":"token c58787df512215bf52cd71268a9272f60a46a568"} # change github api rate limit from 60/hour to 5000/hour
requests_session.headers.update(headers)

def get_stargazers_count(requests_session,repo_name):
    response=requests_session.get(
        "https://api.github.com/repos/"+repo_name
    )
    data= response.json()
    if (response.status_code == 403 ):
        # 403 forbidden, passing rate limit
        print(data)
    # collect needed data, see sample.json for full data
    output = {
        'repo_name':repo_name,
        'stargazers_count':data['stargazers_count'],
        'subscribers_count':data['subscribers_count'],
        'forks':data['forks']
        }
    #jprint(output)
    print(repo_name,' has stars ',data['stargazers_count'])
    save( data, repo_name )
    return output

# read  list of repos
import yaml
def counting(requests_session, file_name,group_name,summary_file):
    # prepare output
    statistics={
        'projects_count':0,
        'repos_count':0,
        'stars_count':0,
        'forks_count':0
    }
    
    stream = open(file_name,'r')
    # data is a json object
    data=yaml.full_load(stream)
    stream.close()
    for country in data:
        print( '   --- processing the current group/country: ', country[group_name] )
        for repo in country['repos']:
            statistics['projects_count'] +=1
            try: 
                repo_name=repo['repo_name']
                # print(repo_name)
                data = get_stargazers_count(requests_session, repo_name)
                statistics['repos_count'] +=1
                statistics['stars_count'] += data['stargazers_count']
                statistics['forks_count'] += data['forks']
            except KeyError:
                print('no repo for this project')

    # print output
    print('summary')
    #print(statistics)
    with open(summary_file,'w') as f:
        f.write(jprint(statistics))
    # print('summary:',repos_count,' repos with ',stars_count,' stars in total.')
    
file_name="../_data/world.yml"
group_name="country"

#counting(requests_session, file_name,group_name)
counting(requests_session, "../_data/world.yml","country","../_data/summary_world.json")
counting(requests_session, "../_data/wuhan.yml","group_name","../_data/summary_wuhan.json")

