import requests,re,os
from bs4 import BeautifulSoup
import 贴吧只看楼主下载,tieba_image
requests.get('http://ia.51.la/go1?id=20246951&pvFlag=1')#统计使用人数，可删除此行。
p=0
tieba = input('贴吧名（不带吧）：')
folder = os.getcwd()+'/'+tieba # os.getcwd() #获取当前绝对路径 # + 编写目录
test=os.path.exists(folder)
if not test:
        os.mkdir(folder)            #--------------------创建文件夹 

input1 = input('贴吧链接是否带https？输入y/n（小写）： ')
inputjpg = input('下载文章输入1，下载图片输入2：\n')

#------------------------------最后一页检测：
lastpage = requests.get('https://tieba.baidu.com/f?kw='+str(tieba)).text
soup = BeautifulSoup(lastpage,'lxml')
last_item =soup.find_all('a',attrs={'class':'last pagination-item'})
lastpage = int(last_item[0]['href'].split('=')[-1])
print(lastpage)
print('总页数：%s'%(lastpage/50))


while True:#获取帖子链接，循环翻页
    url = 'https://tieba.baidu.com/f?kw='+str(tieba)+'&ie=utf-8&pn='+str(p)
    print(url)
    r=requests.get(url).text
    p += 50
    urllist=BeautifulSoup(r,'lxml').find_all('a',attrs={'class':'j_th_tit'})
    a = re.findall('href=\"/p/.*?\"',str(urllist))#正则后
    print('当前页数：')
    print(p/50)
    if p > lastpage:
        print('没有帖子了！任务完成，共爬取了%s个帖子'%lastpage)
        input('')
        break
    if input1 == 'y':
        # print(urllist)
        # print('---------------------------------')
        for aa in a:
            aa = 'https://tieba.baidu.com'+aa[6:-1]#构造完整链接
            if inputjpg == '1':
                贴吧只看楼主下载.run(aa,tieba)
            else:
                tieba_image.run(aa,tieba)
    else:
        for aa in a:
            aa = 'http://tieba.baidu.com'+aa[6:-1]#构造完整链接
            if inputjpg == '1':
                贴吧只看楼主下载.run(aa,tieba)
            else:
                tieba_image.run(aa,tieba)
    
