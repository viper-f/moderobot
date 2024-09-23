apt update
apt install sudo

# Install Chrome and Chrove Driver
apt install wget -y
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb -y
sudo apt install python3 python3-venv libaugeas0 -y  

# Install SSL certbot
sudo python3 -m venv /opt/certbot/  
sudo /opt/certbot/bin/pip install --upgrade pip
sudo /opt/certbot/bin/pip install certbot
sudo ln -s /opt/certbot/bin/certbot /usr/bin/certbot
sudo certbot certonly --standalone #todo
echo "0 0,12 * * * root /opt/certbot/bin/python -c 'import random; import time; time.sleep(random.random() * 3600)' && sudo certbot renew -q" | sudo tee -a /etc/crontab > /dev/null

# Install dependencies
cd moderobot
python3 -m venv ./.venv
.venv/bin/pip install -r requirements.txt
