#!/bin/sh
apt update
apt install git unzip make python3 python3-pip python3-venv snapd -y
pip3 install --upgrade pip

# Clone codebase
mkdir -p code
cd code
# git clone https://github.com/ronanvenkat/website
git clone https://github.com/skoczen/rv-website.git website

# Set up environment
# cd website
cd rv-website
touch .env

cd ~