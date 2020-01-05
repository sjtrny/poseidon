# Update apt
apt-get update

# Install pigpio
apt-get install pigpio
systemctl enable pigpiod
systemctl start pigpiod

# Create virtual env and install requirements
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt

# Enable and run poseidon service
cp poseidon.service /etc/systemd/system 
systemctl enable poseidon
systemctl start poseidon
