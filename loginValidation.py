import urllib.request
import urllib
from urllib.request import urlopen

def validateLogin(IDnum):
    file_url='https://ryan-segali.github.io/menu/customer_data.txt'
    getlines=[]
    rightid=False
    for line in urllib.request.urlopen(file_url):
        decoded=line.decode('utf-8')
        info=decoded.split(',')
        id=info[0]
        if info[0]==IDnum:
            rightid=True