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


print ('''\033[92m
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
                             Author : Jingga
   =====================================================================                                              			     
	
	Selamat datang di Cantip Project
	Jangan mengaku jadi kakak cantip ya :)
	Script ini saya buat untuk rasa terimakasih ke kakak cantip 

Apakah Kamu Kakak Cantip?
Pilih Option :
1.Bukan
2.Ya, Saya Kakak Cantip
3.Pesan
4.Keluar\033[0m''')
option=int(input("Pilih menu > "))

if option==1:
	print('''\033[92mSudah kuduga kalau kamu bukan kakak cantip. yasudah kita berteman saja mwehehe.
Jadi Siapakah kamu?\033[0m''')
	nama_yang_tersedia = ['Savira','Savira Agnisa','Agnisa','savira','savira agnisa', 'agnisa']
	nama_yang_dicari = raw_input('Masukkan Nama Anda > ')
	
	if (nama_yang_dicari in nama_yang_tersedia):
		print('''\033[92mAku ingin mengakui dosa. Tapi jangan marah ya? Maaf sebelumnya. Tadi malam aku mimpi bertemu kamu... 
Setelah bangun, akankah mimpiku menjadi kenyataan? hehe\033[0m''')
	else:
		print('''\033[92mOke kamu memang bukan kakak cantip. \033[0m''')

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
 	  
Jika kamu adalah kakak cantip, pasti tau tanggal berapa kakak cantip lahir??
Pilih Option : 
1. 18-01-2000
2. 24-03-2000
3. 19-09-2000
4. 28-05-1999
5. 15-11-1999
6. 22-02-1998
7. 17-04-1998
8. 19-08-1998
9. 11-12-1998
10. 31-01-1997
11. 31-08-1997
12. 14-12-1997
00. Keluar\033[0m''')
	  tanggal_lahir=31082000
	  option2=int(input("Pilih menu > "))
	  if option2==1:
		  print('''\033[92mSalah, kakak cantip tidak lahir pada tanggal 18-01-2000 \033[0m''')
	  elif option2==2:
		  print('''\033[92mMaaf salah, kakak cantip tidak lahir pada tanggal 24-03-2000 \033[0m''')
	  elif option2==3:
		  print('''\033[92mMaaf kamu masih salah, kakak cantip tidak lahir pada tanggal 19-09-2000 \033[0m''')
	  elif option2==4:
		  print('''\033[92mMaaf kamu salah lagi, kakak cantip tidak lahir pada tanggal 28-05-1999 \033[0m''')
	  elif option2==5:
		  print('''\033[92mMaaf kamu salah terus, kakak cantip tidak lahir pada tanggal 15-11-1998 \033[0m''')
	  elif option2==6:
		  print('''\033[92mMaaf kamu salahh terusss, kakak cantip tidak lahir pada tanggal 22-02-1998 \033[0m''')
	  elif option2==7:
		  print('''\033[92mMaaf kamu salahh teruusss, kakak cantip tidak lahir pada tanggal 17-04-1998 \033[0m''')
	  elif option2==8:
		  hasil=tanggal_lahir
		  print('''\033[92mBenar kamu adalah kakak cantip, Jaga kesehatan yaa kakak!! entar kalo sakit aku jadi sedih kak huhu
Sedikit rasa Terimakasih saya untuk kalian https://imgbox.com/zWaQkBmA \033[0m''')
	  elif option2==9:
		  print('''\033[92mTuhkan kamu masih salah, kakak cantip tidak lahir pada tanggal 11-12-1998 \033[0m''')
	  elif option2==10:
		  print('''\033[92mTuhkan kamu salah lagi, kakak cantip tidak lahir pada tanggal 11-12-1998 \033[0m''')
	  elif option2==11:
		  print('''\033[92mTuhkan kamu salah terus, kakak cantip tidak lahir pada tanggal 31-08-1997 \033[0m''')
	  elif option2==12:
		  print('''\033[92mTuhkan kamu salah terus menerus, kakak cantip tidak lahir pada tanggal 14-12-1997 \033[0m''') 
	  elif option2==0:
		  exit()
	  else:
		  print("Menu salah!") 	  	    
elif option==3:
		  print('''\033[92mPesan yang ingin disampaikan untuk pembuat Program sederhana ini :)\033[0m''')
		  
		  raw_input('Masukkan Nama Anda > ')
		  raw_input('Masukkan Pesan Anda > ')
		  print('''\033[92m
Pesan kamu telah disimpan. Terimakasih atas dukungannya :) 

Karena menu ini masih dalam perbaikan. Jika masih ada masukan silahkan bisa PM saya terimakasih. \033[0m''')

elif option==4:
	 exit()
else:
	print("Menu salah!!")
