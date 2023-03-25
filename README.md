# PersonalChannelBot

[![Build](https://github.com/nathantowell/PersonalChannelBot/workflows/Build%20and%20Push/badge.svg)](https://github.com/nathantowell/PersonalChannelBot/actions/workflows/build.yml)

Discord bot which lets users create non-persistent personal voice channels.

## Running

The bot requires the following environment variables to be set, they're pretty self-explanatory.

```
# Optional
docker network create redis
docker volume create redis
docker run -itd --volume redis:/data --network redis --name redis redis:7-alpine

# Create Bot
docker run -itd \
    -e DISCORD_TOKEN="<your bot token>" \
    -e REDIS_HOST="redis" \
    -e REDIS_PORT="6379" \
    --network redis
    --name SomeBotName \
    ghcr.io/nathantowell/personal-channel-bot:latest
```
