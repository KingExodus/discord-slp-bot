import discord
from discord.ext import commands
import requests
import json
import random
from googletrans import Translator

#pip install googletrans==3.1.0a0
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
encouragements = [
  "Cheer up!",
  "Dont be sad",
  "Kaya mo yan!",
  "Andito lang ako kapag kelangan mo ng kausap",
  "You are a great person!",
]

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
  "uWuuu",
]

ema = 769527881440952320
uwu = 761795281254612992
tirdz = 715574676029440101
sandra = 748447987402932227

foul_words = [
"fuck you", 
"fuck", 
"motherfucker", 
"tang ina mo", 
"pota", 
"potah", 
"king ina", 
"inamo",
"ina mo",
"inamoka", 
"ina mo ka", 
"jabul", 
"bulbol",
"taena",
"potaena",
"pakyu",
"gago",
"tarantado",
"siraulo",
"kingina",
"kinginamo",
"pakyuall",
"namoka",
"tangina",
"tanginamo",
"tangina mo",
"pakyuka",
"pakyu ka",
"jabol",
"online jabol",
"jabulan",
"puwet",
"kilikili",
"putangina",
"putang ina",
"kupal",]

kilig_words = [
"labyu",
"labyuall",
"labyu all",
"hateu",
"hate u",
"hate you",
"hateuall",
"hate u all",
"hate you all",
"iloveyou",
"iloveyouall",
"i love you",
"i luv u",
"i lab u",
"i love you all",]

class Message(commands.Cog):
  def __init__(self, client):
    self.client = client
 
  @commands.Cog.listener()
  async def on_ready(self):
    print("importing messages - Done!")

  @commands.command(pass_context=True, aliases=['name'])
  async def _name(self, ctx, member: discord.Member = None):
    username = member.id
   

    if not member:
      embed = discord.Embed(description="Not found!")
      await ctx.send(embed=embed)

    if username == tirdz:
      await ctx.send("Hello " + ctx.author.display_name + ", ~~Ti R Dz~~ was not here at the moment!")
    #elif username == uwu:
    #  await ctx.send("Hello cute!")
    elif username == sandra:
      await ctx.send("Isubo mo! Kainin mo!")
    elif username == ema:
      await ctx.send("Boss amo master na maganda!")
    else:
      await ctx.send(random.choice(msgcall_random) + "!")

  @commands.command(pass_context=True, aliases=['translate'])
  async def _translate(ctx, lang, *, words):
      translator = Translator()
      translation = translator.translate(words, dest=lang)
      await ctx.send(translation.text)

  @commands.Cog.listener()
  async def on_message(self, message):
    #if message.author == self.user:
    #  return

    msg = message.content.lower()
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(encouragements))

    if any(word in msg for word in foul_words):
      #if badword in msg.content.lower():
      await message.channel.send(f"⛔️ {message.author.mention} Last mo na yan, huwag mo subukan!")
      await message.delete()

    if any(word in msg for word in kilig_words):
      #if badword in msg.content.lower():
      uwunatics = f"<@{uwu}>"
      await message.channel.send(f"❤️ {message.author.mention} i-pm mo nalang, bawal landian sabi ni {uwunatics}!")
      await message.delete()


def setup(bot):
  bot.add_cog(Message(bot))