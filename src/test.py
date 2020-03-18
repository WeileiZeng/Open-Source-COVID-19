#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3


import json
import requests
# now use json file to produce shields

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
    print(summary)
    for k,v in summary.items():
        print(k)
        #print(v)
        label=k[:-6]
        counts=v
        url="https://img.shields.io/static/v1?label="+label+"&message="+str(counts)+"&color=brightgreen"
        print(url)
        save_filename='../assets/page_summary/'+page_name+'_'+k+'.svg'
        download_svg_by_url(url, save_filename)
        requests.get

    
update_summary_badge('world')
update_summary_badge('china')
