# Update apt
apt-get -y update

# Install pigpio
apt-get -y install pigpio
systemctl enable pigpiod
systemctl start pigpiod

# Create virtual env and install requirements
apt-get -y install python3-venv
python3 -m venv venv
venv/bin/activate/python3 -m pip install -r requirements.txt

# Enable and run poseidon service
cp poseidon.service /etc/systemd/system 
systemctl enable poseidon
systemctl start poseidon
