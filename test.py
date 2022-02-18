import os
import discord
from dotenv import load_dotenv
import random
import csv

load_dotenv()
TOKEN = os.getenv('bot_token')
GUILD = os.getenv('bot_guild')



client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} has connected to Discord!')

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


client.run(TOKEN)
