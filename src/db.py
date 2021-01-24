import os,redis,json

REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']

redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

class Server:
    def __init__(self, guild):
        self._guild = guild
        self._private_voice_category = None
        self._private_voice_creation_channel = None
        self.retrieveDB()
    
    @property
    def guild(self):
        return self._guild
    
    @guild.setter
    def guild(self, value):
        self._guild = value
        self.updateDB()
    
    @property
    def private_voice_category(self):
        return self._private_voice_category
    
    @private_voice_category.setter
    def private_voice_category(self, value):
        self._private_voice_category = value
        self.updateDB()

    @property
    def private_voice_creation_channel(self):
        return self._private_voice_creation_channel
    
    @private_voice_creation_channel.setter
    def private_voice_creation_channel(self, value):
        self._private_voice_creation_channel = value
        self.updateDB()
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def updateDB(self):
        redis.set('server:' + str(self._guild), self.toJSON())
    
    def retrieveDB(self):
        if redis.exists('server:' + str(self._guild)) is False:
            return
        data = json.loads(redis.get('server:' + str(self._guild)))
        self._private_voice_category = data['_private_voice_category']
        self._private_voice_creation_channel = data['_private_voice_creation_channel']
