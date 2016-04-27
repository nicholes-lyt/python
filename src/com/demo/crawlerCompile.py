'''
Created on 2016年4月26日

@author: liyut
'''


import urllib.request
import re

def getHtml(urlPath):
    data = urllib.request.urlopen(urlPath).read().decode('utf-8')
    return data


url = "http://www.baidu.com";
data = getHtml(url)

#print data
pattern = re.compile('<div id="u1">(.*?)</div>',re.S)
result = re.findall(pattern, data)
print('第一次截取：',result[0])

pattern2 = re.compile('<a href="(.*?)" .*?>(.*?)</a>',re.S)
result2 = re.findall(pattern2, result[0])
for row in result2:
    print('第二次截取：',row)


       