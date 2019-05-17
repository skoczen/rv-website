apt update
do-release-upgrade
apt install git unzip make python3 python3-pip python3-venv snapd docker-compose -y
pip3 install --upgrade pip

# Clone codebase
git clone https://github.com/ronanvenkat/website

# Set up environment
cd website
touch .env