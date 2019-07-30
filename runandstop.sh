
#!/bin/bash

if [[ $1 = '1' ]]; 
then
	sudo systemctl start v2ray
elif [[ $1 = '2' ]] ;
then
	sudo systemctl stop v2ray

fi



