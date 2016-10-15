FROM python:2.7-onbuild
MAINTAINER nugnes.alberto@gmail.com

RUN apt-get update && apt-get install cron -y
# CMD ["python", "./main.py"]

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/hello-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

RUN crontab /etc/cron.d/hello-cron
RUN chmod +x /usr/src/app/main.py

WORKDIR /usr/src/app

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log
