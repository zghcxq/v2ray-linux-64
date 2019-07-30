
import dlbase64


				
def Analyze(s):


	spilted = s.split(',')  
	
	address = spilted[0].split(':') 
	alterId = spilted[1].split(':')
	alterId = alterId[1].split('\"')
	Host = spilted[2].split(':') 
	id = spilted[3].split(':') 
	network = spilted[4].split(':') 
	path = spilted[5].split(':') 
	port = spilted[6].split(':') 
	port = port[1].split('\"') 
	security = spilted[8].split(':') 
	type = spilted[9].split(':') 


	confige_file = open("config/config.json","r")
	solvethesign = len(confige_file.read())
	confige_file.close()

	confige_file = open("config/config.json", "a")
	employee_file = open("config/configmode1", "r")
	for employee in employee_file.readlines():		
		vimconfig = employee.split('#')
	vimconfig[1] = "\"address\":" +	address[1]
	vimconfig[5] = "\"alterId\":"+alterId[1]
	vimconfig[7] = "\"id\":"+id[1]
	vimconfig[9] = "\"network\":"+network[1]
	vimconfig[3] = "\"port\":"+port[1]
	vimconfig[11] = "\"security\":"+security[1]
	if  "\"tls\""==security[1]:
		vimconfig[12] = ",\"tlssettings\":{\"allowInsecure\":true,\"serverName\":\"\"}"
	if "\"ws\"" == network[1]:
		vimconfig[13] = ",\"wssettings\":{\"connectionReuse\":true,\"headers\":{"
		vimconfig[14] = "\"Host\":"+Host[1]
		vimconfig[15] = "},"
		vimconfig[16] = "\"path\":"+path[1] +"}"
	vimconfig[18] = "\"type\":"+type[1]
	configlist = []
	for numb in range(0,len(vimconfig)):	
		configlist.append(vimconfig[numb])
	resultc = ""
	solvethesameline = len(vimconfig) -1
	for configlen in range(0,solvethesameline):
		resultc= resultc + configlist[configlen]
	if solvethesign == 0:
		confige_file.write(resultc)
	else:	
		confige_file.write("//"+resultc)

	
	confige_file.close()
	employee_file.close()
		
	






