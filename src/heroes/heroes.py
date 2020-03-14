import yaml
import requests

def save(api_content,username):
    with  open( 'json_api/'+username.replace('/','.')+'.json','w') as f:
        f.write(
            json.dumps(api_content, sort_keys=True, indent=4)
        )
     
def getUserInfo(user):
  r = requests.get('https://api.github.com/user'+user)
  return r
