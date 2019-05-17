#!/bin/sh
apt update
apt install git ocaml-nox unzip make python3 python3-pip python3-venv snapd -y
pip3 install --upgrade pip

# Install Unison
mkdir -p src
mkdir -p src/unison
cd src/unison
wget -o# https://github.com/bcpierce00/unison/archive/v2.51.2.zip
unzip v2.51.2
cd unison-2.51.2
make UISTYLE=text
cp src/unison /usr/bin/unison
cd ..
wget https://github.com/TentativeConvert/Syndicator/raw/master/unison-binaries/unison-fsmonitor
cp unison-fsmonitor /usr/bin/unison-fsmonitor
chmod u+x /usr/bin/unison
chmod u+x /usr/bin/unison-fsmonitor
cd
mkdir code


# Clone codebase
mkdir -p code
cd code
# git clone https://github.com/ronanvenkat/website
git clone https://github.com/skoczen/rv-website.git website

# Set up environment
cd website
touch .env

cd ~