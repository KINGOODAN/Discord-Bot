#CUBE DISCORD BOT V1.0.0
#Python V3.9.1
#Discord.py V1.6.0
#V1.0.0 finished 2/12/2021
#-------------------------------------------------
import os
import discord
import discord.utils
import asyncio 
import time
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
#---------
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
ROLEc = 'Cubeular'
ROLEm = 'Muted'
ROLE9 = '9th Grader'
ROLE10 = '10th Grader'
#ROLE11 = '11th Grader'
#ROLE12 = '12th Grader'
#----------
intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)
client = discord.Client
bot = commands.Bot(command_prefix='?', intents = intents)
bot.remove_command('help')
#-------------------------------------------------
@bot.event
async def on_member_join(member):
    channel = bot.get_channel (712437956815618071) 
    embed = discord.Embed(title = 'User Has Joined the Server:sunglasses:', description = f'\n{member} has joined us!' + '\n\nRunning CUBEBOT v1.0.0', color = 0xC0C0C0)
    await channel.send(embed = embed)
    role = get(member.guild.roles, name=ROLEc)
    await member.add_roles(role)
    await member.send(f'Hi {member.name}, welcome to the CUBE Discord server!\n'
    ''' 
        For list of commands do ?help
        Please go the the Who's-Who channel and put your real name for safety reasons.

        Please read the rules of the server below.
        1. BE RESPECTFUL - We really want to create a safe environment in this server where people can have fun and chat
        2. DON'T SPAM - People are in class during the majority of the day and the constant pinging of discord is VERY distracting try not to spam for the sake of others
        3. AVOID POLITICS/SENSITIVE SUBJECTS - This is a school server, not a debate club
        4. STAFF HAVE FINAL SAY, ALWAYS
        5. IF IT'S NOT MEANT TO BE KIND, IT SHOULD NOT BE SAID
        6. NO NSFW, EVER! - NSFW is strictly forbidden, even on profile pictures or statuses! I will remove you from the server if you do not comply with this!
        ''')
#----------
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
#----------
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel (712437956815618071) 
    embed = discord.Embed(title = 'User Has Left the Server:ghost: ', description = f'\n{member} has left us. Hope they rejoin later!' + '\n\nRunning CUBEBOT v1.0.0', color = 0xC0C0C0)
    await channel.send(embed = embed)
#-------------------------------------------------
@bot.command(pass_context = True)
@commands.has_any_role('Moderator', 'Admin')
async def Sa(ctx,arg):
    channel = bot.get_channel(783107953095213086)
    await channel.send('||@everyone||' + ' ' + '\n**Staff Announcment**' + '\n' + arg)
#---------- 
@bot.command(pass_context = True)
@commands.has_role('Esports Coordinator')
async def ESa(ctx,arg):
    channel = bot.get_channel(783107953095213086) 
    await channel.send('||@everyone||' + ' ' + '\n**Esports Announcment**' + '\n' + arg)
#---------- 
@bot.command(pass_context = True)
@commands.has_any_role('Student Association', 'Advisory Senator')
async def SAa(ctx,arg):
    channel = bot.get_channel(783107953095213086) 
    await channel.send('||@everyone||' + ' ' + '\n**Student Association Announcment**' + '\n' + arg)
#----------
@bot.command(pass_context = True)
async def botsuggest(ctx,arg):
    channel = bot.get_channel(786727940125753374)
    embed = discord.Embed(title = 'Bot Suggestion', description = f'\n\n**{arg}**' + f'\n\n Poll initiated by {ctx.message.author}'+ '\n\nRunning CUBEBOT v1.0.0')
    msg = await channel.send(embed=embed)
    emoji = ('⏫')
    emoji2 = ('⏬')
    await msg.add_reaction(emoji)
    await msg.add_reaction(emoji2)
#----------
@bot.command(pass_context = True)
async def serversuggest(ctx,arg):
    channel = bot.get_channel(786727940125753374)
    embed = discord.Embed(title = 'Server Suggestion', description = f'\n\n**{arg}**' + f'\n\n Poll initiated by {ctx.message.author}'+ '\n\nRunning CUBEBOT v1.0.0')
    msg = await channel.send(embed=embed)
    emoji = ('⏫')
    emoji2 = ('⏬')
    await msg.add_reaction(emoji)
    await msg.add_reaction(emoji2)
