import os
import json

def fillConfig(APIKEY, SECRETAPIKEY):
    with open('config.json', 'r') as f:
        config = json.load(f)

    config.update({'apikey':APIKEY, 
    'secretapikey':SECRETAPIKEY})

    with open('config.json', 'w') as f:
        json.dump(config, f)


def fillCron(DOMAIN, SCHEDULE='*/5 * * * *'):
    with open('/porkbun/crontab.txt', 'w') as c:
        c.write(f'{SCHEDULE} python3 /porkbun/porkbun-ddns.py /porkbun/config.json {DOMAIN}\n')


fillConfig( APIKEY = str(os.environ['APIKey']),
            SECRETAPIKEY = str(os.environ['SecretAPIKey']))

#try to avoid errors when no schedule is provided
try:
    fillCron(   SCHEDULE=str(os.environ['Schedule']),
                DOMAIN=str(os.environ['Domain']).replace('*', '"*"'))
except:
    fillCron(DOMAIN=str(os.environ['Domain']).replace('*', '"*"'))

#installing needed modules (has to be done in file, otherwise GitHub actions automatic build will fail)
os.system("pip install -r requirements.txt --no-cache-dir")

#declare /porkbun/crontab.txt as crontab file
os.system("crontab /porkbun/crontab.txt")

#run crontab in foreground to actually execute & keep container alive
os.system("crond -f")
