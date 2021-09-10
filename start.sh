wget -O ./chromedriver.zip https://chromedriver.storage.googleapis.com/93.0.4577.63/chromedriver_linux64.zip
unzip chromedriver.zip 
docker-compose down
docker-compose up -d --build --force-recreate python-cron
