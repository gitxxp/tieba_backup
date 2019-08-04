import threading,re,time,requests
from bs4 import BeautifulSoup

task = []
Name = []
n=0


def download(threadname,tieba):
    while len(task) > 0:
        global n
        jpg = requests.get(task.pop()).content
        with open(tieba+'/'+str(Name.pop()),'wb') as f:
            f.write(jpg)
        print ("%s" % (threadname)+'剩余：'+str(len(task)))
        
def run(url,tieba):
    p=1
    startime = time.time()
    r = requests.get(url)
    sumpage = BeautifulSoup(r.text,'lxml').select('#thread_theme_5 > div.l_thread_info > ul > li:nth-child(2) > span:nth-child(2)')
    sumpage = int(sumpage[0].get_text())
    while p <= sumpage and sumpage !=1:
        r = requests.get(url+'?pn=%s'%p).text
        p += 1
        for i in re.findall('https://imgsa.baidu.com/forum/.*?jpg',str(r)):
            name = i.split('/')[-1]
            Name.append(name)
            task.append('https://imgsrc.baidu.com/forum/pic/item/'+name)
    else:
        for i in re.findall('https://imgsa.baidu.com/forum/.*?jpg',str(r.text)):
            name = i.split('/')[-1]
            Name.append(name)
            task.append('https://imgsrc.baidu.com/forum/pic/item/'+name)
    if len(task) >= 30:
        for ii in range(30):
            ii = str(ii)
            thread1 = threading.Thread(target=download,args=('线程'+ii,tieba))
            thread1.start()
    else:
        for ii in range(7):
            ii = str(ii)
            thread1 = threading.Thread(target=download,args=('线程'+ii,tieba))
            thread1.start()
    thread1.join()  
    print('任务完成，耗时：%s' %(time.time()-startime))
    
if __name__ == "__main__":
    print('请在程序同目录下手动创建文件夹“temp”，否则报错')
    url = input('网址： ')
    run(url,'temp')
