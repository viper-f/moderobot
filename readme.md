ssh username@server_ip  
-- enter password  
apt update  
apt install nano git -y  
git clone https://github.com/viper-f/moderobot.git  
./moderobot/install.sh  
cd config  
cp config_default.json config.json  
nano config.json  
-- change base_url to the base url of the forum  
-- To save the file: Ctrl + O, Enter  
-- To close the file: Ctrl + X  
