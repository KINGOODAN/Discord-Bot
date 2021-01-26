import os
import discord
from dotenv import load_dotenv
#----------
load_dotenv()
DISCORD_TOKEN = {'YOUR TOKEN HERE'}
DISCORD_GUILD=('CUBE EMB TEST SERVER')
#----------
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
#----------
class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
#----------
client = CustomClient()
client = discord.Client()
#----------
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
#----------
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=DISCORD_GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id:{guild.id})'
        )
    member = '\n - '.join([member.name for member in guild.members])
    print (f'Guild Members:\n -{member}')
#----------
@client.event
async def on_member_join(member):
    await member.send(f'Hi {member.name}, welcome to the CUBE Discord server!\n')
    await member.send(
    '''
        Please read the rules of the server below.
        1. BE RESPECTFUL - We really want to create a safe environment in this server where people can have fun and chat
        2. DON'T SPAM - People are in class during the majority of the day and the constant pinging of discord is VERY distracting try not to spam for the sake of others
        3. AVOID POLITICS/SENSITIVE SUBJECTS - This is a school server, not a debate club
        4. STAFF HAVE FINAL SAY, ALWAYS
        5. IF IT'S NOT MEANT TO BE KIND, IT SHOULD NOT BE SAID
        6. NO NSFW, EVER! - NSFW is strictly forbidden, even on profile pictures or statuses! I will remove you from the server if you do not comply with this!
        ''')
#----------
@client.event
async def on_message(message):
    if message.content.startswith('?Memberlist'):
        for guild in client.guilds:
            for member in guild.members:
                await message.channel.send(member)
#----------
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    Hi = f'Hi {message.author}!'  
    if message.content == '?Hello':
        response = (Hi)
        await message.channel.send(Hi)
    elif message.content == 'raise-exception':
        raise discord.DiscordException
#----------
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
#----------
client.run('YOUR TOKEN HERE')
