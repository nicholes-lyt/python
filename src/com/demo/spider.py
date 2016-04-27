'''
Created on 2016年4月26日

@author: liyut
'''
from urllib import request
from bs4 import BeautifulSoup

class BsoupHTML(object):
    #打开页面
    def getUrl(self,url,coding='utf-8'):  
        req = request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 UBrowser/5.5.9703.2 Safari/537.36')
        with request.urlopen(req) as response:
            return BeautifulSoup(response.read().decode(coding))
            