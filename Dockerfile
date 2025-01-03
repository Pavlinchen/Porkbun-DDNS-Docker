FROM python:3.9-alpine

WORKDIR /porkbun

COPY main.py main.py
COPY requirements.txt requirements.txt 

#installing pip (needed for requirements)
RUN apk add py3-pip --no-cache

# installing curl to get scripts from Porkbun GitHub https://github.com/porkbundomains/porkbun-dynamic-dns-python
RUN apk add curl --no-cache
RUN curl https://raw.githubusercontent.com/porkbundomains/porkbun-dynamic-dns-python/main/porkbun-ddns.py -o porkbun-ddns.py
RUN curl https://raw.githubusercontent.com/porkbundomains/porkbun-dynamic-dns-python/main/config.json.example -o config.json

#removing curl to save space
RUN apk del curl

ENTRYPOINT ["python", "main.py"]