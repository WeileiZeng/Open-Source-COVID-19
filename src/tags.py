#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3


# read  list of repos
import yaml
def counting(pool, requests_session, file_name,group_name,summary_file):
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
    shields_repo_name=[]
    stream.close()
    for country in data:
        print( '   --- processing the current group/country: ', country[group_name] )
        for repo in country['repos']:
            statistics['projects_count'] +=1
            try: 
                repo_name=repo['repo_name']
                #download_image(repo_name)
                shields_repo_name.append(repo_name)
            except KeyError:
                print('no repo for this project')
            #some may have two repo
            try: 
                repo_name=repo['repo2_name']
                #download_image(repo_name)
                shields_repo_name.append(repo_name)
                print('got repo2: '+repo_name)
            except KeyError:
                #print('no repo2')
                pass
    debug = False #True
    if debug:
        for r in shields_repo_name :
            download_image(r)            
    else:
        pool.map(download_image,shields_repo_name)
    

# read data
filenames=[
    "../_data/global.yml",
    "../_data/china.yml",
    "../_data/areas.yml"
]
projects = []
for filename in filenames:
    
    with open(filename, 'r') as f:
        groups = yaml.full_load(f)
        for group in groups:
            group_name=group['group_name']
            repos=group['repos']            
            projects = projects + repos
print(len(projects))

# get all tags with corresponding projects
tags={}
tags['others']=[]
for p in projects:
    try:
        for tag in p['tags']:
            try:
                tags[tag].append(p)
            except KeyError:
                tags[tag]=[p]
    except KeyError:
        # if the project doesn't have a tag.
        tags['others'].append(p)

#print tags
tags_only=[]
for k in tags:
    tags_only.append(k)
    print(k)


#change dict to list
tags_projects=[]
for k,v in tags.items():
    group={ 'group_name':k,
            'repos':v }
    tags_projects.append(group)


with open('../_data/tags_projects.yml','w') as f:
    yaml.dump(tags_projects,f)
with open('../_data/tags.yml','w') as f:
    yaml.dump(tags_only,f)

    
print('done')


