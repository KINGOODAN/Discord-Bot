# bot.py
import os

import discord
from dotenv import load_dotenv

DISCORD_TOKEN={'ODAxMTY0MzY0NTQyOTAyMzM0.YAcsdQ.Y1DgCM5Crm9glEO5JmehR5u5a68'}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)


