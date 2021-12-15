import discord
from discord.ext import commands
from config import *
import requests
import json
import random

#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import db

cred = credentials.Certificate(firebase_authkey)
databaseApp = firebase_admin.initialize_app(cred, {
  'databaseURL': database_url
})

default = discord.Color.green()


msgcall_random = [
  "Boss",
  "Ano yun boss",
  "Amo",
  "Cute",
  "Hello pogi",
  "Master",
  "Magandang lalaki ka boss",
  "Hello boss amo master",
  "Hello cute",
  "uWuuu"
]

def get_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Miscellaneous?blacklistFlags=nsfw,racist&type=single")
  json_data = json.loads(response.text)
  joke = json_data["joke"]
  return (joke)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)

class Member(commands.Cog):
  def __init__(self, client):
    self.client = client
 
  @commands.Cog.listener()
  async def on_ready(self):
    print("importing member commands - Done!")

  @commands.command(pass_context=True, aliases=['inspire', 'quote'])
  async def _inspire(self, ctx):
    quote = get_quote()
    embed = discord.Embed(description = quote, color=discord.Color.purple())
    await ctx.send(embed=embed)

  @commands.command(pass_context=True, aliases=['joke'])
  async def _joke(self, ctx):
    jokes = get_joke()
    embed = discord.Embed(description=jokes, color=discord.Color.gold())
    await ctx.send(embed=embed)

  @commands.command(pass_context=True, aliases=['avatar', 'profile'])
  async def _avatar(self, ctx, member: discord.Member=None):
    if not member:
      member = ctx.message.author
      
      embed = discord.Embed(color = member.colour)
      embed.set_image(url='{}'.format(member.avatar_url))
      msg = await ctx.send(embed = embed)
      await msg.add_reaction('👍')
    else:
      embed = discord.Embed(color = member.colour)
      embed.set_image(url='{}'.format(member.avatar_url))
      msg = await ctx.send(embed = embed)
      await msg.add_reaction('👍')

  #async def avatar(ctx, *, member: discord.Member=None): # set the member object to None
  #  if not member: # if member is no mentioned
  #      member = ctx.message.author # set member as the author
  #  userAvatar = member.avatar_url
  #  await ctx.send(userAvatar)
  
  @commands.command(pass_context=True, aliases=['info'])
  async def _info(self, ctx, member: discord.Member=None):
    
    if not member:
      member = ctx.message.author

      embed = discord.Embed(title = "User Information", color = member.colour) 
      embed.set_thumbnail(url='{}'.format(member.avatar_url))
      embed.add_field(name="ID", value=member.id, inline=False)
      embed.add_field(name="Name", value=str(member), inline=True)
      embed.add_field(name="Role", value=member.top_role.mention, inline=True)
      embed.add_field(name="Status", value=str(member.status).title(), inline=True)
      embed.add_field(name="Created at", value=member.created_at.strftime("%m/%d/%Y %H:%M %p"), inline=True)
      embed.add_field(name="Joined at", value=member.joined_at.strftime("%m/%d/%y %H:%M %p"), inline=True)
      embed.add_field(name = ":video_game: Activity", value = None if ctx.guild is None or member.activity is None else member.activity.name, inline=False)
      
      if bool(member.premium_since) == True:
        embed.add_field(name=":gem:  Premium", value="Since {}".format(member.premium_since), inline=True)
      else:
        embed.add_field(name=":gem:  Premium", value=bool(member.premium_since), inline=True)
      
      await ctx.send(embed=embed)

    else:
      #timestamp = atetime.utcnow()
      embed = discord.Embed(title = "User Information", color = member.colour) 
      embed.set_thumbnail(url='{}'.format(member.avatar_url))
      embed.add_field(name="ID", value=member.id, inline=False)
      embed.add_field(name="Name", value=str(member), inline=True)
      embed.add_field(name="Role", value=member.top_role.mention, inline=True)
      embed.add_field(name="Status", value=str(member.status).title(), inline=True)
      embed.add_field(name="Created at", value=member.created_at.strftime("%m/%d/%Y %H:%M %p"), inline=True)
      embed.add_field(name="Joined at", value=member.joined_at.strftime("%m/%d/%y %H:%M %p"), inline=True)
      embed.add_field(name = ":video_game: Activity", value = None if ctx.guild is None or member.activity is None else member.activity.name)

      if bool(member.premium_since) == True:
        embed.add_field(name=":gem:  Premium", value="Since {}".format(member.premium_since), inline=True)
      else:
        embed.add_field(name=":gem:  Premium", value=bool(member.premium_since), inline=True)
      
      await ctx.send(embed=embed)

  @commands.command(pass_context=True, aliases = ['setcall']) 
  async def _saveOnFirebase(self, ctx, *, alias:str):
    getUser = ctx.message.author

    if not alias:      
      embed = discord.Embed(description="> Use !setcall [aliases] to continue")
      await ctx.send(embed = embed)
    else:
      ref = db.reference("/Members/Aliases")
      ref.update({
        getUser.id: {
          "Alias": alias,
          "Name": getUser.name
        }
      })
      await ctx.send("Aliases has been saved")
      
  @commands.command(pass_context=True, aliases = ['getcall']) 
  async def _getcall(self, ctx):
    ref = db.reference(f'/Members/Aliases/Alias')
    alias = ref.get()
    await ctx.send(alias)
      

def setup(bot):
  bot.add_cog(Member(bot))