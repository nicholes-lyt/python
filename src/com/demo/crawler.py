#    python 爬虫网页

from _collections import deque
import re
import urllib.request


queue = deque();
visited = set();

# 入口页面, 可以换成别的
url = 'http://jiankang.baidu.com/juhe/index?qid=0&pssid=0&pvid=1460631863628608197&tn=NONE&zt=self&wd=&key=%E5%84%BF%E7%AB%A5%E5%8C%BB%E9%99%A2&aType=27'; 

queue.append(url);
cnt = 0;

while queue:
    url = queue.popleft();#队首元素出列
    visited |= {url};
    
    print('已经抓取：'+str(cnt)+' 正在抓取 --->'+url);
    cnt += 1;
    urlop = urllib.request.urlopen(url);
    if 'html' not in urlop.getheader('Content-Type'):
        continue;
    #避免程序异常终止，用try catch处理异常
    try:
        data = urlop.read().decode('utf-8');
        #print(data);
        #print(type(urlop));
        print('--------html start-------');
        print(data);
        print('--------html end-------');
    except:
        continue;
    
    #正在表达式提取页面中所有队列，并判断是否已经访问过，然后加入待爬队列
    linkre = re.compile('href=\"(.+?)\"');
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x);
            print('加入队列---> '+x);
            
            
            