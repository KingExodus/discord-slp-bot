import discord
from discord.ext import commands
import os
import requests
import json
from random import choice


default = discord.Color.blue()

#api_key = os.environ.get('binance_api')
#api_secret = os.environ.get('binance_secret')
#client_binance = Client(api_key, api_secret)

all_tokens = requests.get("https://api.coingecko.com/api/v3/coins/list")
all_tokens_json = all_tokens.json()

unknown_coin = ["Unknown coin.", "Coin not found.", "Invalid coin."]
unknown_coin_2 = [
    "Baka na typo ka lang.", "Ayusin mo mali.", "Paulit-ulit ka, ayusin mo."
]

def repsonse_to_string(response):
  data = {}
  data[
    'status_maintenance'] = ':green_circle: No Maintenance' if not response[
    'status_maintenance'] else ':red_circle: Maintenance undergoing'
  data['status_battles'] = get_battle_status(response['status_battles'])
  data['status_graphql'] = ':green_circle: Game servers OK' if response[
    'status_graphql'] else ':red_circle: Game servers Offline'
  data['status_cloudflare'] = ':green_circle: Marketplace OK' if response[
    'status_cloudflare'] else ':red_circle: Marketplace Offline'
  return data

def get_battle_status(status):
  if (status == 0): return ':green_circle: Battle servers OK'
  if (status == 1):
    return ':yellow_circle: Battle servers running with restrictions'
  if (status == 2): return ':black_circle: Battle servers offline'
  else: return ':red_circle: Undefined Status'

def usage_msg(cmd, usage):
  return '**Usage**: {0} {1}'.format(cmd, usage)

#def get_coin(code):
#  query = client_binance.get_symbol_ticker(symbol=code.upper() + "USDT")
#  return query


class Heistcommands(commands.Cog):
  def __init__(self, client):
    self.client = client
 
  @commands.Cog.listener()
  async def on_ready(self):
    print("importing crypto commands - Done!")

  # AXIE INFINITY API #
  @commands.group(invoke_without_command=True)
  async def axie(self, ctx):
    await ctx.send("Use `!axie status` to show game server status of axie infinty")

  @axie.command(pass_context=True, aliases=['status', 'stats'])
  async def _server(self, ctx):
    response = requests.get('https://axie.zone:3000/server_status', verify=False)
    json_data = repsonse_to_string(json.loads(response.text))

    embed = discord.Embed(title="Axie Infinity Server Status", color=default)
    embed.set_thumbnail(url="https://www.cryptonewsz.com/wp-content/uploads/2021/07/Axie-Infinity-Price-Analysis.jpg")
    embed.add_field(name="**Maintenance**", value=json_data['status_maintenance'], inline=False)
    embed.add_field(name="**Battle Server**", value=json_data['status_battles'], inline=False)
    embed.add_field(name="**Marketplace**", value=json_data['status_cloudflare'], inline=False)
    embed.add_field(name="**Game API Server**", value=json_data['status_graphql'], inline=False)
    embed.set_footer(text="Source: Axie Infinity")
    await ctx.send(embed=embed)

  # COINGECKO API #
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
  # BINANCE API #
  @commands.command(pass_context=True, aliases=['bnbprice'])
  async def _bnb(self, ctx, coin: str = None):
    # Getting crypto price from Binance then sending it to chat.
    if not coin:
      await ctx.send("Lagyan mo ng token bobo.")
    else:
      try:
        coin_pair = get_coin(coin)
      except:
        await ctx.send(f"{choice(unknown_coin)} {choice(unknown_coin_2)}", mention_author=False)

      else:
        price_usd = float(coin_pair.get('price'))
        price_php = price_usd * 50
        #await ctx.send("**{0}** Price: ${1} ≈ P{2}\n{3}".format(coin.upper(), str(price_usd), str(round(price_php,2)), dt_string))

        title = f'{coin.upper()}'
        color = discord.Color.gold()

        commands_embed = discord.Embed(title=title, description="", color=color)
        commands_embed.set_thumbnail(url="https://i.ytimg.com/vi/JNU5S97ev8M/hqdefault.jpg")
        commands_embed.add_field(name="Price", value=f'$ {price_usd}', inline=False)
        commands_embed.add_field(name="Php", value=f'₱ {price_php}', inline=False)
        commands_embed.set_footer(text="Source: Binance")
        await ctx.send(embed=commands_embed)
  

  @commands.command(pass_context=True, aliases=['calc'])
  async def _calc(self, ctx, coin: str = None, usd_sellprice: float = None):
    # Calculating how much ETH to sell Axie for based on USD value
    if not coin or not usd_sellprice:
      await ctx.send("Lagyan mo ng token at presyo.")
    else:
      try:
        coin_pair = get_coin(coin)

      except:
        await ctx.send(f"{choice(unknown_coin)} {choice(unknown_coin_2)}", mention_author=False)

      else:
        coin_price_usd = float(coin_pair.get('price'))

        coin_price_php = usd_sellprice / 50
        #result = usd_sellprice/coin_price_usd
        result = coin_price_php / coin_price_usd

        #await ctx.send("${0} = {1} {2}".format(str(usd_sellprice), str(round(result, 4)), coin.upper()))

        title = f'{coin.upper()}'
        #description = f'{name}'
        color = discord.Color.gold()

        commands_embed = discord.Embed(title=title, description="", color=color)
        commands_embed.set_thumbnail(url="https://i.ytimg.com/vi/JNU5S97ev8M/hqdefault.jpg")
        commands_embed.add_field(name="Price", value=f'Php {usd_sellprice}', inline=False)
        commands_embed.add_field(name="Value", value=f' {round(result,4)}' + coin.upper(), inline=False)
        commands_embed.set_footer(text="Source: Binance")

        await ctx.send(embed=commands_embed)
  """

def setup(commands):
  commands.add_cog(Heistcommands(commands))