import dealv2raylink
import os
import sys

#print(sys.argv[0])
#print(sys.argv[1])
def help():
		print ("V2ray-script version 1.0.1  ( author:dawn)")
		print("usage: python3 main.py -h  [help]")
		print("usage: python3 main.py -v  [vmessNode]")
		print("usage: python3 main.py -l  [list of ssrNode]")
		print("usage: python3 main.py -r  [run]")
		print("usage: python3 main.py -s  [stop]")
		print("usage: python3 main.py- i  [install v2ray]")
		print("usage: python3 main.py -rm  [remove v2ray]")
def main():
		
	if len(sys.argv)==1:	
		help()
	
	elif len(sys.argv)==2:
		if sys.argv[1] == "-h":
			help()
		if sys.argv[1] == "-v":
				s = input("please enter vmessNode : ")
				is_vmess = s.find('vmess://')
				if is_vmess != -1:
					vmess = s[is_vmess:].strip()
					dealv2raylink.decode_v2ray(vmess)
				else:
					print("v2ray node is worse !!!")
			
		if sys.argv[1] == "-l":
			employee_file = open("config/config.json", "r") 
 
			for employee in employee_file.readlines():
				spilted = employee.split('//')  
			print ("-----------------------------")
			print ("|     v2ray node              |")
			i=0
			for ipaddresschoose in range(0,len(spilted)):
				i = i+1
				solverange = ipaddresschoose
				ipaddress = spilted[solverange].split('"address":"')
				ipaddress = ipaddress[1].split('"')
				print ("-----------------------------")
				print ("* "+str(i)+ ". "+ipaddress[0] + "        ")
	
			print ("-----------------------------")    
			employee_file.close()
			
			#userchoosenode = employee.split('//')
			while 1:
				choosenodenum = int (input ("please enter a number to choice a ssr node :"))
				testvalue = 0
				
				employee_filebychoice = open("/etc/v2ray/config.json", "w")
				for ipaddresschoose in range(0,len(spilted)):
					ipaddresschoose = ipaddresschoose + 1
					if choosenodenum == ipaddresschoose:    
						employee_filebychoice.write(spilted[choosenodenum-1])
						testvalue = 1;
				if testvalue == 1 :
					print("	choice success ")
					break;
				else :
					print("	Invail value")
			employee_filebychoice.close()
		
		if sys.argv[1] == "-r":
			os.system("bash runandstop.sh 1")
 
		if sys.argv[1] == "-s":
			os.system("bash runandstop.sh 2")
		if sys.argv[1] == "-i":
			os.system("bash init.sh")
		if sys.argv[1] == "-rm":
			os.system("bash rmv2ray.sh")


main()

