import requests,re,os
from bs4 import BeautifulSoup
import 贴吧只看楼主下载
p=0
tieba = input('贴吧名：')
folder = os.getcwd()+'/'+tieba # xxx = os.getcwd() #获取当前绝对路径 # + 编写目录
test=os.path.exists(folder)
if not test:
        os.mkdir(folder)            #--------------------创建theme文件夹 
else:
        pass
input1 = input('贴吧链接是否带https？输入y/n：')
while True:
    url = 'https://tieba.baidu.com/f?kw='+str(tieba)+'&ie=utf-8&pn='+str(p)
    r=requests.get(url).text
    p += 50
    soup = BeautifulSoup(r,'lxml')
    urllist=soup.find_all('a',attrs={'class':'j_th_tit'})
    a = re.findall('href=\"/p/.*?\"',str(urllist))#正则后
    print(p/50)
    if len(a) == '0':
        print('没有帖子了！')
        input()
    if input1 == 'y':
        # print(urllist)
        # print('---------------------------------')
        for aa in a:
            aa = 'https://tieba.baidu.com'+aa[6:-1]#构造完整链接
            贴吧只看楼主下载.run(aa,tieba)
    else:
        for aa in a:
            aa = 'http://tieba.baidu.com'+aa[6:-1]#构造完整链接
            贴吧只看楼主下载.run(aa,tieba)
    