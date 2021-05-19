#Dockerfile
FROM python:3.6
RUN mkdir /application
WORKDIR "/application"
# Upgrade pip
RUN pip install --upgrade pip
# Update
RUN apt-get update \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
ADD requirements.txt /application/
ADD src/script.py /application/
RUN pip install -r /application/requirements.txt
CMD [ "python", "main.py" ]