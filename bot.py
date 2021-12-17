#import disnake
#from disnake.ext import commands
#from disnake import ApplicationCommandInteraction
import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand
from config import *

import requests
import json

bot = commands.Bot(command_prefix=PREFIX)
guild_ids = [832750290767708170]
#guild_ids = bot.get_guild(constants.Guild.id)
#guild_ids = []
twitch_url="youtube.com"

slash=SlashCommand(bot, sync_commands=True)

all_tokens = requests.get("https://api.coingecko.com/api/v3/coins/list")
all_tokens_json = all_tokens.json()

@bot.event
async def on_ready(): 
  symbol = "slp" #ctx.message.content.lower().split()[1]
  index = next((i for i, item in enumerate(all_tokens_json) 
  if item["symbol"] == symbol), None)
  if index != None:
    id = all_tokens_json[index]["id"]
    name = all_tokens_json[index]["name"]

    response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=php,usd"
            .format(all_tokens_json[index]["id"]))
    response_json = response.json()
    price = "{:,.8f}".format(response_json[id]["usd"]).rstrip("0").rstrip(".")
    php = "{:,.8f}".format(response_json[id]["php"]).rstrip("0").rstrip(".")
            
    #title = f'{symbol.upper()}'
    #description = f'{name}'
    #➘ ➚ ⤴ ⤵ ⇗ ⇘ ↘ ↗
    
    tagname = "{0.user}".format(bot)
    bot.user.edit(username=tagname)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{symbol.upper()} ${price}"))
        

  #Playing
  #await bot.change_presence(activity=discord.Game(name=f"in 1000 servers")) #{len(bot.guilds)}
  #Streaming
  #await bot.change_presence(activity=discord.Streaming(name=f"My Stream", url=twitch_url))
  #Listening
  #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
  #Watching
  #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

  #await bot.edit(nick="testthing")
  print("I'm alive and logged in as {0.user}".format(bot))

@bot.event # This event runs whenever a user updates: status, game playing, avatar, nickname or role
async def on_member_update(before, after): 
    n = after.nick 
    if n: # Check if they updated their username
        if n.lower().count("Oasis") > 0: # If username contains tim
            last = before.nick
            if last: # If they had a usernae before change it back to that
                await after.edit(nick="last")
            else: # Otherwise set it to "NO STOP THAT"
                await after.edit(nick="NO STOP THAT")

#@bot.slash_command(
@slash.slash(
  name='pong',
  description='Sends back bot latencey.'
  )
#async def pong(inter: ApplicationCommandInteraction):
async def pong(ctx):
  #embed = disnake.Embed(
  embed = discord.Embed(
    title='Pong :ping_pong:',
    description=f'Latency: {round(bot.latency*1000)}ms'
  )

  #return await inter.send(embed=embed, ephemeral=True) #response()
  return await ctx.send(embed=embed)

"""
@commands.command(pass_context=True, aliases=['price'])
  async def _coingecko(self, ctx):
    if len(ctx.message.content.split()) == 2:
      symbol = ctx.message.content.lower().split()[1]
      index = next((i for i, item in enumerate(all_tokens_json) 
      if item["symbol"] == symbol), None)
      if index != None:
        id = all_tokens_json[index]["id"]
        name = all_tokens_json[index]["name"]

        response = requests.get(
          "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=php,usd"
          .format(all_tokens_json[index]["id"]))
        response_json = response.json()
        price = "{:,.8f}".format(response_json[id]["usd"]).rstrip("0").rstrip(".")
        php = "{:,.8f}".format(response_json[id]["php"]).rstrip("0").rstrip(".")
           
        title = f'{symbol.upper()}'
        description = f'{name}'
        color = discord.Color.green()

        commands_embed = discord.Embed(title=title, description=description, color=color)
        commands_embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1qCcyuRCGMQXS38p_iwJCXQ32FnEBVExlDmFIytBYFTBpDzW0KH6n02xwLnZs5n2dd-E&usqp=CAU")
        commands_embed.add_field(name="Price", value=f'$ {price}', inline=False)
        commands_embed.add_field(name="Php", value=f'₱ {php}', inline=False)
        commands_embed.set_footer(text="Source: Coingecko")
        await ctx.send(embed=commands_embed, mention_author=False)
        
      else:
        await ctx.send(f"{choice(unknown_coin)} {choice(unknown_coin_2)}", mention_author=False)

    elif len(ctx.message.content.split()) == 1:
      await ctx.send("Lagyan mo ng token.")
    else:
      await ctx.send("Too many parameters. Isa-isa lang uyyy.")
"""

try:
  bot.run(TOKEN)
except Exception as error:
  print(f'Failed to start bot.\n\nInfo:\n{error}')