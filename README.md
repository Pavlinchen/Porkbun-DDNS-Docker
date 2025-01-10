#

## Porkbun DDNS Docker

### This Repository wraps the (now legacy, but as of 01/2025 still working) [Porkbun dynamic DNS (DDNS) Python API](https://github.com/porkbundomains/porkbun-dynamic-dns-python) into a lightweight, multiplattform [docker image](https://hub.docker.com/r/pavlinchen/porkbun-ddns)

### Table of contents

1. [Usage](#usage)
   - [Docker compose](#docker-compose)
   - [CLI](#cli)
2. [Building from source](#building-from-source)
3. [Environment variables](#environment-variables)

## Usage

For an in depth explanation on how the API works or how to get started, please refer to the [official getting started guide](https://kb.porkbun.com/article/190-getting-started-with-the-porkbun-dns-api), the [official API documentation](https://porkbun.com/api/json/v3/documentation) and/or the wrapped [official porkbun repository](https://github.com/porkbundomains/porkbun-dynamic-dns-python).

### Docker compose

```docker
version: "3"
services:
    porkbun-ddns:
        image: pavlinchen/porkbun-ddns
        container_name: porkbun-ddns
        restart: always
        pull_policy: always
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
-e APIKey="<YourAPIKey>" \
-e SecretAPIKey="<YourSecretAPIKey>" \
-e Domain="<YourDomain>" \
-e Schedule="<YourSchedule (in cron syntax)>" \
-e TZ="<YourTimezone>" \
--pull=always \
--restart always \
--name porkbun-ddns \
pavlinchen/porkbun-ddns
```

### Building from source

> [!TIP]
> Please note, that the pull=always policy needs to be removed (or changed) in order to run the local build.</br>
> Furthermore the tag for your container ("pavlinchen/porkbun-ddns" in the examples above) needs to be adjusted when running the locally built container to the tag that is set with '-t' here ("porkbun-ddns" below).

```bash
git clone https://github.com/Pavlinchen/Porkbun-DDNS-Docker
cd Porkbun-DDNS-Docker
docker build . -t porkbun-ddns
```

### Environment variables

| Argument | description | example | default | required
|-|-|-|-|-
| `APIKey` | The API key provided to you by porkbun | pk1_abcdef123456 | None | yes
| `SecretAPIKey` | The secret API key provided to you by porkbun | sk1_abcdef123456 | None | yes
| `Domain` | The Domain you want to map to your IP adress, as seen [here](https://github.com/porkbundomains/porkbun-dynamic-dns-python#running-the-client)| google.com domains </br> (would be domains.google.com) | None | yes
| `Schedule` | Schedule to execute the script to sync DNS A records with your IP address [in cron syntax](https://crontab.guru/) | */10 * * * * </br> (every 10 minutes) | */5 * * * * </br> (every 5 minutes) | no
| `TZ` | Your Timezone  in [tz database format](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) name </br> (only really needed, if used in schedule) | Europe/Berlin | UTC | no
