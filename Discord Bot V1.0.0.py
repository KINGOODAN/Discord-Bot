#CUBE DISCORD BOT V1.1.0
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
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
ROLEc = 'Cubeular'
ROLEm = 'Muted'
ROLE9 = '9th Grader'
ROLE10 = '10th Grader'
#----------
intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)
client = discord.Client
bot = commands.Bot(command_prefix='?', intents = intents)
bot.remove_command('help')
#-------------------------------------------------
ending_note = "Running CUBEBOT v1.1.0"
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
    channel = bot.get_channel (712437956815618071) 
    embed = discord.Embed(title = 'User Has Joined the Server:sunglasses:', description = f'\n{member} has joined us!' + '\n\nRunning CUBEBOT v1.1.0', color = 0xC0C0C0)
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
    await bot.change_presence(activity=discord.Game('CUBEBOT Build v1.1.0! \n Github==> https://github.com/KINGOODAN/Discord-Bot'))
#----------
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel (712437956815618071) 
    embed = discord.Embed(title = 'User Has Left the Server:ghost: ', description = f'\n{member} has left us. Hope they rejoin later!' + '\n\nRunning CUBEBOT v1.1.0', color = 0xC0C0C0)
    await channel.send(embed = embed)
#----------
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")
#-------------------------------------------------
class Announce(commands.Cog, description="These are the commands to make announcements."):
    #----------
    @commands.command(pass_context = True)
    @commands.has_any_role('Moderator', 'Admin')
    async def Sa(self,ctx,arg):
        '''An announcement command for staff.'''
        channel = bot.get_channel(783107953095213086)
        await channel.send('||@everyone||' + ' ' + '\n**Staff Announcement**' + '\n' + arg)
    #---------- 
    @commands.command(pass_context = True)
    @commands.has_role('Esports Coordinator')
    async def ESa(self,ctx,arg):
        '''An announcement command for E-Sports.'''
        channel = bot.get_channel(783107953095213086) 
        await channel.send('||@everyone||' + ' ' + '\n**Esports Announcement**' + '\n' + arg)
    #---------- 
    @commands.command(pass_context = True)
    @commands.has_any_role('Student Association', 'Advisory Senator')
    async def SAa(self,ctx,arg):
        '''An announcement command for Student Association.'''
        channel = bot.get_channel(783107953095213086) 
        await channel.send('||@everyone||' + ' ' + '\n**Student Association Announcement**' + '\n' + arg)
#-------------------------------------------------
class Suggest_Report(commands.Cog, description="Theses are commands to make suggestions or report things."):
    #----------
    @commands.command(pass_context = True)
    async def bugreport(self,ctx,arg):
        '''A command that allows you to report bug with the bot.'''
        channel = bot.get_channel(820104608956678144)
        channel2 = bot.get_channel(820102051866476565)
        embed = discord.Embed(title = 'Bug Report', description = '\n\n{**arg**}' + f'\n\n Bug Report initiated by {ctx.message.author}'+ '\n\nRunning CUBEBOT v1.1.0')
        await channel2.send(embed=embed)
        await channel.send("Your report has been logged!")
    #----------
    @commands.command(pass_context = True)
    async def botsuggest(self,ctx,arg):
        '''A command that lets you make suggestions about the bot.'''
        channel = bot.get_channel(786727940125753374)
        embed = discord.Embed(title = 'Bot Suggestion', description = f'\n\n**{arg}**' + f'\n\n Poll initiated by {ctx.message.author}'+ '\n\nRunning CUBEBOT v1.1.0')
        msg = await channel.send(embed=embed)
        emoji = ('⏫')
        emoji2 = ('⏬')
        await msg.add_reaction(emoji)
        await msg.add_reaction(emoji2)
    #----------
    @commands.command(pass_context = True)
    async def serversuggest(self,ctx,arg):
        '''A command that lets you make suggestions about the server.'''
        channel = bot.get_channel(786727940125753374)
        embed = discord.Embed(title = 'Server Suggestion', description = f'\n\n**{arg}**' + f'\n\n Poll initiated by {ctx.message.author}'+ '\n\nRunning CUBEBOT v1.1.0')
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
        embed = discord.Embed(title = 'Members:', description = f'{member}' + '\n\nRunning CUBEBOT v1.1.0',color = 0xC0C0C0)
        await ctx.send (embed = embed)
    #----------
    @commands.command(pass_context = True)
    async def hello(self,ctx): 
        '''A fun command that say Hello.'''
        await ctx.send(f'Hello {ctx.message.author.mention}!')
