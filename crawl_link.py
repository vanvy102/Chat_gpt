import requests
from bs4 import BeautifulSoup
import config as cf
import unidecode
def get_link_cafef(ticker):
#headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    header='https://s.cafef.vn'
#Lấy địa web trên trang cafef.vn
    nh=cf.get_name_cp()
    kd=[]
    for i in nh:
        kd.append(unidecode.unidecode(i).lower())
    for n in range(len(kd)):
        if ' - ' in kd[n]:
            kd[n]=kd[n].replace(' - ','-')
            kd[n]=kd[n].replace(' ','-')
        else:
            kd[n]=kd[n].replace(' ','-')
    ticket=cf.get_ticket()
    code=cf.get_trade_code()

    for i in range(len(ticket)):
        URL=header+'/'+code[i]+'/'+ticket[i]+'-'+kd[i]+'.chn'
        resp=requests.get(url=URL)
    #định dạng web
        soup=BeautifulSoup(resp.content,"html.parser")
    #tìm đến vị trí có chứa URL
        link=soup.find('ul',attrs={'class':'tlist'})
        crawl_link=link.find_all('a')
        URLS=[]
        for links in crawl_link:
            URLS.append(links['href'])
        webs=[]
    #các bài đường dẫn liên quan.
        for u in URLS:
            k=header+ u
            webs.append(k)
        return webs
