#CUBE DISCORD BOT V1.2.1
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
from pretty_help import PrettyHelp, Navigation
#---------
load_dotenv()
TOKEN = open('MAIN_SERVER_TOKEN.txt', 'r').read()
ROLEc = 'Cubeular'
ROLEm = 'Muted'
ROLE9 = '9th Grader'
ROLE10 = '10th Grader'
BotVerson = 'V1.2.2'
WT = "War Thunder"
COD = "COD"
CSGO = "CSGO"
AL = "Apex Legends"
LOL = "League of Legends"
RSS = "Rainbow Six Siege"
SSB = "Super Smash Bros"
O = "Overwatch"
BF1 = "BF1"
M = "Minecraft"
D = "Doom"
DCP = "Developer Changelog Ping"
#----------
intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)
client = discord.Client
bot = commands.Bot(command_prefix='?', intents = intents)
bot.remove_command('help')
#-------------------------------------------------
ending_note = f"Running CUBEBOT {BotVerson}"
nav = Navigation("⏫", "⏬")
color = discord.Color.dark_gold()
bot.help_command = PrettyHelp(navigation=nav, 
index_title="Commands", 
color=color, 
active_time=120, 
ending_note=ending_note,
sort_commands=False
)
#-------------------------------------------------
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="joins") 
    embed = discord.Embed(title = 'User Has Joined the Server:sunglasses:', description = f'\n{member} has joined us!' + f'\n\nRunning CUBEBOT {BotVerson}', color = 0xC0C0C0)
    await channel.send(embed = embed)
    role = get(member.guild.roles, name=ROLEc)
    await member.add_roles(role)
    await member.send(f'    Hi {member.name}, welcome to the CUBE Discord server!\n'
    ''' 
        For list of commands do ?help
        Please go the the Who's-Who channel and put your real name for safety reasons.
        Rules:''') 

    await member.send(
'''(1)Your Account: 
    1. Inappropriate or offensive avatars, usernames, and statuses are prohibited. 
    2. Self-advertising through usernames or statuses is not permitted.
    3. Staff are hereby granted the right to change nicknames if and only if said username or status violates rules(s) (1) or (2) of this section, or rule (1) of Section (3).
    4. Any user may only hold one account on this server. If we suspect that a user has a secondary account, immediate action will be taken. 

    (2)Server Rules: 
    1. Discrimination, racist or otherwise offensive jokes, and/or hate speech through text, images, or videos will not be tolerated. 
    2. Insults, threats, excessive pinging, or any offensive content targeted at specific members is strictly not allowed. 
    3. DDOS, raid, or other such threats will not be tolerated. 
    4. Please post content in correct channels. 
    4a. Self-promotions are only allowed in #advertising channel. 
    5. Do not ask staff to become a moderator, all moderator applications are closed.
    6. Impersonating staff members, including similar avatars and nicknames is not allowed.
    7. Political opinions, including links, images, videos, avatars, nicknames, and statuses will not be tolerated. This is a school server.
    8. Please Direct Message me or an Admin with complaints about staff/server policies.
    9. Do not leak Direct Messages, locked chats, or sensitive information about this server. 

    (3)Content:
    1. NSFW content, text, avatars, or usernames/nicknames of any kind is strictly prohibited. 
    2. Discussing/promoting illegal activity will not be tolerated. 
    3. Staff reserves the right to remove any content for any reason at any time. 
    4. Plagiarism, spam, and copypasta are all forbidden.''')
    await member.send('''Punishment System: 

    Tier One - Warning 
    -Violating Section(1); rule (2). 
    -Violating Section (2); rule(s) (4/4a), (5), (6), or (8). 

    Tier Two - Mute
    -Violating Section(2); rule(s) (1), (2), (3), or (7). 
    -Violating Section(3); rule(s) (2) or (4).
    -Repeated violations (<2) of the rules outlined in Tier One.

    Tier Three - Kick/Role Removal
     -Violating Section(1); rule (1).
     -Violating Section(2); rule (9).
     -Repeated violations (<4) of the rules outlined in Tier One. 
     -Repeated violations (<2) of the rules outlined in Tier Two. 

    Tier Four - Ban
    -Violating Section(1); rule (4)
    -Violating Section(3); rule (1)
    -Repeated violations (<5) of the rules outlined in Tier One. 
    -Repeated violations (<3) of the rules outlined in Tier Two. 
    -Repeated violations (<1) of the rules outlined in Tier Three.
''')
#----------
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(f'CUBEBOT Build {BotVerson} \n Github==> https://github.com/KINGOODAN/Discord-Bot'))
#----------
@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="joins") 
    embed = discord.Embed(title = 'User Has Left the Server:ghost: ', description = f'\n{member} has left us. Hope they rejoin later!' + f'\n\nRunning CUBEBOT {BotVerson}', color = 0xC0C0C0)
    await channel.send(embed = embed)
