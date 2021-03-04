#CUBE DISCORD BOT V1.0.0
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
    channel = bot.get_channel (801166049159544845) 
    embed = discord.Embed(title = 'User Has Joined the Server:sunglasses:', description = f'\n{member} has joined us!' + '\n\nRunning CUBEBOT v1.0.0', color = 0xC0C0C0)
    await channel.send(embed = embed)
    role = get(member.guild.roles, name=ROLEc)
    await member.add_roles(role)
    await member.send(f'Hi {member.name}, welcome to the CUBE Discord server!\n'
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
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
#----------
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel (801166049159544845) 
    embed = discord.Embed(title = 'User Has Left the Server:ghost: ', description = f'\n{member} has left us. Hope they rejoin later!' + '\n\nRunning CUBEBOT v1.0.0', color = 0xC0C0C0)
    await channel.send(embed = embed)
#-------------------------------------------------
@bot.command(pass_context = True)
async def Sa(ctx,arg):
    channel = bot.get_channel(807326547735347291)
    await channel.send('||@everyone||' + ' ' + '\n**Staff Announcment**' + '\n' + arg)
#---------- 
@bot.command(pass_context = True)
async def ESa(ctx,arg):
    channel = bot.get_channel(807326547735347291) 
    await channel.send('||@everyone||' + ' ' + '\n**Esports Announcment**' + '\n' + arg)
#---------- 
@bot.command(pass_context = True)
async def SAa(ctx,arg):
    channel = bot.get_channel(807326547735347291) 
    await channel.send('||@everyone||' + ' ' + '\n**Student Association Announcment**' + '\n' + arg)
#----------     
@bot.command(pass_context = True)
async def warthunder(ctx,arg):
    channel = bot.get_channel(801166288327016488)
    embed = discord.Embed(title = "**War Thunder LFT**", description = f'\n**{arg}**' + f"\n\n War Thunder LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.blue())
    await channel.send('||<@&808143642954956819>||')
    await channel.send(embed = embed)
#----------
@bot.command(pass_context = True)
async def botsuggest(ctx,arg):
    channel = bot.get_channel(801166288327016488)
    embed = discord.Embed(title = 'Bot Suggestion', description = f'\n\n**{arg}**' + f'\n\n Poll initiated by {ctx.message.author}'+ '\n\nRunning CUBEBOT v1.0.0')
    msg = await channel.send(embed=embed)
    emoji = ('⏫')
    emoji2 = ('⏬')
    await msg.add_reaction(emoji)
    await msg.add_reaction(emoji2)
#----------
@bot.command(pass_context = True)
async def serversuggest(ctx,arg):
    channel = bot.get_channel(801166288327016488)
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
    embed = discord.Embed(title = 'Available LFT(looking for teammates) Commands:', description = '\n?warthunder<yourmessage>' + '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.green())
    await ctx.send (embed = embed)
#----------
@bot.command(pass_context = True)
async def helproles(ctx): 
    embed = discord.Embed(title = 'Available Role Commands:', description = "\n?ninthgrade<@your username>\n(please only use if you are a 9th grader!) \n\n?tenthgrade<@your username>\n(please only use if you are a 10th grader!) \n\n?warthunderrole<@your username>"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.green())
    await ctx.send (embed = embed)
#----------
@bot.command(pass_context = True)
async def helpmisc(ctx): 
    embed = discord.Embed(title = 'Available Commands:', description = '\n?hello'+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.green())
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
                role = get(ctx.message.guild.roles, id = 805870610156093522)
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
                role = get(ctx.message.guild.roles, id = 804046846363828254)
                await ctx.send (f'{ctx.message.author.mention} you now have the 10th Grade role!') 
                await ctx.message.author.add_roles(role)
#----------
@bot.command(pass_context = True)
async def warthunderrole(ctx): 
    role = get(ctx.message.guild.roles, id = 808143642954956819)
    await ctx.send (f'{ctx.message.author.mention} you now have the War Thunder Ping role!') 
    await ctx.message.author.add_roles(role)
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

'''@bot.command(pass_context = True)
async def helplist(ctx):
    helptext = "```"
    for command in bot.commands:
        helptext+=f"{command}\n"
    helptext+="```"
    await ctx.send(helptext)'''

@bot.command(pass_context = True)
async def mod(ctx, member: discord.Member):
    guild = ctx.guild
    for role in guild.roles:
        if role in member.roles:
            role = get(ctx.message.guild.roles, id = 808710488547393578) 
            await ctx.message.author.add_roles(role)

bot.run('Your Bot Token')