#----------
@bot.command(pass_context = True)
async def help(ctx): 
    embed = discord.Embed(title = 'Available Categories:', description = '\n?helpLFT \n?helpsuggest\n?helproles\n?helpmisc'+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.green())
    await ctx.send (embed = embed)
#----------
@bot.command(pass_context = True)
async def helpsuggest(ctx): 
    embed = discord.Embed(title = 'Available Suggestion Commands:', description = '\n?botsuggest<yoursuggestion> \n?serversuggest<yoursuggestion>'+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.green())
    await ctx.send (embed = embed)
#----------
@bot.command(pass_context = True)
async def helpLFT(ctx): 
    embed = discord.Embed(title = 'Available LFT(looking for teammates) Commands:', description = '\n?WarThunderping<yourmessage> \n?CODping<yourmessage> \n?CSGOping<yourmessage> \n?ApexLegendsping<yourmessage> \n?LeagueofLegendsping<yourmessage> \n?SuperSmashBrosping<yourmessage> \n?RainbowSixSeigeping<yourmessage> \n?Overwatchping<yourmessage>' + '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.green())
    await ctx.send (embed = embed)
#----------
@bot.command(pass_context = True)
async def helproles(ctx): 
    embed = discord.Embed(title = 'Available Role Commands:', description = "\n?ninthgrade<@your username>\n(please only use if you are a 9th grader!) \n?tenthgrade<@your username>\n(please only use if you are a 10th grader!) \n?WarThunderrole \n?CODrole \n?CSGOrole \n?ApexLegendsrole \n?LeagueofLegendsrole \n?SuperSmashBrosrole \nRainbowSixSiegerole \nOverwatchrole"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.green())
    await ctx.send (embed = embed)
#----------
@bot.command(pass_context = True)
async def helpmisc(ctx): 
    embed = discord.Embed(title = 'Available Commands:', description = '\n?hello \n?memberlist'+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.green())
    await ctx.send (embed = embed)
#----------
@bot.command(pass_context = True)
async def memberlist(ctx):
    member = '\n  '.join([member.name for member in ctx.guild.members])
    embed = discord.Embed(title = 'Members:', description = f'{member}' + '\n\nRunning CUBEBOT v1.0.0',color = 0xC0C0C0)
    await ctx.send (embed = embed)
#----------
@bot.command(pass_context = True)
async def ninthgrade(ctx, member: discord.Member):
    guild = ctx.guild
    for role in guild.roles:
        if role.name == "10th Grader":
            embedalreadyhavegrade = discord.Embed(title="You Already have a grade", description=f"{member.mention} you already have a grade " + '\n\nRunning CUBEBOT v1.0.0', color=discord.Colour.red())
            if role in member.roles:
                await ctx.send(embed=embedalreadyhavegrade)
            else:
                role = get(ctx.message.guild.roles, id = 784553347079208980)
                await ctx.send (f'{ctx.message.author.mention} you now have the 9th Grade role!') 
                await ctx.message.author.add_roles(role)
#----------
@bot.command(pass_context = True)
async def tenthgrade(ctx, member: discord.Member):
    guild = ctx.guild
    for role in guild.roles:
        if role.name == "9th Grader":
            embedalreadyhavegrade = discord.Embed(title="You Already have a grade", description=f"{member.mention} you already have a grade " + '\n\nRunning CUBEBOT v1.0.0', color=discord.Colour.red())
            if role in member.roles:
                await ctx.send(embed=embedalreadyhavegrade)
            else:
                role = get(ctx.message.guild.roles, id = 784556769799962625)
                await ctx.send (f'{ctx.message.author.mention} you now have the 10th Grade role!') 
                await ctx.message.author.add_roles(role)
#----------
@bot.command(pass_context = True)
async def WarThunderrole(ctx): 
    role = get(ctx.message.guild.roles, id = 818603292120580106)
    await ctx.send (f'{ctx.message.author.mention} you now have the War Thunder role!') 
    await ctx.message.author.add_roles(role)
#----------     
@bot.command(pass_context = True)
@commands.has_role('War Thunder')
async def WarThunderping(ctx,arg):
    channel = bot.get_channel(758445986816589874)
    embed = discord.Embed(title = "**War Thunder LFT**", description = f'\n**{arg}**' + f"\n\n War Thunder LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.blue())
    await channel.send('||<@&808143642954956819>||')
    await channel.send(embed = embed)
#----------
@bot.command(pass_context = True)
async def CODrole(ctx): 
    role = get(ctx.message.guild.roles, id = 818603436593381406)
    await ctx.send (f'{ctx.message.author.mention} you now have the COD role!') 
    await ctx.message.author.add_roles(role)
#----------     
@bot.command(pass_context = True)
@commands.has_role('COD')
async def CODping(ctx,arg):
    channel = bot.get_channel(758445986816589874)
    embed = discord.Embed(title = "**COD LFT**", description = f'\n**{arg}**' + f"\n\n COD LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.blue())
    await channel.send('||<@&808143642954956819>||')
    await channel.send(embed = embed)
#----------
@bot.command(pass_context = True)
async def CSGOrole(ctx): 
    role = get(ctx.message.guild.roles, id = 818603636002127903)
    await ctx.send (f'{ctx.message.author.mention} you now have the CSGO role!') 
    await ctx.message.author.add_roles(role)
#----------     
@bot.command(pass_context = True)
@commands.has_role('CSGO')
async def CSGOping(ctx,arg):
    channel = bot.get_channel(758445986816589874)
    embed = discord.Embed(title = "**CSGO LFT**", description = f'\n**{arg}**' + f"\n\n CSGO LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.blue())
    await channel.send('||<@&808143642954956819>||')
    await channel.send(embed = embed)
#----------
@bot.command(pass_context = True)
async def ApexLegendsrole(ctx): 
    role = get(ctx.message.guild.roles, id = 818603693314277376)
    await ctx.send (f'{ctx.message.author.mention} you now have the Apex Legends role!') 
    await ctx.message.author.add_roles(role)
#----------     
@bot.command(pass_context = True)
@commands.has_role('Apex Legends')
async def ApexLegendsping(ctx,arg):
    channel = bot.get_channel(758445986816589874)
    embed = discord.Embed(title = "**Apex Legends LFT**", description = f'\n**{arg}**' + f"\n\n Apex Legends LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.blue())
    await channel.send('||<@&808143642954956819>||')
    await channel.send(embed = embed)
#----------
@bot.command(pass_context = True)
async def LeagueofLegendsrole(ctx): 
    role = get(ctx.message.guild.roles, id = 818603798749511680)
    await ctx.send (f'{ctx.message.author.mention} you now have the League of Legends role!') 
    await ctx.message.author.add_roles(role)
#----------     
@bot.command(pass_context = True)
@commands.has_role('League of Legends')
async def LeagueofLegendsping(ctx,arg):
    channel = bot.get_channel(758445986816589874)
    embed = discord.Embed(title = "**League of Legends LFT**", description = f'\n**{arg}**' + f"\n\n League of Legends LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.blue())
    await channel.send('||<@&808143642954956819>||')
    await channel.send(embed = embed)
#----------
@bot.command(pass_context = True)
async def SuperSmashBrosrole(ctx): 
    role = get(ctx.message.guild.roles, id = 818975670972841995)
    await ctx.send (f'{ctx.message.author.mention} you now have the SuperSmashBros role!') 
    await ctx.message.author.add_roles(role)
#----------     
@bot.command(pass_context = True)
@commands.has_role('SuperSmashBros')
async def SuperSmashBrosping(ctx,arg):
    channel = bot.get_channel(818975670972841995)
    embed = discord.Embed(title = "**SuperSmashBros LFT**", description = f'\n**{arg}**' + f"\n\n SuperSmashBros LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.blue())
    await channel.send('||<@&808143642954956819>||')
    await channel.send(embed = embed)
#----------
@bot.command(pass_context = True)
async def RainbowSixSiegerole(ctx): 
    role = get(ctx.message.guild.roles, id = 818975587527950377)
    await ctx.send (f'{ctx.message.author.mention} you now have the RainbowSixSiege role!') 
    await ctx.message.author.add_roles(role)
#----------     
@bot.command(pass_context = True)
@commands.has_role('RainbowSixSiege')
async def RainbowSixSiegeping(ctx,arg):
    channel = bot.get_channel(818975587527950377)
    embed = discord.Embed(title = "**RainbowSixSiege LFT**", description = f'\n**{arg}**' + f"\n\n RainbowSixSiege LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.blue())
    await channel.send('||<@&808143642954956819>||')
    await channel.send(embed = embed)
#----------
@bot.command(pass_context = True)
async def Overwatchrole(ctx): 
    role = get(ctx.message.guild.roles, id = 818975708708864013)
    await ctx.send (f'{ctx.message.author.mention} you now have the Overwatch role!') 
    await ctx.message.author.add_roles(role)
#----------     
@bot.command(pass_context = True)
@commands.has_role('Overwatch')
async def Overwatchping(ctx,arg):
    channel = bot.get_channel(818975708708864013)
    embed = discord.Embed(title = "**Overwatch LFT**", description = f'\n**{arg}**' + f"\n\n Overwatch LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.blue())
    await channel.send('||<@&808143642954956819>||')
    await channel.send(embed = embed)
#----------
@bot.command(pass_context = True)
async def hello(ctx): 
    await ctx.send(f'Hello {ctx.message.author.mention}!')
#-------------------------------------------------
@bot.command()
@commands.has_any_role('Moderator', 'Admin')
async def mute(ctx, member: discord.Member, time: int, d, *, reason=None):
    guild = ctx.guild
    for role in guild.roles:
        if role.name == "Muted":
            embedalreadymuted = discord.Embed(title="Already Muted", description=f"{member.mention} is already muted " + '\n\nRunning CUBEBOT v1.0.0', color=discord.Colour.red())
            if role in member.roles:
                await ctx.send(embed=embedalreadymuted)
            else:
                await member.add_roles(role)
                embed = discord.Embed(title="Muted!", description=f"{member.mention} has been muted ", colour=discord.Colour.red())
                embed.add_field(name="Reason:", value=reason, inline=False)
                embed.add_field(name="Time left for the mute:", value=f'{time} {d}' + '\n\nRunning CUBEBOT v1.0.0', inline=False)
                await ctx.send(embed=embed)
                if d == "s":
                    await asyncio.sleep(time)
                if d == "m":
                    await asyncio.sleep(time*60)
                if d == "h":
                    await asyncio.sleep(time*60*60)
                if d == "d":
                    await asyncio.sleep(time*60*60*24)
                if role in member.roles:
                    await member.remove_roles(role)
                    embed = discord.Embed(title="Unmuted ", description=f"{member.mention} your mute time is up." + '\n\nRunning CUBEBOT v1.0.0', color=discord.Colour.red())
                    await ctx.send(embed=embed)
                else:
                    return
#----------
@bot.command()
@commands.has_any_role('Moderator', 'Admin')
async def unmute(ctx, member: discord.Member):
    guild = ctx.guild
    for role in guild.roles:
        if role.name == "Muted":
            if role in member.roles:
                await member.remove_roles(role)
                embed = discord.Embed(title="unmuted ", description=f"{member.mention} you have been unmuted" + '\n\nRunning CUBEBOT v1.0.0', color=discord.Colour.red())
                await ctx.send(embed=embed)
            else:
                embednot = discord.Embed(title="Not Muted", description=f"{member.mention} is not muted." + '\n\nRunning CUBEBOT v1.0.0', color=discord.Colour.red())
                await ctx.send(embed=embednot)
                return
#-------------------------------------------------
bot.run('ODE4NTk1ODIxMDcwMzE5NjM3.YEaWxA.y7QTUC2loJTyq9AXNr6-tAUcZXg')
#-------------------------------------------------
#Thimgs we want to add in the future
#1 improved help command
#2 improve/add swear warning
#3 if you have any grade role you can't use any other grade command
#4 Xp/level system
#5 for any command that need an arg sending message to server not terminal
#6 send message to server if unknown command is used
#7 some sort of reward for leveling up with rng(more xp, xp multiplier)and with animation
#8 more hello like commands
#9 more game roles
#10 roll forward roles each year
#11 game status roles
#12 bug report command