import requests,os,re,time
from bs4 import BeautifulSoup
xuhao = 0
def run(put,tieba):
    global xuhao
    p = 0
    print('-----------------------------------------')
    inputurl = put
    url = inputurl+'?see_lz=1&pn='
    title = '你是怎么发现这个bug的'
    once = 0
    
    while True:
      p += 1
      r = requests.get(url+str(p))
      if inputurl[:5] == 'http:':
        soup  = BeautifulSoup(r.text,'lxml').find_all('div',attrs='d_post_content j_d_post_content clearfix')
      else:
        soup  = BeautifulSoup(r.text,'lxml').find_all('div',attrs='d_post_content j_d_post_content')
      sumpage = BeautifulSoup(r.text,'lxml').select('#thread_theme_5 > div.l_thread_info > ul > li:nth-child(2) > span:nth-child(2)')
      try:
        sumpage = sumpage[0].get_text()
      except:
        print('错误，IndexError: list index out of range')
        print(sumpage)
        time.sleep(20)

        break
      if once != 1 :
        xuhao += 1
        if inputurl[:5] == 'http:':
          # print('检测为大型吧，采用方案1')
          title = BeautifulSoup(r.text,'lxml').select('#j_core_title_wrap > div.core_title.core_title_theme_bright > h1')
          
        elif inputurl[:5] == 'https':
          # print('检测为小众吧，采用方案2')
          title = BeautifulSoup(r.text,'lxml').select('#j_core_title_wrap > h3')

        else:
          print('链接格式有误，请确保输入http/https')
          input()  
        title = title[0].get_text()
        print('获取标题:',title)
      dr = re.compile(r'<[^>]+>',re.S)
      done = dr.sub('',str(soup).replace("<br/>", "\r\n").replace("            ","\r\n"))#去标签正文 
      print('下载第%s页'%p)
      try:
        with open(tieba+'/'+str(title)+'.txt','a',encoding='utf-8')as f:
          f.write(str(done))
      except:
        print('文件名非法，重命名为序号')
        
        with open(tieba+'/'+str(xuhao)+'.txt','a',encoding='utf-8')as f:
          f.write(str(done))
          pass
      once = 1
      if p  >= int(sumpage):
        print('done')
        # check = input('按回车继续，退出输入q')
        break
    # if check == 'q':
    #   break