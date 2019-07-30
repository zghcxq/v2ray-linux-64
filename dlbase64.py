import base64

def debase64_2(a):
	

	
	a = a.encode("UTF-8")
	missing_padding = 4 - len(a) % 4
	if missing_padding:
		a += b'=' * missing_padding
	b = base64.b64decode(a)
	return b 
	


