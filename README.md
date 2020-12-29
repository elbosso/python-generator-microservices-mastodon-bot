# python-generator-microservices-mastodon-bot

<!---
[![start with why](https://img.shields.io/badge/start%20with-why%3F-brightgreen.svg?style=flat)](http://www.ted.com/talks/simon_sinek_how_great_leaders_inspire_action)
--->
[![GitHub release](https://img.shields.io/github/release/elbosso/python-generator-microservices-mastodon-bot/all.svg?maxAge=1)](https://GitHub.com/elbosso/python-generator-microservices-mastodon-bot/releases/)
[![GitHub tag](https://img.shields.io/github/tag/elbosso/python-generator-microservices-mastodon-bot.svg)](https://GitHub.com/elbosso/python-generator-microservices-mastodon-bot/tags/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/elbosso/python-generator-microservices-mastodon-bot.svg)](https://github.com/elbosso/python-generator-microservices-mastodon-bot/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/elbosso/python-generator-microservices-mastodon-bot.svg)](https://GitHub.com/elbosso/python-generator-microservices-mastodon-bot/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/elbosso/python-generator-microservices-mastodon-bot.svg)](https://GitHub.com/elbosso/python-generator-microservices-mastodon-bot/issues?q=is%3Aissue+is%3Aclosed)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/elbosso/python-generator-microservices-mastodon-bot/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/elbosso/python-generator-microservices-mastodon-bot.svg)](https://GitHub.com/elbosso/python-generator-microservices-mastodon-bot/graphs/contributors/)
[![Github All Releases](https://img.shields.io/github/downloads/elbosso/python-generator-microservices-mastodon-bot/total.svg)](https://github.com/elbosso/python-generator-microservices-mastodon-bot)
[![Website elbosso.github.io](https://img.shields.io/website-up-down-green-red/https/elbosso.github.io.svg)](https://elbosso.github.io/)

This project uses test data generators to post messages to the Mastodon Social Network. 
It uses the Rest Services offered by 
[generator-microservices](https://GitHub.com/elbosso/generator-microservices).

The application is designed to run inside a docker container. 

The docker container needs an environment file (see also _environment.env.template_) defining

```
MASTODON_ACCESS_TOKEN=
MASTODON_API_BASE_URL=
```
The application generates among others

* clickbait
* fantasy roleplaying character professions
* credit card data
* avatar images
* floor plans for randomly generated dungeons/caves
* mazes
