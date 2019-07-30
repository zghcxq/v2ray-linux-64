sudo mkdir  -p /etc/v2ray /usr/bin/v2ray /var/log/v2ray 
sudo chmod +x v2ray v2ctl 
sudo cp -r v2ray v2ctl geoip.dat geosite.dat -t /usr/bin/v2ray 
sudo touch /etc/v2ray/config.json 
sudo cp -r systemd/v2ray.service /etc/systemd/system/
sudo chmod 777 /etc/v2ray/config.json
