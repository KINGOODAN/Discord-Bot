# bot.py

import os

import discord
from dotenv import load_dotenv



load_dotenv()
DISCORD_TOKEN = {'ODAxMTY0MzY0NTQyOTAyMzM0.YAcsdQ.BwtQtrrORGwh3MOZv1E-MPr3rYQ'}
DISCORD_GUILD=('CUBE EMB TEST SERVER')


TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

client = CustomClient()

client = discord.Client()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  
    guild = discord.utils.get(client.guilds, name=DISCORD_GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id:{guild.id})'
        )
     
    member = '\n - '.join([member.name for member in guild.members])
    print (f'Guild Members:{member}')



    
  
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    Hi = f'Hi @{message.author}'  

    if message.content == '?Hello':
        response = (Hi)
   
        await message.channel.send(Hi)
@client.event
async def on_message(message):
    if message.content.startswith('?Memberlist'):
        for guild in client.guilds:
            for member in guild.members:
                await message.channel.send(member) 
        

    
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
client.run('ODAxMTY0MzY0NTQyOTAyMzM0.YAcsdQ.BwtQtrrORGwh3MOZv1E-MPr3rYQ')

