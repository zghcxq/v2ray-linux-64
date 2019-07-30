import dealv2raylink
import os

def main():
	while 1 :	    
		print ("                                         ")
		print ("|---------------------------------------|")
		print ("|        v2ray-script                   |")
		print ("|        author:dawn                    |")
		print ("|---------------------------------------|")
		print ("| 1. inputv2raylink                     |")
		print ("| 2.choosev2raynode                     |")
		print ("| 3.run service                         |")
		print ("| 4.stop service                        |")
		print ("| 5.init  software                      |")
		print ("| 6.remove v2ray  software              |")
		print ("|---------------------------------------|")
			
		num = int (input("please enter a number(represent quit is zero)  : "))
	
		if num == 1:
			s = input("please enter v2ray node : ")
			is_vmess = s.find('vmess://')
			if is_vmess != -1:
				vmess = s[is_vmess:].strip()
				
				dealv2raylink.decode_v2ray(vmess)
			else:
				print("v2ray node is worse !!!")
		elif num == 2:
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
			
	
		elif num == 3:
			os.system("bash runandstop.sh 1")
 
		elif num == 4:
			os.system("bash runandstop.sh 2")
		elif num == 5:
			os.system("bash init.sh")
		elif num == 6:
			os.system("bash rmv2ray.sh")

		elif num == 0:
			break;

main()