#----------
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")
#-------------------------------------------------
class Announcements(commands.Cog, description="These are the commands to make announcements."):
    #----------
    @commands.command(pass_context = True)
    @commands.has_any_role('Moderator', 'Admin')
    async def Sa(self,ctx,*,arg):
        '''An announcement command for staff.'''
        channel = discord.utils.get(ctx.guild.channels, name="announcements")
        await ctx.message.delete()
        await channel.send('||@everyone||' + ' ' + '\n**Staff Announcement**' + '\n' + arg)
    #---------- 
    @commands.command(pass_context = True)
    @commands.has_role('Esports Coordinator')
    async def ESa(self,ctx,*,arg):
        '''An announcement command for E-Sports.'''
        channel = discord.utils.get(ctx.guild.channels, name="announcements") 
        await ctx.message.delete()
        await channel.send('||@everyone||' + ' ' + '\n**Esports Announcement**' + '\n' + arg)
    #---------- 
    @commands.command(pass_context = True)
    @commands.has_any_role('Student Association', 'Advisory Senator')
    async def SAa(self,ctx,*,arg):
        '''An announcement command for Student Association.'''
        channel = discord.utils.get(ctx.guild.channels, name="announcements") 
        await ctx.message.delete()
        await channel.send('||@everyone||' + ' ' + '\n**Student Association Announcement**' + '\n' + arg)
    #----------
    @commands.command()
    @commands.has_role('Developer')
    async def Changelog(self,ctx,arg1,arg2): 
        '''This is the changelog command (developers only!). Individual <args> apply; numbered 1 and 2. Arg 1 are the added features, and Arg 2 are the fixes.'''
        d = get(ctx.guild.roles, name="Developer Changelog Ping")
        channel = discord.utils.get(ctx.guild.channels, name="bot-change-log")
        await ctx.message.delete()
        await channel.send (f"||{d.mention}|| \n\n **Bot Update!** \n Version {BotVerson} \n\n Added: \n-{arg1} \n\n Fixed: \n-{arg2}")
