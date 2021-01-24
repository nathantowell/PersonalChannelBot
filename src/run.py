import os,discord
from db import Server

intents = discord.Intents(voice_states=True, members=True, guilds=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(name='your back!', type=discord.ActivityType.watching))
    #await client.change_presence(activity=discord.CustomActivity(name='Handling My Business!', emoji='<a:Tail_Wag:711971800157913088>'), status=discord.Status.dnd)
    print('Logged on as', client.user)
    

@client.event
async def on_guild_available(guild):
    print('Joined guild:', guild.name)
    server = Server(guild.id)
    if server.private_voice_category is not None:
        category = discord.utils.get(guild.categories, id=server.private_voice_category)
        if category is not None and category.channels is not None:
            for channel in category.channels:
                if len(channel.members) == 0 and channel.id != server.private_voice_creation_channel:
                    await channel.delete()

@client.event
async def on_voice_state_update(member, before, after):
    server = Server(member.guild.id)
    if server.private_voice_category is None:
        return

    if after.channel is not None:
        if after.channel.id == server.private_voice_creation_channel:
            channel = await after.channel.guild.create_voice_channel(name =  f'{member.name}\'s Channel', overwrites=None, category=after.channel.category, reason=None)
            await channel.set_permissions(member, manage_channels=True, move_members=True, view_channel=True, connect=True)
            await member.move_to(channel)
    
    if before.channel is not None:
        if before.channel.category_id is not None and before.channel.category_id == server.private_voice_category:
            if before.channel.id != server.private_voice_creation_channel:
                if len(before.channel.members) == 0:
                    await before.channel.delete()

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
client.run(DISCORD_TOKEN)