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
from pretty_help import PrettyHelp, Navigation
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
ending_note = "Running CUBEBOT v1.0.2"
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
#----------
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")
#-------------------------------------------------
class Announce(commands.Cog, description="These are the commands to make announcements."):
    #----------
    @commands.command(pass_context = True)
    async def Sa(self,ctx,arg):
        channel = bot.get_channel(807326547735347291)
        await channel.send('||@everyone||' + ' ' + '\n**Staff Announcment**' + '\n' + arg)
    #---------- 
    @commands.command(pass_context = True)
    async def ESa(self,ctx,arg):
        channel = bot.get_channel(807326547735347291) 
        await channel.send('||@everyone||' + ' ' + '\n**Esports Announcment**' + '\n' + arg)
    #---------- 
    @commands.command(pass_context = True)
    async def SAa(self,ctx,arg):
        channel = bot.get_channel(807326547735347291) 
        await channel.send('||@everyone||' + ' ' + '\n**Student Association Announcment**' + '\n' + arg)
#-------------------------------------------------
class Suggest_Report(commands.Cog, description="Theses are commands to make suggestions or report things."):
    #----------
    @commands.command(pass_context = True)
    async def bugreport(self,ctx,arg):
        channel = bot.get_channel(820102994292113409)
        channel2 = bot.get_channel(820103059870449685)
        embed = discord.Embed(title = 'Bug Report', description = '\n\n{**arg**}' + f'\n\n Bug Report initiated by {ctx.message.author}'+ '\n\nRunning CUBEBOT v1.0.1')
        await channel2.send(embed=embed)
        await channel.send("Your report has been logged!")
    #----------
    @commands.command(pass_context = True)
    async def botsuggest(self,ctx,arg):
        channel = bot.get_channel(801166288327016488)
        embed = discord.Embed(title = 'Bot Suggestion', description = f'\n\n**{arg}**' + f'\n\n Poll initiated by {ctx.message.author}'+ '\n\nRunning CUBEBOT v1.0.0')
        msg = await channel.send(embed=embed)
        emoji = ('⏫')
        emoji2 = ('⏬')
        await msg.add_reaction(emoji)
        await msg.add_reaction(emoji2)
    #----------
    @commands.command(pass_context = True)
    async def serversuggest(self,ctx,arg):
        channel = bot.get_channel(801166288327016488)
        embed = discord.Embed(title = 'Server Suggestion', description = f'\n\n**{arg}**' + f'\n\n Poll initiated by {ctx.message.author}'+ '\n\nRunning CUBEBOT v1.0.0')
        msg = await channel.send(embed=embed)
        emoji = ('⏫')
        emoji2 = ('⏬')
        await msg.add_reaction(emoji)
        await msg.add_reaction(emoji2)
#-------------------------------------------------
class Miscellaneous(commands.Cog, description="These are Miscellaneous commands."):
    @commands.command(pass_context = True)
    async def memberlist(self,ctx):
        member = '\n  '.join([member.name for member in ctx.guild.members])
        embed = discord.Embed(title = 'Members:', description = f'{member}' + '\n\nRunning CUBEBOT v1.0.0',color = 0xC0C0C0)
        await ctx.send (embed = embed)
    #----------
    @commands.command(pass_context = True)
    async def hello(self,ctx): 
        await ctx.send(f'Hello {ctx.message.author.mention}!')
#-------------------------------------------------
class Pings(commands.Cog, description="These are all the different Ping command."):
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('Warthunder')
    async def warthunder(self,ctx,arg):
        channel = bot.get_channel(801166288327016488)
        embed = discord.Embed(title = "**War Thunder LFT**", description = f'\n**{arg}**' + f"\n\n War Thunder LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.blue())
        await channel.send('||<@&808143642954956819>||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('COD')
    async def COD(self,ctx,arg):
        channel = bot.get_channel(801166288327016488)
        embed = discord.Embed(title = "**COD LFT**", description = f'\n**{arg}**' + f"\n\n COD LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.blue())
        await channel.send('||<@&808143642954956819>||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('CSGO')
    async def CSGO(self,ctx,arg):
        channel = bot.get_channel(801166288327016488)
        embed = discord.Embed(title = "**CSGO LFT**", description = f'\n**{arg}**' + f"\n\n CSGO LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.blue())
        await channel.send('||<@&808143642954956819>||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('Apex Legends')
    async def ApexLegends(self,ctx,arg):
        channel = bot.get_channel(801166288327016488)
        embed = discord.Embed(title = "**Apex Legends LFT**", description = f'\n**{arg}**' + f"\n\n Apex Legends LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.blue())
        await channel.send('||<@&808143642954956819>||')
        await channel.send(embed = embed)
    #----------     
    @commands.command(pass_context = True)
    @commands.has_role('League of Legends')
    async def LeagueofLegends(self,ctx,arg):
        channel = bot.get_channel(801166288327016488)
        embed = discord.Embed(title = "**League of Legends LFT**", description = f'\n**{arg}**' + f"\n\n League of Legends LFT initiated by {ctx.message.author}"+ '\n\nRunning CUBEBOT v1.0.0', color=discord.Color.blue())
        await channel.send('||<@&808143642954956819>||')
        await channel.send(embed = embed)
#-------------------------------------------------
class Roles(commands.Cog, description="These are all the commands that you use to get roles."):
    #----------
    @commands.command(pass_context = True)
    async def ninthgrade(self,ctx, member: discord.Member):
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
    @commands.command(pass_context = True)
    async def tenthgrade(self,ctx, member: discord.Member):
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
    @commands.command(pass_context = True)
    async def warthunderrole(self,ctx): 
        role = get(ctx.message.guild.roles, id = 808143642954956819)
        await ctx.send (f'{ctx.message.author.mention} you now have the War Thunder role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(pass_context = True)
    async def CODrole(self,ctx): 
        role = get(ctx.message.guild.roles, id = 817517518885355574)
        await ctx.send (f'{ctx.message.author.mention} you now have the COD role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(pass_context = True)
    async def CSGOrole(self,ctx): 
        role = get(ctx.message.guild.roles, id = 817517633908768848)
        await ctx.send (f'{ctx.message.author.mention} you now have the CSGO role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(pass_context = True)
    async def ApexLegendsrole(self,ctx): 
        role = get(ctx.message.guild.roles, id = 817517820857548832)
        await ctx.send (f'{ctx.message.author.mention} you now have the Apex Legends role!') 
        await ctx.message.author.add_roles(role)
    #----------
    @commands.command(pass_context = True)
    async def LeagueofLegendsrole(self,ctx): 
        role = get(ctx.message.guild.roles, id = 817518004514324521)
        await ctx.send (f'{ctx.message.author.mention} you now have the League of Legends role!') 
        await ctx.message.author.add_roles(role)
#-------------------------------------------------
class Admin(commands.Cog, description="These are commands for the staff of the server."):
    @commands.command()
    @commands.has_any_role('Moderator', 'Admin')
    async def mute(self,ctx, member: discord.Member, time: int, d, *, reason=None):
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
    @commands.command()
    @commands.has_any_role('Moderator', 'Admin')
    async def unmute(self,ctx, member: discord.Member):
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
    #----------
    @commands.command(pass_context = True)
    async def mod(self,ctx, member: discord.Member):
        guild = ctx.guild
        for role in guild.roles:
            if role in member.roles:
                role = get(ctx.message.guild.roles, id = 808710488547393578) 
                await ctx.message.author.add_roles(role)
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