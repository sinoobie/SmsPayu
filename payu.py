#Author: KANG-NEWBIE (noobie)

import requests,time,os

class Payu:
	def __init__(self):
		self.u='https://nuubi.herokuapp.com/api/smsgratis'
		self.banner()

	def banner(self):
		os.system('clear')
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;
		; SMS Gratis PayuTerus ;
		;    By KANG-NEWBIE    ;
		;;;;;;;;;;;;;;;;;;;;;;;;
		""")
		no=input('[?] Nomor Target: ')
		psn=input('[info] ketik "\\n" untuk garis baru pada pesan\n[?] Pesan: ')
		self.main(no,psn)

	def main(self,no,msg):
		sub=requests.post("https://nuubi.herokuapp.com/api/smsgratis",
			data={'number': no, 'pesan': msg}).json()
		if sub['status'] == 'ok':
			print(f"[#] {sub['msg']}")
		else:
			print(f"[#] {sub['msg']}")

try:
	Payu()
	while True:
		plh=input("\n[?] kirim lagi (y/n) ")
		if plh.lower() == 'y':
			Payu()
		elif plh.lower() == 'n':
			exit('sampai jumpa lagi...')
except KeyboardInterrupt:
	print('\nErr: KeyboardInterrupt')
except Exception as E:
	print('Err: %s'%(E))