#-------------------------------------------------
class Suggest_Report(commands.Cog, description="Theses are commands to make suggestions or report things."):
    #----------
    @commands.command(pass_context = True)
    async def bugreport(self,ctx,*,arg):
        '''A command that allows you to report bug with the bot.'''
        channel = discord.utils.get(ctx.guild.channels, name="bug-report-output")
        embed = discord.Embed(title = 'Bug Report', description = f'\n\n{arg}' + f'\n\n Bug Report initiated by {ctx.message.author}'+ f'\n\nRunning CUBEBOT {BotVerson}')
        await channel.send(embed=embed)
        await ctx.send("Your report has been logged!")
    #----------
    @commands.command(pass_context = True)
    async def botsuggest(self,ctx,*,arg):
        '''A command that lets you make suggestions about the bot.'''
        channel = discord.utils.get(ctx.guild.channels, name="server-suggestions")
        embed = discord.Embed(title = 'Bot Suggestion', description = f'\n\n**{arg}**' + f'\n\n Poll initiated by {ctx.message.author}'+ f'\n\nRunning CUBEBOT {BotVerson}')
        msg = await channel.send(embed=embed)
        emoji = ('⏫')
        emoji2 = ('⏬')
        await msg.add_reaction(emoji)
        await msg.add_reaction(emoji2)
    #----------
    @commands.command(pass_context = True)
    async def serversuggest(self,ctx,*,arg):
        '''A command that lets you make suggestions about the server.'''
        channel = discord.utils.get(ctx.guild.channels, name="server-suggestions")
        embed = discord.Embed(title = 'Server Suggestion', description = f'\n\n**{arg}**' + f'\n\n Poll initiated by {ctx.message.author}'+ f'\n\nRunning CUBEBOT {BotVerson}')
        msg = await channel.send(embed=embed)
        emoji = ('⏫')
        emoji2 = ('⏬')
        await msg.add_reaction(emoji)
        await msg.add_reaction(emoji2)
#-------------------------------------------------
class Miscellaneous(commands.Cog, description="These are Miscellaneous commands."):
    #----------
    @commands.command(pass_context = True)
    async def memberlist(self,ctx):
        '''A command that gives a list of all the members on the server.'''
        member = '\n  '.join([member.name for member in ctx.guild.members])
        embed = discord.Embed(title = 'Members:', description = f'{member}' + f'\n\nRunning CUBEBOT {BotVerson}',color = 0xC0C0C0)
        await ctx.send (embed = embed)
    #----------
    @commands.command(pass_context = True)
    async def hello(self,ctx): 
        '''A fun command that say Hello.'''
        await ctx.send(f'Hello {ctx.message.author.mention}!')
    #----------
    @commands.command(pass_context = True)
    async def hi(self,ctx): 
        '''A fun command that say Hi.'''
        await ctx.send(f'Hi {ctx.message.author.mention}!')
