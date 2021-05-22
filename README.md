<p align="center">
  <img src="./resources/extras/cf1.jpg" alt="Infinato Logo">
</p>
<h1 align="center">
  <b>Infinato - UserBot</b>
</h1>

<b>A SIMPLE TELEGRAM USERBOT WITH TELETHON</b>   

[![Stars](https://img.shields.io/github/stars/coolfoolunidentifiedhacker/INFINATO-UB?style=flat-square&color=yellow)](https://github.com/coolfoolunidentifiedhacker/INFINATO-UB/stargazers)
[![Forks](https://img.shields.io/github/forks/coolfoolunidentifiedhacker/INFINATO-UB?style=flat-square&color=orange)](https://github.com/coolfoolunidentifiedhacker/INFINATO-UB/fork)
[![Size](https://img.shields.io/github/repo-size/coolfoolunidentifiedhacker/INFINATO-UB?style=flat-square&color=green)](https://github.com/coolfoolunidentifiedhacker/INFINATO-UB/)   
[![Python](https://img.shields.io/badge/Python-v3.9-blue)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/coolfoolunidentifiedhacker/INFINATO-UB/graphs/commit-activity)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/coolfoolunidentifiedhacker/INFINATO-UB)   
[![Contributors](https://img.shields.io/github/contributors/coolfoolunidentifiedhacker/INFINATO-UB?style=flat-square&color=green)](https://github.com/coolfoolunidentifiedhacker/INFINATO-UB/graphs/contributors)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/coolfoolunidentifiedhacker/INFINATO-UB/blob/main/LICENSE)   

----

# Deploy
- [Heroku](#Deploy-to-Heroku)
- [Local Machine](#Deploy-Locally)

# Tutorial 
- Full Tutorial - [![Full Tutorial](https://img.shields.io/badge/Watch%20Now-blue)](https://www.youtube.com/watch?v=9wF7k9qA0Q4)

- Tutorial to get Redis URL and password - [here.](./resources/extras/redistut.md)
---

## Deploy to Heroku
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Deploy Locally
- [Traditional Method](#local-deploy---traditional-method)
- [Easy Method](#local-deploy---easy-method)

### Local Deploy - Traditional Method
- Get your [Necessary Variables](#Necessary-Variables)
- Clone the repository: <br />
`git clone https://github.com/coolfoolunidentifiedhacker/INFINATO-UB.git`
- Go to the cloned folder: <br />
`cd INFINATO-UB`
- Create a virtual env:   <br />
`virtualenv -p /usr/bin/python3 venv`
`../venv/bin/activate`
- Install the requirements:   <br />
`pip3 install -U -r requirements.txt`
- Generate your `SESSION`:
  - Go to `https://replit.com/@INFINATO/INFINATO-UB-SESSION-BUILDER`
  - Or `python3 resources/session/ssgen.py`
- Fill your details in a `.env` file, as given in [`.env.sample`](https://github.com/coolfoolunidentifiedhacker/INFINATO-UB/blob/main/.env.sample).
(You can either edit and rename the file or make a new file named `.env`.)
- Run the bot:
  - Linux Users:
   `bash resources/startup/startup.sh`
  - Windows Users:
    `python3 -m infinatoUserbot`

## Necessary Variables
- `API_ID` - Your API_ID from [my.telegram.org](https://my.telegram.org/)
- `API_HASH` - Your API_HASH from [my.telegram.org](https://my.telegram.org/)
- `SESSION` - SessionString for your accounts login session. Get it from [here](https://replit.com/@INFINATO/INFINATO-UB-SESSION-BUILDER)
- `REDIS_URI` - Redis endpoint URL, from [redislabs](http://redislabs.com/), tutorial [here.](./resources/extras/redistut.md)
- `REDIS_PASSWORD ` - Redis endpoint Password, from [redislabs](http://redislabs.com/), tutorial [here.](./resources/extras/redistut.md)

## Session String
* [![Run on Repl.it](https://replit.com/badge/github/coolfoolunidentifiedhacker/INFINATO-UB)](https://replit.com/@INFINATO/INFINATO-UB-SESSION-BUILDER)

## FORKED FROM [ULTROID](https://github.com/TeamUltroid/Ultroid) MODIFIED BY INFINATO