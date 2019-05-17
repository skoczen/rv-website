# Web project

This website hosts and will host several projects, including:

## Number reader

Users can upload a picture of a hand-written number, and a neural network trained on the MNIST dataset will read the image, and show the number.


## Server Setup and Admin

### Setting up a new server
1. Create a blank image, ssh in.
2. Run the following commands:

```bash
curl -O https://raw.githubusercontent.com/skoczen/rv-website/master/bin/bootstrap_server.sh
chmod +x bootstrap_server.sh
./bootstrap_server.sh
```

3. Fill out the `~/code/website/.env` file.


### Setting up the project

```bash
cd ~/code/website
export $(cat .env | xargs)
docker network create $WEBSITE_DOMAIN 
docker-compose up -d
```

### Updating to the latest code

```bash
cd ~/code/website
git pull
```

### Re-building the project

If requirements.txt has changed or there are other significant changes:

```bash
docker-compose down
docker-compose build
docker-compose up -d
```


### Viewing logs

```bash
cd ~/code/website
docker-compose logs -f --tail=50
```

## SSH into the docker container
```bash
docker-compose run  --rm --label traefik.enable=false project bash
```
