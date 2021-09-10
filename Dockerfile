FROM python:3.7
RUN apt-get update && apt-get -y install cron vim

# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Magic happens
RUN apt-get install -y google-chrome-stable

WORKDIR /app
COPY crontab /etc/cron.d/crontab
COPY ./* /app/
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab
RUN python -m pip install -U pip
RUN pip install -r requirements.txt
RUN apt-get install -y libnss3
ENV DISPLAY=:99


# run crond as main process of container
CMD ["cron", "-f"]
