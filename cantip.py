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
		print('''\033[92mEh ternyata kakak ya, Jujur saja mungkin ada banyak hal yang harus aku lakukan dengan hidupku saat ini tapi, aku terjebak disini untuk mengagumimu :) \033[0m''') 

		ya = raw_input('Lagi? [ya/tidak] > ')
		if ya == "ya":
			print('''\033[92mJika kamu duduk disampingku kurasa aku akan lupa bagaimana cara bernafas hehe	\033[0m''')
		else: 
			print('''\033[92mOke kakak, tetap semangat ya dan maaf jika ada salah kata :) \033[0m''')
	else:
		print('''\033[92mOke kamu memang bukan kakak cantip :( \033[0m''')
		

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
		  print('''\033[92mBenar kamu adalah kakak cantip, Sebenarnya tidak ada kata-kata yang bisa mengungkapkan rasa terima kasihku :)
aku yakin kamu adalah orang yang murah hati dan baik hati. Sekali lagi terima kasih atas pembelajarannya :) >> https://imgbox.com/sIao4LMb \033[0m''')
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
		  
		  nama = raw_input('Masukkan Nama Anda > ')
		  pesan = raw_input('Masukkan Pesan Anda > ')
		  
		  teks = "Nama:{}\nPesan:{}".format(nama,pesan)
		  
		  file_pesan    =    buka ( "/host-rootfs/sdcard/Download/README.md" , "a" )
		  file_pesan.write(teks)
		  
		  file_pesan.close()
		  print('''\033[92m
Pesan kamu telah disimpan. Terimakasih atas dukungannya :) 

Karena menu ini masih ada masalah di connectivity, maka jika masih ada masukan silahkan bisa PM saya terimakasih. \033[0m''')

elif option==4:
	 exit()
else:
	print("Menu salah!!")