#-------------------------------------------------
class Roles(commands.Cog, description="These are all the commands that you use to get roles."):
    """#----------
    @commands.command(pass_context = True)
    async def ninthgrade(self,ctx, member: discord.Member):
        '''This command give you the Ninth Grader role.'''
        guild = ctx.guild
        for role in guild.roles:
            if role.name == "10th Grader":
                embedalreadyhavegrade = discord.Embed(title="You Already have a grade", description=f"{member.mention} you already have a grade " + f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Colour.red())
                if role in member.roles:
                    await ctx.send(embed=embedalreadyhavegrade)
                else:
                    role = get(ctx.message.guild.roles, id = 784553347079208980)
                    await ctx.send (f'{ctx.message.author.mention} you now have the 9th Grade role!') 
                    await ctx.message.author.add_roles(role)
    #----------
    @commands.command(pass_context = True)
    async def tenthgrade(self,ctx, member: discord.Member):
        '''This command give you the Tenth Grader role.'''
        guild = ctx.guild
        for role in guild.roles:
            if role.name == "9th Grader":
                embedalreadyhavegrade = discord.Embed(title="You Already have a grade", description=f"{member.mention} you already have a grade " + f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Colour.red())
                if role in member.roles:
                    await ctx.send(embed=embedalreadyhavegrade)
                else:
                    role = get(ctx.message.guild.roles, id = 784556769799962625)
                    await ctx.send (f'{ctx.message.author.mention} you now have the 10th Grade role!') 
                    await ctx.message.author.add_roles(role)
    """#----------
    @commands.command(name="WarThunderrole", aliases=["WarThunderRole"],pass_context = True)
    async def WarThunderrole(self,ctx):
        '''This command give you the War Thunder role.'''
        role = get(ctx.guild.roles, name = f"{WT}")
        await ctx.send (f'{ctx.message.author.mention} you now have the {WT} role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(name="CODrole", aliases=["CODRole"],pass_context = True)
    async def CODrole(self,ctx): 
        '''This command give you the COD role.'''
        role = get(ctx.guild.roles, name = f"{COD}")
        await ctx.send (f'{ctx.message.author.mention} you now have the {COD} role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(name="CSGOrole", aliases=["CSGORole"],pass_context = True)
    async def CSGOrole(self,ctx): 
        '''This command give you the CSGO role.'''
        role = get(ctx.guild.roles, name = f"{CSGO}")
        await ctx.send (f'{ctx.message.author.mention} you now have the {CSGO} role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(name="ApexLegendsrole", aliases=["ApexLegendsRole"],pass_context = True)
    async def ApexLegendsrole(self,ctx):
        '''This command give you the Apex Legends role.''' 
        role = get(ctx.guild.roles, name = f"{AL}")
        await ctx.send (f'{ctx.message.author.mention} you now have the {AL} role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(name="LeagueofLegendsrole", aliases=["LeagueofLegendsRole"],pass_context = True)
    async def LeagueofLegendsrole(self,ctx): 
        '''This command give you the League of Legends role.'''
        role = get(ctx.guild.roles, name = f"{LOL}")
        await ctx.send (f'{ctx.message.author.mention} you now have the {LOL} role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(name="SuperSmashBrosrole", aliases=["SuperSmashBrosRole"],pass_context = True)
    async def SuperSmashBrosrole(self,ctx): 
        '''This command give you the Super Smash Bros role.'''
        role = get(ctx.guild.roles, name = f"{SSB}")
        await ctx.send (f'{ctx.message.author.mention} you now have the {SSB} role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(name="RainbowSixSiegerole", aliases=["RainbowSixSiegeRole"],pass_context = True)
    async def RainbowSixSiegerole(self,ctx): 
        '''This command give you the Rainbow Six Siege role.'''
        role = get(ctx.guild.roles, name = f"{RSS}")
        await ctx.send (f'{ctx.message.author.mention} you now have the {RSS} role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(name="Overwatchrole", aliases=["OverwatchRole"],pass_context = True)
    async def Overwatchrole(self,ctx): 
        '''This command give you the Overwatch role.'''
        role = get(ctx.guild.roles, name = f"{O}")
        await ctx.send (f'{ctx.message.author.mention} you now have the {O} role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(name="BF1role", aliases=["BF1Role"],pass_context = True)
    async def BF1role(self,ctx): 
        '''This command give you the BF1 role.'''
        role = get(ctx.guild.roles, name = f"{BF1}")
        await ctx.send (f'{ctx.message.author.mention} you now have the {BF1} role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(name="Minecraftrole", aliases=["MinecraftRole"],pass_context = True)
    async def Minecraftrole(self,ctx): 
        '''This command give you the Minecraft role.'''
        role = get(ctx.guild.roles, name = f"{M}")
        await ctx.send (f'{ctx.message.author.mention} you now have the {M} role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(name="Doomrole", aliases=["DoomRole"],pass_context = True)
    async def Doomrole(self,ctx): 
        '''This command give you the Doom role.'''
        role = get(ctx.guild.roles, name = f"{D}")
        await ctx.send (f'{ctx.message.author.mention} you now have the {D} role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(name="DCLProle", aliases=["DCLPRole"],pass_context = True)
    async def DCLProle(self,ctx): 
        '''This command give you the Developer Change Log Ping role.'''
        role = get(ctx.guild.roles, name = f"{DCP}")
        await ctx.send (f'{ctx.message.author.mention} you now have the {DCP} role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(name="removerole", aliases=["removeRole"],pass_context = True)
    async def removerole(self,ctx,arg): 
        '''This command lets you remove roles from yourself using roles name.'''
        role = get(ctx.guild.roles, name = f"{arg}")
        await ctx.message.author.remove_roles(role)
        await ctx.send (f'{ctx.message.author.mention} your role has been removed!')
#-------------------------------------------------
class Pings(commands.Cog, description="These are all the different Ping command."):
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('War Thunder')
    async def WarThunderping(self,ctx,*,arg):
        '''This command pings people with your message with the War Thunder role'''
        wt = get(ctx.guild.roles, name = f"{WT}")
        channel = discord.utils.get(ctx.guild.channels, name = "looking-for-teammates")
        embed = discord.Embed(title = "**War Thunder LFT**", description = f'\n**{arg}**' + f"\n\n {WT} LFT initiated by {ctx.message.author}"+ f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Color.blue())
        await channel.send(f'||{wt.mention}||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('COD')
    async def CODping(self,ctx,*,arg):
        '''This command pings people with your message with the COD role'''
        cod = get(ctx.guild.roles, name = f"{COD}")
        channel = discord.utils.get(ctx.guild.channels, name = "looking-for-teammates")
        embed = discord.Embed(title = "**COD LFT**", description = f'\n**{arg}**' + f"\n\n {COD} LFT initiated by {ctx.message.author}"+ f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Color.blue())
        await channel.send(f'||{cod.mention}||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('CSGO')
    async def CSGOping(self,ctx,*,arg):
        '''This command pings people with your message with the CSGO role'''
        csgo = get(ctx.guild.roles, name = f"{CSGO}")
        channel = discord.utils.get(ctx.guild.channels, name = "looking-for-teammates")
        embed = discord.Embed(title = "**CSGO LFT**", description = f'\n**{arg}**' + f"\n\n {CSGO} LFT initiated by {ctx.message.author}"+ f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Color.blue())
        await channel.send(f'||{csgo.mention}||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('Apex Legends')
    async def ApexLegendsping(self,ctx,*,arg):
        '''This command pings people with your message with the Apex Legends role'''
        al = get(ctx.guild.roles, name = f"{AL}")
        channel = discord.utils.get(ctx.guild.channels, name = "looking-for-teammates")
        embed = discord.Embed(title = "**Apex Legends LFT**", description = f'\n**{arg}**' + f"\n\n {AL} LFT initiated by {ctx.message.author}"+ f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Color.blue())
        await channel.send(f'||{al.mention}||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('League of Legends')
    async def LeagueofLegendsping(self,ctx,*,arg):
        '''This command pings people with your message with the League of Legends role'''
        lol = get(ctx.guild.roles, name = f"{LOL}")
        channel = discord.utils.get(ctx.guild.channels, name = "looking-for-teammates")
        embed = discord.Embed(title = "**League of Legends LFT**", description = f'\n**{arg}**' + f"\n\n {LOL} LFT initiated by {ctx.message.author}"+ f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Color.blue())
        await channel.send(f'||{lol.mention}||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('Super Smash Bros')
    async def SuperSmashBrosping(self,ctx,*,arg):
        '''This command pings people with your message with the Super Smash Bros role'''
        ssb = get(ctx.guild.roles, name = f"{SSB}")
        channel = discord.utils.get(ctx.guild.channels, name = "looking-for-teammates")
        embed = discord.Embed(title = "**SuperSmashBros LFT**", description = f'\n**{arg}**' + f"\n\n {SSB} LFT initiated by {ctx.message.author}"+ f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Color.blue())
        await channel.send(f'||{ssb.mention}||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('Rainbow Six Siege')
    async def RainbowSixSiegeping(self,ctx,*,arg):
        '''This command pings people with your message with the Rainbow Six Siege role'''
        rss = get(ctx.guild.roles, name = f"{RSS}")
        channel = discord.utils.get(ctx.guild.channels, name = "looking-for-teammates")
        embed = discord.Embed(title = "**RainbowSixSiege LFT**", description = f'\n**{arg}**' + f"\n\n {RSS} LFT initiated by {ctx.message.author}"+ f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Color.blue())
        await channel.send(f'||{rss.mention}||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('Overwatch')
    async def Overwatchping(self,ctx,*,arg):
        '''This command pings people with your message with the Overwatch role'''
        o = get(ctx.guild.roles, name = f"{O}")
        channel = discord.utils.get(ctx.guild.channels, name = "looking-for-teammates")
        embed = discord.Embed(title = "**Overwatch LFT**", description = f'\n**{arg}**' + f"\n\n {O} LFT initiated by {ctx.message.author}"+ f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Color.blue())
        await channel.send(f'||{o.mention}||')
        await channel.send(embed = embed)
    #----------
    @commands.command(pass_context = True)
    @commands.has_role('BF1')
    async def BF1ping(self,ctx,*,arg):
        '''This command pings people with your message with the BF1 role'''
        bf1 = get(ctx.guild.roles, name = f"{BF1}")
        channel = discord.utils.get(ctx.guild.channels, name = "looking-for-teammates")
        embed = discord.Embed(title = "**BF1 LFT**", description = f'\n**{arg}**' + f"\n\n {BF1} LFT initiated by {ctx.message.author}"+ f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Color.blue())
        await channel.send(f'||{bf1.mention}||')
        await channel.send(embed = embed)
    #----------
    @commands.command(pass_context = True)
    @commands.has_role('Minecraft')
    async def Minecraftping(self,ctx,*,arg):
        '''This command pings people with your message with the Minecraft role'''
        m = get(ctx.guild.roles, name = f"{M}")
        channel = discord.utils.get(ctx.guild.channels, name = "looking-for-teammates")
        embed = discord.Embed(title = "**Minecraft LFT**", description = f'\n**{arg}**' + f"\n\n {M} LFT initiated by {ctx.message.author}"+ f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Color.blue())
        await channel.send(f'||{m.mention}||')
        await channel.send(embed = embed)
    #----------
    @commands.command(pass_context = True)
    @commands.has_role('Doom')
    async def Doomping(self,ctx,*,arg):
        '''This command pings people with your message with the Doom role'''
        d = get(ctx.guild.roles, name = f"{D}")
        channel = discord.utils.get(ctx.guild.channels, name = "looking-for-teammates")
        embed = discord.Embed(title = "**Doom LFT**", description = f'\n**{arg}**' + f"\n\n {D} LFT initiated by {ctx.message.author}"+ f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Color.blue())
        await channel.send(f'||{d.mention}||')
        await channel.send(embed = embed)
#-------------------------------------------------
class Admin(commands.Cog, description="These are commands for the staff of the server."):
    #----------
    @commands.command()
    @commands.has_any_role('Moderator', 'Admin', 'Trial Moderator')
    async def mute(self,ctx, member: discord.Member, time: int, d, *, reason=None):
        '''A command to mute members.'''
        guild = ctx.guild
        for role in guild.roles:
            if role.name == "Muted":
                embedalreadymuted = discord.Embed(title="Already Muted", description=f"{member.mention} is already muted " + f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Colour.red())
                if role in member.roles:
                    await ctx.send(embed=embedalreadymuted)
                else:
                    await member.add_roles(role)
                    embed = discord.Embed(title="Muted!", description=f"{member.mention} has been muted ", colour=discord.Colour.red())
                    embed.add_field(name="Reason:", value=reason, inline=False)
                    embed.add_field(name="Time left for the mute:", value=f'{time} {d}' + f'\n\nRunning CUBEBOT {BotVerson}', inline=False)
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
                        embed = discord.Embed(title="Unmuted ", description=f"{member.mention} your mute time is up." + f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Colour.red())
                        await ctx.send(embed=embed)
                    else:
                        return
    #----------
    @commands.command()
    @commands.has_any_role('Moderator', 'Admin', 'Trial Moderator')
    async def unmute(self,ctx, member: discord.Member):
        '''A command to unmute member who are muted.'''
        guild = ctx.guild
        for role in guild.roles:
            if role.name == "Muted":
                if role in member.roles:
                    await member.remove_roles(role)
                    embed = discord.Embed(title="unmuted ", description=f"{member.mention} you have been unmuted" + f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Colour.red())
                    await ctx.send(embed=embed)
                else:
                    embednot = discord.Embed(title="Not Muted", description=f"{member.mention} is not muted." + f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Colour.red())
                    await ctx.send(embed=embednot)
                    return
        #----------
        #----------
    @commands.command()
    @commands.has_role('Admin')
    async def modtrial(self,ctx,member: discord.Member):
        '''Gives a member mod for 7 days.'''
        guild = ctx.guild
        for role in guild.roles:
            if role.name == "Trial Moderator":
                embedalreadyintrial = discord.Embed(title="Already in a trial", description=f"{member.mention} is already in a Moderator Trial." + '\n\nRunning CUBEBOT v1.0.0', color=discord.Colour.red())
                if role in member.roles:
                    await ctx.send(embed=embedalreadyintrial)
                else:
                    await member.add_roles(role)
                    embed = discord.Embed(title="Moderator Trial Started", description=f"{member.mention} you are now a mod for the next 7 days (this trial can be removed).", colour=discord.Colour.red())
                    await ctx.send(embed=embed)
                    await asyncio.sleep(7*60*60*24)
                    if role in member.roles:
                        await member.remove_roles(role)
                        embedtrialover = discord.Embed(title="Moderator Trial Ended", description=f"{member.mention} your Moderator Trial is over." + '\n\nRunning CUBEBOT v1.0.0', color=discord.Colour.red())
                        await ctx.send(embed=embedtrialover)
                    else:
                        return
    #----------
    @commands.command()
    @commands.has_role('Admin')
    async def removemodtrial(self,ctx, member: discord.Member):
        '''Removes the mod trial from a member.'''
        guild = ctx.guild
        for role in guild.roles:
            if role.name == "Trial Moderator":
                if role in member.roles:
                    await member.remove_roles(role)
                    embed = discord.Embed(title="Your Moderator Trial Has Ended", description=f"{member.mention} your Moderator Trial has been ended early for more information as to why please contact an Admin." + '\n\nRunning CUBEBOT v1.0.0', color=discord.Colour.red())
                    await ctx.send(embed=embed)
                else:
                    embednot = discord.Embed(title="Not in Moderator Trial", description=f"{member.mention} in not in a Moderator Trial." + '\n\nRunning CUBEBOT v1.0.0', color=discord.Colour.red())
                    await ctx.send(embed=embednot)
                    return
    #----------
    @commands.command()
    @commands.has_any_role('Admin', 'Moderator', 'Trial Moderator')
    async def warn(self,ctx,  member: discord.Member, *, reason = None ):
        '''This command warns people when they are misbehaving'''
        embed = discord.Embed(title = "**Warn**", description = f'\n**{member.mention} Has Been Warned**', color=discord.Color.blue())
        embed.add_field (name = "Reason: ", value = reason + f'\n\nRunning CUBEBOT {BotVerson}', inline = False )
        await ctx.send(f"{member.mention}")
        await ctx.send(embed = embed) 
#-------------------------------------------------
def run():
    bot.add_cog(Pings(bot))
    bot.add_cog(Announcements(bot))
    bot.add_cog(Suggest_Report(bot))
    bot.add_cog(Miscellaneous(bot))
    bot.add_cog(Roles(bot))
    bot.add_cog(Admin(bot))
    bot.run("TOKEN")
#-------------------------------------------------
if __name__ == "__main__":
    run()
#-------------------------------------------------
#Things we want to add in the future
    '''#1 improved help command'''
    '''#2 improve/add swear warning'''
    #3 if you have any grade role you can't use any other grade command
    #4 Xp/level system
    '''#5 for any command that need an arg sending message to server not terminal'''
    '''#6 send message to server if unknown command is used'''
    #7 some sort of reward for leveling up with rng(more xp, xp multiplier)and with animation
    #8 more hello like commands
    '''#9 more game roles'''
    '#10 roll forward roles each year'
    #11 game status roles
    '''#12 bug report command'''