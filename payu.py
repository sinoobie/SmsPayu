#Author: KANG-NEWBIE
#Contact: t.me/kang_nuub
#SPECIAL THANKS TO WIDHI

#peringatan buat kang recode, kontol!
#recode tidak akan membuatmu menjadi pro-programmer!

import mechanize,time,os
from bs4 import BeautifulSoup as BS

class Payu:
	def __init__(self):
		#install browser
		self.br = mechanize.Browser()
		self.br.set_handle_equiv(True)
		self.br.set_handle_gzip(True)
		self.br.set_handle_redirect(True)
		self.br.set_handle_referer(True)
		self.br.set_handle_robots(False)
		self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		self.br.addheaders =[('Connection','keep-alive'),
		('Pragma','no-cache'),
		('Cache-Control','no-cache'),
		('Origin','http://sms.payuterus.biz'),
		('Upgrade-Insecure-Requests','1'),
		('Content-Type','application/x-www-form-urlencoded'),
		('User-Agent','Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'),
		('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'),
		('Referer','http://sms.payuterus.biz/alpha/'),
		('Accept-Encoding','gzip, deflate'),
		('Accept-Language','id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'),
		]
		self.u='http://sms.payuterus.biz/alpha'
		self.banner()

	def banner(self):
		os.system('clear')
		print("""
		;;;;;;;;;;;;;;;;;;;;;;
		; PayuTerus Spammers ;
		;   By KANG-NEWBIE   ;
		;;;;;;;;;;;;;;;;;;;;;;
		""")
		no=int(input('[?] Nomor Target: '))
		psn=input('[?] Pesan: ')
		jm=int(input('[?] Jumlah: '))
		msg=psn.split(' ')
		if jm > 20:
			exit('[Sorry] Jangan kebanyakan gan!!!')
		else:
			for i in range(jm):
				self.main(no,msg)
				time.sleep(1.5)

	def main(self,no,msg):
		o=[]
		bs=BS(self.br.open(self.u),features="html.parser")
		for x in bs.find_all("span"):
			o.append(x.text)
		capt=int(str(o)[2])+int(str(o)[6])
		self.br.select_form(nr=0)
		self.br.form['nohp']=str(no)
		self.br.form['pesan']=str(msg)
		self.br.form['captcha']=str(capt)
		sub=self.br.submit().read()
		if 'SMS Gratis Telah Dikirim' in str(sub):
			print('[+] Sukses mengirim sms ke',no)
		else:
			print('[-] Gagal mengirim sms ke',no)

try:
	Payu()
except KeyboardInterrupt:
	print('\nErr: KeyboardInterrupt')
except Exception as E:
	print(f'Err: {E}')
