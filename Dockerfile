FROM python:3-alpine

WORKDIR /porkbun

# needed to download the used scripts
RUN apk add curl

COPY main.py main.py
COPY requirements.txt requirements.txt 

# getting used scripts from https://github.com/porkbundomains/porkbun-dynamic-dns-python
RUN curl https://raw.githubusercontent.com/porkbundomains/porkbun-dynamic-dns-python/main/porkbun-ddns.py -o porkbun-ddns.py
RUN curl https://raw.githubusercontent.com/porkbundomains/porkbun-dynamic-dns-python/main/config.json.example -o config.json

#installing additional needed modules
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]