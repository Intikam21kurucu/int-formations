#usr/bin/int-info/ python3
import os
import time
from pyfiglet import Figlet
import sys
import time

def loading(text):
    for i in range(10):
        sys.stdout.write("\r" + "[+] " + text + "." * i)
        time.sleep(0.1)
        sys.stdout.flush()
    print("\033[92m" + "\r" + "[+] " + text + "....................OK!\033[0m")

ascii = """ ⠀			 
	⠀	⠀			⢀⣤⣶⣶⠖⠛⠛⠲⣶⣶⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣇⣤⠶⠛⣛⣉⣙⡛⠛⢶⣄⣸⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣿⣿⣿⡟⢁⣴⣿⣿⣿⣿⣿⣿⣦⡈⢿⣿⣿⣿⣀⡀⠀⠀⠀
⠀⠀⢠⣴⣿⣿⣿⣿⡟⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢿⣿⣿⣿⣿⣦⡄⠀
⠀⣴⣿⣿⡿⠿⢛⣻⡇⢸⡟⠻⣿⣿⣿⣿⣿⡿⠟⢻⡇⣸⣛⡛⠿⣿⣿⣿⠀
⢸⣿⡿⠋⠀⠀⢸⣿⣿⡜⢧⣄⣀⣉⡿⣿⣉⣀⣠⣼⢁⣿⣿⡇⠀⠀⠙⢿⡆
⣿⣿⠁⠀⠀⠀⠈⣿⣿⡇⣿⡿⠛⣿⣵⣮⣿⡟⢻⡿⢨⣿⣿⠀⠀⠀⠀⠈⣿
⢿⡟⠀⠀⠀⠀⠀⠘⣿⣷⣤⣄⡀⣿⣿⣿⣿⢁⣤⣶⣿⣿⠃⠀⠀⠀⠀⠀⠘⠇⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡇⢿⣿⣿⣿⢸⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⢩⣦⣘⡘⠋⣛⣸⡍⠁⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀
⠀⠀⠘⢿⣷⣤⣤⣄⣤⣤⣶⣿⣿⣿⡿⢿⣿⣿⣿⣷⣤⣤⣠⣤⣴⣾⡿⠁	⠀
⠀⠀⠀⠀⠉⠛⠿⠿⠿⡿⠿⠿⠛⠉⠀⠀⠉⠛⠿⠿⣿⠿⠿⠿⠛⠉⠀⠀⠀⠀"""

# HTML içeriğini yazdırın
print(ascii + """Hoşgeldin! | HELLO!
SOCIAL MEDIA INFORMATION GATHERING
-------------------------------------------------------------------
SOSYAL MEDYA HESABI BİLGİSİ ALMA""")
print("-----------------------------------------------------------------")

print(" ")
print(" ")

def open():
	k = input("Do you want to continue[Y/N]")
	if k == "Y" or "y":
		print("ok!")
		loading("no exiting")
	if k == "N" or "n":
		loading("exiting......")
		time.sleep(3)
		os.system("exit")
open()
print("""İnformation Gathering Tools:
	           Youtube							
    ╭──╯			  ╰──╮								
İp İnfos	              	Youtubeinformations

				OTHER
	                 |
	                └─ SOCİAL İnformations 
	                
	                
	                WE ARE WORKİNG.....

1-)Youtube İnformation
2-)ip İnformation
3-)Social İnformation
""")

user_input = input("""
┌──(İntikam21@Termux[İnformations]
└─$""")
while True:
	if user_input == "1":
		os.system("python3 youtubeinfo.py")
	if user_input == "2":
		os.system("python3 ipinfo.py")
	if user_input == "3":
		os.system("python3 socialhacks.py")
	if user_input == "help":
		print("""İnformation Gathering Tools:
	           Youtube							
    ╭──╯			  ╰──╮								
İp İnfos	              	Youtubeinformations

				OTHER
	                 |
	                └─ SOCİAL İnformations 
	                
	                
	                WE ARE WORKİNG.....

1-)Youtube İnformation
2-)ip İnformation
3-)Social İnformation
""")
	if user_input == "exit":
		loading("exiting..............")
		time.sleep("3")
		break
		os.system("exit")	
else:
	os.system(user_input)
