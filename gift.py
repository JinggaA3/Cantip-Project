#!/usr/bin/python3
# -*- coding: utf-8 -*-
#///////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
#///////////                                                         ///////////
#///////////           ▐▀▄        ▄▀▌   ▄▄▄▄▄▄▄                      ///////////
#///////////            ▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄                   ///////////
#///////////           ▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄                 ///////////
#///////////           ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄               ///////////
#///////////         ▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌              ///////////
#///////////         ▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐   ▄▄         ///////////
#///////////         ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▄█▒█         ///////////
#///////////         ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▀          ///////////
#///////////         ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀            ///////////
#///////////         ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌             ///////////
#///////////          ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐              ///////////
#///////////          ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌              ///////////
#///////////           ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐               ///////////
#///////////           ▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌               ///////////
#///////////             ▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀                 ///////////
#///////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////

print (''' \033[92m	
   =====================================================================
   =   _____            _   _         _____           _           _    =
   =  / ____|          | | (_)       |  __ \         (_)         | |   =
   = | |     __ _ _ __ | |_ _ _ __   | |__) | __ ___  _  ___  ___| |_  =
   = | |    / _` | '_ \| __| | '_ \  |  ___/ '__/ _ \| |/ _ \/ __| __| =
   = | |___| (_| | | | | |_| | |_) | | |   | | | (_) | |  __/ (__| |_  =
   =  \_____\__,_|_| |_|\__|_| .__/  |_|   |_|  \___/| |\___|\___|\__| =
   =                         | |                    _/ |               =
   =                         |_|                   |__/                =
   =====================================================================  
                           Cantip Project v1.0
   =====================================================================                                              			     
	
	Selamat datang di Cantip Project
	Jangan mengaku jadi kakak cantip :)
	Script ini saya buat untuk rasa terimakasih ke kakak cantip 

Apakah Kamu Kakak Cantip?
Pilih Option :
1.Bukan
2.Ya, Saya Kakak Cantip
3.Keluar\033[0m''')
option=int(input("Pilih menu >:"))

if option==1:
	  print('''\033[92mSudah kuduga kalau kamu bukan kakak cantip. yaudah kita cuma sebatas teman.\033[0m''') 
	  
elif option==2:
	  print('''\033[92m
		   	 ___
            (___)
     ____
   _\___ \  |\_/|
  \     \ \/ , , \ ___
   \__   \ \ ="= //|||\
    
    |===  \/____)_)||||
    \______|    | |||||
        _/_|  | | =====
       (_/  \_)_) 
 	  
Jika kamu adalah kakak cantip, pastikan tau tanggal lahir saya.
Pilih Option : 
1. 31012000
2. 31022000
3. 31032000
4. 31042000
5. 31052000
6. 31062000
7. 31072000
8. 31082000
9. 31092000
10. 31102000
11. 31112000
12. 31122000\033[0m''')
	  tanggal_lahir=31082000
	  option2=int(input("Pilih menu >:"))
	  if option2==1:
		  print("Maaf kamu salah, kamu bukan kakak cantip huhu... lain kali jangan ngaku ngaku ya kaowkoa")
	  elif option2==2:
		  print("Maaf kamu salahh, kamu bukan kakak cantip huhu... lain kali jangan ngaku ngaku ya kaowkoa")
	  elif option2==3:
		  print("Maaf kamu salahh lagi, kamu bukan kakak cantip huhu... lain kali jangan ngaku ngaku ya kaowkoa")
	  elif option2==4:
		  print("Maaf kamu salahh terus, kamu bukan kakak cantip huhu... lain kali jangan ngaku ngaku ya kaowkoa")
	  elif option2==5:
		  print("Maaf kamu salahh teruss, kamu bukan kakak cantip huhu... lain kali jangan ngaku ngaku ya kaowkoa")
	  elif option2==6:
		  print("Maaf kamu salahh terusss, kamu bukan kakak cantip jangan maksa... lain kali jangan ngaku ngaku ya kaowkoa")
	  elif option2==7:
		  print("Maaf kamu salahh teruusss, udahlah kamu bukan kakak cantip jingga jadi males ... lain kali jangan ngaku ngaku ya kaowkoa")
	  elif option2==8:
		  hasil=tanggal_lahir
		  print(''' \033[92mBenar kamu adalah kakak cantip, tanggal lahir saya adalah 31082000
Jaga kesehatan yaa kakak!! entar kalo sakit akunya jadi sedih kak huhu
Oh iya ada sedikit kejutan nih, dilihat ya https://editor.zyro.com/YX443Nl777f9kQlq/preview \033[0m''')
	  elif option2==9:
		  print("Tuhkann kamu masih salahh, udahlah kamu bukan kakak cantip jingga jadi males jangan maksa teruss... lain kali jangan ngaku ngaku ya kaowkoa")	
	  elif option2==10:
		  print("Salahh udahlah jingga sudah males... lain kali jangan ngaku ngaku ya kaowkoa")
	  elif option2==11:
		  print("Masih Salahh gausah maksa jadi kakak cantip deh jingga jadi males... lain kali jangan ngaku ngaku ya kaowkoa")
	  elif option2==12:
		  print(''' \033[92mLain kali jangan ngaku ngaku jadi kakak cantip ya jingga sudah males kaowkoa \033[0m''')   
	  else:
		  print("Menu salah!") 	  	    
elif option==3:
	 exit()
else:
	print("Menu salah!!")
