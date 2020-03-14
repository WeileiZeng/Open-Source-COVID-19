from multiprocessing import Pool
from time import sleep
import requests
def f(x):
    print('hello ',x)
    sleep(1)
    print('by ',x)

def get(url):
    res = requests.get(url)
    print(res)
    
def test1():
    pool=Pool(100)
    for i in range(20):
        #pool.map(f,['weilei','kangkang','love','more','and'])
        pool.map(f,range(9))

def test2():
    pool=Pool(100)
    print('get Pool')
    url="https://4chan.org"
    urls=[url]*100
    print(urls)
    pool.map(get,urls)
if __name__ == "__main__":    
    test2()




    

