#    python 爬虫网页
import urllib.request;
#from FileUtils import saveFile;

import os;

try:
    #获取地址信息
    url = 'http://jiankang.baidu.com/juhe/index?qid=0&pssid=0&pvid=1460631863628608197&tn=NONE&zt=self&wd=&key=%E5%84%BF%E7%AB%A5%E5%8C%BB%E9%99%A2&aType=27';
    data = urllib.request.urlopen(url).read();
    data = data.decode('UTF-8');
    #print(data);
    
except:
    print('Error:请求地址错误！');

    
#打开一个文本文件
'''
fp = open("d:\\python-crawler\\web.txt", "w");
fp.write(data);
fp.close();#关闭文件
'''

def saveFile(pathFile,data,openMode):
    if(os.path.exists(pathFile)== True):
        fp = open(pathFile, openMode);
        fp.write(data);
        fp.close();#关闭文件
        print('文件已保存成功！')
    else:
        os.mkdir(pathFile);
        print('创建文件路径为：'+pathFile);
        
'''
将data内容保存到d盘
'''
pathFile = "d:\\python-crawler\\web\\w1.txt";
openMode = "w";#文件打开方式
saveFile(pathFile,data,openMode);
