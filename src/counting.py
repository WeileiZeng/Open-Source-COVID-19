#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# use Github API to get the data of repos, including star_counts
# do some post processing like statistics of all stars and all forks.

print("this script calculate the summary of wuhan page and world page. The summary has been saved in _data/*.yml, and will be loaded automatically. You can run this once a while after adding site regularly.")

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



import shutil
def download_image(repo_name):
    [owner,name]=repo_name.split('/')
    save_folder='../assets/shields/'
    #save_folder='../'
    save_filename=save_folder+owner+'-'+name+'.svg'
    # This is the image url.
    #image_url="https://img.shields.io/github/stars/theleadio/corona-frontend?color=yellow&label=&logoColor=blue&style=social"
    image_url="https://img.shields.io/github/stars/"+repo_name+"?color=yellow&label=&logoColor=blue&style=social"
    
    # Open the url image, set stream to True, this will return the stream content.
    resp = requests.get(image_url, stream=True)
    # Open a local file with wb ( write binary ) permission.
    local_file = open(save_filename, 'wb')
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True
    # Copy the response stream raw data to local image file.
    shutil.copyfileobj(resp.raw, local_file)
    local_file.close()
    # Remove the image url response object.
    del resp
    print(save_filename)
#repo_name='WeileiZeng/tutorial'
#download_image(repo_name)



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
                download_image(repo_name)
            except KeyError:
                print('no repo for this project')
            #some may have two repo
            try: 
                repo_name=repo['repo2_name']
                # print(repo_name)
                data = get_stargazers_count(requests_session, repo_name)
                statistics['repos_count'] +=1
                statistics['stars_count'] += data['stargazers_count']
                statistics['forks_count'] += data['forks']
                download_image(repo_name)
                print('got repo2: '+repo_name)
            except KeyError:
                #print('no repo2')
                pass

                

    # print output
    print('summary')
    #print(statistics)
    with open(summary_file,'w') as f:
        f.write(jprint(statistics))
    # print('summary:',repos_count,' repos with ',stars_count,' stars in total.')
    
file_name="../_data/global.yml"
group_name="group_name"

#counting(requests_session, file_name,group_name)
counting(requests_session, "../_data/global.yml","group_name","../_data/summary_global.json")
counting(requests_session, "../_data/china.yml","group_name","../_data/summary_china.json")
counting(requests_session, "../_data/areas.yml","group_name","../_data/summary_areas.json")



print("this script calculate the summary of wuhan page and world page. The summary has been saved in _data/*.yml, and will be loaded automatically. You can run this once a while after adding site regularly.\nThis one also update all shields and json file")



# now use json file to produce shields for page summary

import shutil
def download_svg_by_url(image_url, save_filename):
    resp = requests.get(image_url, stream=True) 
    local_file = open(save_filename, 'wb')
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    local_file.close()
    del resp
    
def update_summary_badge(page_name):
    filename='../_data/summary_'+page_name+'.json'
    summary={}
    with open(filename,'r') as f:
        summary=json.load(f)
    for k,v in summary.items():
        label=k[:-6]
        counts=v
        url="https://img.shields.io/static/v1?label="+label+"&message="+str(counts)+"&color=brightgreen"
        print(url)
        save_filename='../assets/page_summary/'+page_name+'_'+k+'.svg'
        download_svg_by_url(url, save_filename)        
    return summary

s1=update_summary_badge('global')
s2=update_summary_badge('china')
s3=update_summary_badge('areas')
total={}
for k in s1:
    total[k]=s1[k]+s2[k]+s3[k]
with open('../_data/summary_total.json','w') as f:
    f.write( json.dumps(total, indent=2) )
update_summary_badge('total')
print("finish generate summary badge")



