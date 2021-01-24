# PersonalChannelBot
Discord bot which lets users create non-persistent personal voice channels.

![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/nathantowell/personal-channel-bot?style=flat-square) ![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/nathantowell/personal-channel-bot?style=flat-square)
## Running
The bot requires the following environment variables to be set, they're pretty self-explanatory.

```
# Optional
docker run -itd -p 127.0.0.1:6379:6379 --name=bot-redis redis:latest

# Create Bot
docker run -itd \
    -e DISCORD_TOKEN="<your bot token>" \
    -e REDIS_HOST="127.0.0.1" \
    -e REDIS_PORT="6379" \
    --net host \
    --name SomeBot \
    nathantowell/personal-channel-bot:latest
```