#-------------------------------------------------
class Roles(commands.Cog, description="These are all the commands that you use to get roles."):
    #----------
    @commands.command(pass_context = True)
    async def ninthgrade(self,ctx, member: discord.Member):
        '''This command give you the Ninth Grader role.'''
        guild = ctx.guild
        for role in guild.roles:
            if role.name == "10th Grader":
                embedalreadyhavegrade = discord.Embed(title="You Already have a grade", description=f"{member.mention} you already have a grade " + '\n\nRunning CUBEBOT v1.1.0', color=discord.Colour.red())
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
                embedalreadyhavegrade = discord.Embed(title="You Already have a grade", description=f"{member.mention} you already have a grade " + '\n\nRunning CUBEBOT v1.1.0', color=discord.Colour.red())
                if role in member.roles:
                    await ctx.send(embed=embedalreadyhavegrade)
                else:
                    role = get(ctx.message.guild.roles, id = 784556769799962625)
                    await ctx.send (f'{ctx.message.author.mention} you now have the 10th Grade role!') 
                    await ctx.message.author.add_roles(role)
    #----------
    @commands.command(pass_context = True)
    async def WarThunderrole(self,ctx):
        '''This command give you the War Thunder role.'''
        role = get(ctx.message.guild.roles, id = 818603292120580106)
        await ctx.send (f'{ctx.message.author.mention} you now have the War Thunder role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(pass_context = True)
    async def CODrole(self,ctx): 
        '''This command give you the COD role.'''
        role = get(ctx.message.guild.roles, id = 818603436593381406)
        await ctx.send (f'{ctx.message.author.mention} you now have the COD role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(pass_context = True)
    async def CSGOrole(self,ctx): 
        '''This command give you the CSGO role.'''
        role = get(ctx.message.guild.roles, id = 818603636002127903)
        await ctx.send (f'{ctx.message.author.mention} you now have the CSGO role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(pass_context = True)
    async def ApexLegendsrole(self,ctx):
        '''This command give you the Apex Legends role.''' 
        role = get(ctx.message.guild.roles, id = 818603693314277376)
        await ctx.send (f'{ctx.message.author.mention} you now have the Apex Legends role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(pass_context = True)
    async def LeagueofLegendsrole(self,ctx): 
        '''This command give you the League of Legends role.'''
        role = get(ctx.message.guild.roles, id = 818603798749511680)
        await ctx.send (f'{ctx.message.author.mention} you now have the League of Legends role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(pass_context = True)
    async def SuperSmashBrosrole(self,ctx): 
        '''This command give you the Super Smash Bros role.'''
        role = get(ctx.message.guild.roles, id = 818975670972841995)
        await ctx.send (f'{ctx.message.author.mention} you now have the SuperSmashBros role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(pass_context = True)
    async def RainbowSixSiegerole(self,ctx): 
        '''This command give you the Rainbow Six Siege role.'''
        role = get(ctx.message.guild.roles, id = 818975587527950377)
        await ctx.send (f'{ctx.message.author.mention} you now have the RainbowSixSiege role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(pass_context = True)
    async def Overwatchrole(self,ctx): 
        '''This command give you the Overwatch role.'''
        role = get(ctx.message.guild.roles, id = 818975708708864013)
        await ctx.send (f'{ctx.message.author.mention} you now have the Overwatch role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(pass_context = True)
    async def BF1role(self,ctx): 
        '''This command give you the BF1 role.'''
        role = get(ctx.message.guild.roles, id = 819783988721745942)
        await ctx.send (f'{ctx.message.author.mention} you now have the BF1 role!') 
        await ctx.message.author.add_roles(role)
#-------------------------------------------------
class Pings(commands.Cog, description="These are all the different Ping command."):
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('War Thunder')
    async def WarThunderping(self,ctx,arg):
        '''This command pings people with your message with the War Thunder role'''
        channel = bot.get_channel(758445986816589874)
        embed = discord.Embed(title = "**War Thunder LFT**", description = f'\n**{arg}**' + f"\n\n War Thunder LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.1.0', color=discord.Color.blue())
        await channel.send('||<@&808143642954956819>||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('COD')
    async def CODping(self,ctx,arg):
        '''This command pings people with your message with the COD role'''
        channel = bot.get_channel(758445986816589874)
        embed = discord.Embed(title = "**COD LFT**", description = f'\n**{arg}**' + f"\n\n COD LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.1.0', color=discord.Color.blue())
        await channel.send('||<@&808143642954956819>||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('CSGO')
    async def CSGOping(self,ctx,arg):
        '''This command pings people with your message with the CSGO role'''
        channel = bot.get_channel(758445986816589874)
        embed = discord.Embed(title = "**CSGO LFT**", description = f'\n**{arg}**' + f"\n\n CSGO LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.1.0', color=discord.Color.blue())
        await channel.send('||<@&808143642954956819>||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('Apex Legends')
    async def ApexLegendsping(self,ctx,arg):
        '''This command pings people with your message with the Apex Legends role'''
        channel = bot.get_channel(758445986816589874)
        embed = discord.Embed(title = "**Apex Legends LFT**", description = f'\n**{arg}**' + f"\n\n Apex Legends LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.1.0', color=discord.Color.blue())
        await channel.send('||<@&808143642954956819>||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('League of Legends')
    async def LeagueofLegendsping(self,ctx,arg):
        '''This command pings people with your message with the League of Legends role'''
        channel = bot.get_channel(758445986816589874)
        embed = discord.Embed(title = "**League of Legends LFT**", description = f'\n**{arg}**' + f"\n\n League of Legends LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.1.0', color=discord.Color.blue())
        await channel.send('||<@&808143642954956819>||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('SuperSmashBros')
    async def SuperSmashBrosping(self,ctx,arg):
        '''This command pings people with your message with the Super Smash Bros role'''
        channel = bot.get_channel(758445986816589874)
        embed = discord.Embed(title = "**SuperSmashBros LFT**", description = f'\n**{arg}**' + f"\n\n SuperSmashBros LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.1.0', color=discord.Color.blue())
        await channel.send('||<@&808143642954956819>||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('RainbowSixSiege')
    async def RainbowSixSiegeping(self,ctx,arg):
        '''This command pings people with your message with the Rainbow Six Siege role'''
        channel = bot.get_channel(758445986816589874)
        embed = discord.Embed(title = "**RainbowSixSiege LFT**", description = f'\n**{arg}**' + f"\n\n RainbowSixSiege LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.1.0', color=discord.Color.blue())
        await channel.send('||<@&808143642954956819>||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('Overwatch')
    async def Overwatchping(self,ctx,arg):
        '''This command pings people with your message with the Overwatch role'''
        channel = bot.get_channel(758445986816589874)
        embed = discord.Embed(title = "**Overwatch LFT**", description = f'\n**{arg}**' + f"\n\n Overwatch LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.1.0', color=discord.Color.blue())
        await channel.send('||<@&808143642954956819>||')
        await channel.send(embed = embed)
    #----------
    @commands.command(pass_context = True)
    @commands.has_role('BF1role')
    async def BF1ping(self,ctx,arg):
        '''This command pings people with your message with the BF1 role'''
        channel = bot.get_channel(758445986816589874)
        embed = discord.Embed(title = "**BF1 LFT**", description = f'\n**{arg}**' + f"\n\n BF1 LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.1.0', color=discord.Color.blue())
        await channel.send('||<@&808143642954956819>||')
        await channel.send(embed = embed)
#-------------------------------------------------
class Admin(commands.Cog, description="These are commands for the staff of the server."):
    #----------
    @commands.command()
    @commands.has_any_role('Moderator', 'Admin')
    async def mute(self,ctx, member: discord.Member, time: int, d, *, reason=None):
        '''A command to mute members.'''
        guild = ctx.guild
        for role in guild.roles:
            if role.name == "Muted":
                embedalreadymuted = discord.Embed(title="Already Muted", description=f"{member.mention} is already muted " + '\n\nRunning CUBEBOT v1.1.0', color=discord.Colour.red())
                if role in member.roles:
                    await ctx.send(embed=embedalreadymuted)
                else:
                    await member.add_roles(role)
                    embed = discord.Embed(title="Muted!", description=f"{member.mention} has been muted ", colour=discord.Colour.red())
                    embed.add_field(name="Reason:", value=reason, inline=False)
                    embed.add_field(name="Time left for the mute:", value=f'{time} {d}' + '\n\nRunning CUBEBOT v1.1.0', inline=False)
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
                        embed = discord.Embed(title="Unmuted ", description=f"{member.mention} your mute time is up." + '\n\nRunning CUBEBOT v1.1.0', color=discord.Colour.red())
                        await ctx.send(embed=embed)
                    else:
                        return
    #----------
    @commands.command()
    @commands.has_any_role('Moderator', 'Admin')
    async def unmute(self,ctx, member: discord.Member):
        '''A command to unmute member who are muted.'''
        guild = ctx.guild
        for role in guild.roles:
            if role.name == "Muted":
                if role in member.roles:
                    await member.remove_roles(role)
                    embed = discord.Embed(title="unmuted ", description=f"{member.mention} you have been unmuted" + '\n\nRunning CUBEBOT v1.1.0', color=discord.Colour.red())
                    await ctx.send(embed=embed)
                else:
                    embednot = discord.Embed(title="Not Muted", description=f"{member.mention} is not muted." + '\n\nRunning CUBEBOT v1.1.0', color=discord.Colour.red())
                    await ctx.send(embed=embednot)
                    return
#-------------------------------------------------
def run():
    bot.add_cog(Pings(bot))
    bot.add_cog(Announce(bot))
    bot.add_cog(Suggest_Report(bot))
    bot.add_cog(Miscellaneous(bot))
    bot.add_cog(Roles(bot))
    bot.add_cog(Admin(bot))
    bot.run('YOUR BOT TOKEN')
#-------------------------------------------------
if __name__ == "__main__":
    run()
#-------------------------------------------------
# BOT TOKEN FOR BESTS SERVER ''
#Thimgs we want to add in the future
'''#1 improved help command'''
#2 improve/add swear warning
#3 if you have any grade role you can't use any other grade command
#4 Xp/level system
#5 for any command that need an arg sending message to server not terminal
'''#6 send message to server if unknown command is used'''
#7 some sort of reward for leveling up with rng(more xp, xp multiplier)and with animation
#8 more hello like commands
'''#9 more game roles'''
#10 roll forward roles each year
#11 game status roles
'''#12 bug report command'''