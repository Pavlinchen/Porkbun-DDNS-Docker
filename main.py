import os
import json

CRONTAB_FILE = '/porkbun/crontab.txt'

def fillConfig(APIKEY, SECRETAPIKEY):
    with open('config.json', 'r') as f:
        config = json.load(f)

    config.update({'apikey':APIKEY, 
    'secretapikey':SECRETAPIKEY})

    with open('config.json', 'w') as f:
        json.dump(config, f)


def fillCron(DOMAIN, SCHEDULE='*/5 * * * *'):
    with open(CRONTAB_FILE, 'a') as c:
        c.write(f'### start entries from porkbun ddns-docker container ###\n')
        c.write(f'{SCHEDULE} echo execution @ $(date +"%Y-%m-%d %H:%M:%S"):\n')
        c.write(f'{SCHEDULE} python3 /porkbun/porkbun-ddns.py /porkbun/config.json {DOMAIN}\n')
        c.write(f'### end entries from porkbun ddns-docker container ###\n')


# installing needed modules (has to be done in file, otherwise GitHub actions automatic build will fail)
os.system('echo === Installing dependencies...')
os.system('pip install -r requirements.txt --root-user-action=ignore --no-cache-dir')

fillConfig( APIKEY = str(os.environ['APIKey']),
            SECRETAPIKEY = str(os.environ['SecretAPIKey']))

# try to set schedule from environment variable
# replacing * with "*", as the " are needed by porkbun API if * is used
try:
    fillCron(   SCHEDULE=str(os.environ['Schedule']),
                DOMAIN=str(os.environ['Domain']).replace('*', '"*"'))
except:
    fillCron(DOMAIN=str(os.environ['Domain']).replace('*', '"*"'))

# declare /porkbun/crontab.txt as file to be executed by crontab 
os.system(f'crontab {CRONTAB_FILE}')

os.system(f'echo === Setup finished, cron ready and waiting!')

# run crontab in foreground to actually execute & keep container alive
os.system('crond -f')