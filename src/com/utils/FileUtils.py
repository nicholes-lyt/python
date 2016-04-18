'''
Created on 2016年4月18日

将文件保存到本地磁盘

@author: liyut
'''
import os;

'''
    pathFile:文件路径
    data:保存数据
    openMode:打开方式
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
    
