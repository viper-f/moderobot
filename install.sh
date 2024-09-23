apt update
apt install sudo
apt install wget -y
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb -y
sudo apt install python3 python3-venv -y
cd moderobot
python3 -m venv ./.venv
.venv/bin/pip install -r requirements.txt
