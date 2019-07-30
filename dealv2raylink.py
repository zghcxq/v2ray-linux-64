
# -*- coding: utf-8 -*-

import base64


import configcreat 


def base64decode(s):
    transtab = str.maketrans('-_', '+/')
    s = s.translate(transtab)
    if len(s) % 4 != 0:
    	s = s + (4 - len(s) % 4)*'='
    return base64.urlsafe_b64decode(s.encode())




def decode_v2ray(vmess):
    

    
    first_b = base64decode(vmess[8:])
    
    print(first_b.decode())

    configcreat.Analyze(first_b.decode())


    

 









	






