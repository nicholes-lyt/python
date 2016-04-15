#    python 爬虫网页
import urllib.request;

#获取地址信息
url = 'http://jiankang.baidu.com/juhe/index?qid=0&pssid=0&pvid=1460631863628608197&tn=NONE&zt=self&wd=&key=%E5%84%BF%E7%AB%A5%E5%8C%BB%E9%99%A2&aType=27';
data = urllib.request.urlopen(url).read();
data = data.decode('UTF-8');
print(data);
