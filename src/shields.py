#!/usr/local/bin/python3
# !/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# only update shields at every push

# use Github API to get the data of repos, including star_counts
# do some post processing like statistics of all stars and all forks.
# bug note: invalid repo name with https:// would raise an error: ValueError: too many values to unpack
print("only update shields at every push")


# set up requests
import requests
requests_session= None

import shutil
def download_image(repo_name):
    print(repo_name)
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
    debug = False
    if debug:
        for r in shields_repo_name :
            print("---debug mode---:     r =",r)
            download_image(r)            
    else:
        pool.map(download_image,shields_repo_name)
    

#counting(requests_session, file_name,group_name)

from multiprocessing import Pool
import sys
if __name__ == "__main__":
    pool_size=10
    if (str(sys.argv[-1]) == "--debug"):
        print("debug mode on. single thread used")
        pool_size=1
    else:
        print("use --debug to turn on single threads for debuging. There is also a switch in the function.")
    pool=Pool(pool_size)
    #much faster with pool
    counting(pool,requests_session, "../_data/global.yml","group_name","../_data/summary_global.json")
    print("finish gloabl and start china")
    counting(pool,requests_session, "../_data/china.yml","group_name","../_data/summary_china.json")
    counting(pool,requests_session, "../_data/areas.yml","group_name","../_data/summary_areas.json")


