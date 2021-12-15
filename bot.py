import discord
from discord.ext import commands
import os
from config import *
#from keep_alive import keep_alive

#import heistbot
#import member
import helps
import crypto
#import music
#import welcome
#import spotify
#import moderation
#import messages

#import nacl
import platform

default = discord.Color.blue()

try:
  import nacl
  import platform
except ImportError:
  try:
    if platform.system().lower().startswith('win'):
      os.system("pip install --upgrade pip")    
      os.system("pip install pynacl")
      os.system("pip install discord.py[voice]")
      #os.system("pip install pymongo[srv]")
    else:
      os.system("pip install --upgrade pip")
      os.system("pip install pynacl")
      os.system("pip install discord.py[voice]")
      #os.system("pip install pymongo[srv]")
  except Exception as e:
    print("Error:", e)
    exit()

#keep_alive()
cogs = [helps, crypto]
#cogs = [heistbot, member, helps, crypto, moderation, messages] #importing modules
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = PREFIX, description ="Online ako kili-kili!", intents = intents)
bot.remove_command('help')

for module in range(len(cogs)):
  cogs[module].setup(bot)
  print("Setup successfully initialized.")

@bot.event
async def on_ready():
  print("I'm alive and logged in as {0.user}".format(bot))

#@bot.command(pass_context=True) #firebase write
#async def firebase(ctx, color: str):
#  print("Pick a color")
#  colors = color
#  user = ctx.message.author.id
#  ref = db.reference(f"/")
#  ref.update({
#    user: {
#      "Color": str(colors)
#    }
#  })

@bot.command()
async def test(ctx):
  embed = discord.Message.Embed(title ="Cleared all recent messages")
  
  await ctx.send(embed = embed)


#keep_alive()
bot.run(TOKEN, bot=True, reconnect=True)
