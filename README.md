# Porkbun DDNS Docker

## This is the [Porkbun DDNS Python API](https://github.com/porkbundomains/porkbun-dynamic-dns-python) wrapped into a lightweight docker image.

### Table of contents:
1. [Usage](#usage)
   - [Docker Compose](#docker-compose)
   - [CLI](#cli)
2. [Build from source](#build-from-source)
3. [Environment Variables](#environment-variables)


## Usage: 
For an in depth explanation on how the API works or how to get started, please consider the [official getting started guide](https://kb.porkbun.com/article/190-getting-started-with-the-porkbun-dns-api), the [official porkbun repository](https://github.com/porkbundomains/porkbun-dynamic-dns-python) or the [official API documentation](https://porkbun.com/api/json/v3/documentation).

### Docker Compose
```docker
version: "3"
services:
    porkbunddns:
        image: pavlinchen/porkbun-ddns-docker
        container_name: porkbun-ddns
        environment:
            APIKey: <YourAPIKey>
            SecretAPIKey: <YourSecretAPIKey>
            Domain: <YourDomain>
            Schedule: <YourSchedule (in cron syntax)> #optional
            TZ: <YourTimezone> #optional
```

### CLI
```docker
docker run -d \
-e APIKey='<YourAPIKey>' \
-e SecretAPIKey='<YourSecretAPIKey>' \
-e Domain='<YourDomain>' \
-e Schedule='<YourSchedule (cron syntax)>' \
-e TZ='<YourTimezone>' \
--pull=always \
--name porkbun-ddns \
pavlinchen/porkbun-ddns-docker
```

### Build from source:
```bash
git clone https://github.com/Pavlinchen/Porkbun-DDNS-Docker
cd Porkbun-DDNS-Docker
docker build . -t porkbunddns
```

### Environment Variables
| Argument | description | example | default | optional
|-|-|-|-|-|
| `APIKey` | The API key provided to you by porkbun | | None | no |
| `SecretAPIKey` | The secret API key provided to you by porkbun | | None | no |
| `Domain` | The Domain you want to map to your IP adress, as seen [here](https://github.com/porkbundomains/porkbun-dynamic-dns-python#running-the-client)| google.com domains </br> (would be domains.google.com) | None | no |
| `Schedule` | Schedule to execute the script to sync DNS A records with your IP address in cron format | */10 * * * * </br> (every 10 minutes) | */5 * * * * </br> (every 5 minutes) | yes |
| `TZ` | Your Timezone  as [tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) name </br> (only really needed, if used in schedule) | Europe/Berlin | UTC | yes |
