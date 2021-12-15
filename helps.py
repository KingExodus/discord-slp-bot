import discord
from discord.ext import commands

default = discord.Color.red()

class Helps(commands.Cog):
  def __init__(self, client):
    self.client = client
 
  @commands.Cog.listener()
  async def on_ready(self):
    print("importing help commands - Done")
  """"
  @commands.before_slash_command_invoke
  async def slash_command_handler(interaction):
    interaction_data = parse_interaction(interaction)
    if used_commands == []:
      used_commands.append(parse_interaction(interaction))
    else:
      if used_commands[len(used_commands)-1] != interaction_data:
        used_commands.append(parse_interaction(interaction))

    if interaction.author.id in blacklisted_users:
      await interaction.response.send_message(functions.get_text(interaction.author.id, "banned_message"), ephemeral=True)
      raise Exception("no permission")

    if not interaction.guild:
      await interaction.response.send_message(functions.get_text(interaction.author.id, "use_in_server"))
      raise Exception("no permission")

    if interaction.data.name in variables.owner_commands and interaction.author.id not in variables.bot_owners:
      await interaction.response.send_message(functions.get_text(interaction.author.id, "not_bot_owner"), ephemeral=True)
      raise Exception("no permission")

    if get_cooldown(interaction.author.id, interaction.data.name) > 0:
      cooldown_string = generate_cooldown(
            interaction.author.id,
            interaction.data.name,
            get_cooldown(interaction.author.id, interaction.data.name),
        )
      embed = disnake.Embed(title=functions.get_text(interaction.author.id, "command_cooldown"), description=cooldown_string, color=variables.embed_color)
      await interaction.response.send_message(embed=embed, ephemeral=True)
      raise Exception("no permission")

    variables.last_command = time.time()
    if interaction.data.name != "afk":
      afk_key = f"afk.{interaction.author.id}".encode("utf-8")
      if afk_key in database.keys():
        del database[afk_key]
        try:
          await interaction.author.send(functions.get_text(interaction.author.id, "afk_removed"))
        except:
          pass
    if interaction.data.name == "text":
      if not interaction.author.guild_permissions.administrator:
        try:
          try:
            ignored_channels = json.loads(database[f"filter-ignore.{interaction.guild.id}"])
          except:
            ignored_channels = {"insults": []}
          if interaction.channel.id not in ignored_channels["insults"]:
            if json.loads(database[f"insults.toggle.{interaction.guild.id}"]):
              insults = json.loads(database[f"insults.list.{interaction.guild.id}"])
              for word in insults:
                if word.lower() in interaction.data.options[0].options[0].value.replace(" ", ""):
                  await interaction.response.send_message(f'Please do not use the word **"{word.lower()}"** in this server!', ephemeral=True)
                  raise Exception("no permission")
        except:
          pass

  @client.slash_command(name="helps", description="Get started with Doge Utilities")
  async def help_command(interaction):
    await help_paginator.start(interaction)
    add_cooldown(interaction.author.id, "help", 30)
  """
  @commands.group(invoke_without_command=True)
  #@commands.slash_command(name="help", description="Get started with Doge Utilities")
  async def help(self, ctx):
    name = str(ctx.guild.name)
    #icon = str(ctx.guild.icon_url)
    icon = "https://m.media-amazon.com/images/I/71I9zJauHfL._SS500_.jpg" 
    embed = discord.Embed(title="**{0} Plugins Commands**".format(name), color = default)
    embed.set_thumbnail(url=icon)
    embed.add_field(name = "Bot Command Prefix", value = "` ! `", inline=False)
    embed.add_field(name = "Music Plugin", value = "` play [song name | url] ` ` pause ` ` resume ` ` stop ` ` now |  current | playing ` ` queue ` ` shuffle ` ` skip ` ` remove  [song-index] ` ` loop ` ` volume [level] ` ` summon | summon   [channel] ` ` join ` ` leave | disconnect `", inline=False)

    embed.add_field(name = "Server Plugin", value = "` announce [message] ` ` avatar [member] ` ` info [member] ` ` inspire | quote ` ` joke ` ` botcheck `  ` ping | pong ` ` server `", inline=False)

    embed.add_field(name = "Crypto Plugin", value = "` axie status ` ` price [token-name] `", inline=False)

    embed.add_field(name = "Moderation Plugin", value = "` kick [member] ` ` ban [member] ` ` softban [member] ` ` unban [member] ` ` mute voice [member] ` ` mute chat [member] ` ` unmute [member] `", inline=False)
    await ctx.send(embed=embed)

  #MUSIC HELP
  @help.command(pass_context=True, aliases=['music'])
  async def _music(self, ctx):
    plugin = "Music"
    embed = discord.Embed(title="**{0} Plugins**".format(plugin), color=default)
    embed.add_field(
    name= " ` play [song name | url] `  ", value=" Magpatugtog ng isang kanta", inline=False)
    embed.add_field(name=" ` pause `  ", value=" I-pause ang kasalukuyang tumutugtog na kanta", inline=False)
    embed.add_field(name=" ` resume `  ", value=" Ipagpatuloy ang isang kasalukuyang naka-pause na kanta", inline=False)
    embed.add_field(name=" ` stop `  ", value=" Ihinto sa pagtugtog ang kanta at i-clear ang list ng kanta", inline=False)
    embed.add_field(name=" ` now | current | playing `  ", value="  Ipakita ang kasalukuyang tumutugtog na kanta", inline=False)
    embed.add_field(name=" `  queue `  ", value="  Ipinapakita ang nakalista na mga kanta", inline=False)
    embed.add_field(name=" ` shuffle `  ", value="  I-shuffle ang kanta", inline=False)
    embed.add_field(name=" ` skip `  ", value=" Bumoto upang laktawan ang isang kanta, kailangan ng 2 boto sa pag-skip\n\tAng requester ng kanta ay maaaring i-bypass ang pagboto", inline=False)
    embed.add_field(name=" ` remove [index] `  ", value=" Alisin ang isang kanta mula sa listahan batay sa ibinigay na index", inline=False)
    embed.add_field(name=" ` loop `  ", value=" I-loop ang kasalukuyang tumutugtog na kanta\n\tMuling i-loop ang kasalukuyang tumutugtog na kanta para ma un-loop", inline=False)
    embed.add_field(name=" ` volume [level] `  ", value=" Itakda ang lakas ng tunog", inline=False)
    embed.add_field(name=" ` summon | summon [channel] `  ", value="  I-summon ang bot sa voice channel", inline=False)
    embed.add_field(name=" ` join `  ", value=" Sumali sa voice channel", inline=False)
    embed.add_field(name=" ` leave | disconnect `  ", value="  Alisin ang mga kanta mula sa listahan at mag leave sa voice channel", inline=False)
    await ctx.send(embed=embed)

  #CRYPTO HELP
  @help.command(pass_context=True, aliases=['crypto'])
  async def _crypto(self, ctx):
    plugin = "Crypto"
    embed = discord.Embed(title="**{0} Plugins**".format(plugin), color=default)
    embed.add_field(name=" ` axie status `  ", value=" Ipinapakita ang estado (status) ng laro na axie infinity", inline=False)
    embed.add_field(name=" ` price [token] `  ", value=" Ipinapakita ang presyo ng isang token batay sa coingecko", inline=False)
    #embed.add_field(name=" `  bnbprice [token-name] `  ", value="  Ipinapakita ang presyo ng isang token batay sa binance", inline=False)
    #embed.add_field(name=" `  calc [token-name][PHP price] `  ", value=" Pagkalkula ng katumbas na presyo ng crypto token/coin sa peso naten", inline=False)
    await ctx.send(embed=embed)

  #SERVER HELP
  @help.command(pass_context=True, aliases=['server'])
  async def _server(self, ctx):
    plugin = "Server"
    name = str(ctx.guild.name)
    embed = discord.Embed(title="**{0} Plugins**".format(plugin), color=default)
    embed.add_field(name=" ` name [member] `  ", value=" Ipinapakita ang pasadyang mensahe para sa tukoy na miyembro ng " + name, inline=False)

    embed.add_field(name=" ` announce [message] `  ", value=" Ipinapakita ang buong mensahe ng membro sa announcement channel", inline=False)

    embed.add_field(name=" ` avatar [member] `  ", value=" Ipinapakita ang profile avatar ng mga membro", inline=False)
    embed.add_field(name=" ` info [member] `  ", value=" Ipinapakita ang buong profile ng mga membro", inline=False)

    embed.add_field(name=" ` inspire | quote `  ", value="  Ipinapakita ang random na mensahe ng mga quote", inline=False)  
    embed.add_field(name=" ` joke `  ", value=" Ipinapakita ang random na mensahe ng mga biro", inline=False)
    embed.add_field(name=" ` botcheck `  ", value=" Ipinapakita kung ang bot ay online", inline=False)
    embed.add_field(name=" ` ping | pong `  ", value=" Ipinapakita ang bot ping", inline=False)

    embed.add_field(name=" ` server `  ", value=" Ipinapakita ang buong detalye ng server", inline=False)
    
    await ctx.send(embed=embed)

  #SERVER HELP
  @help.command(pass_context=True, aliases=['moderation', 'moderator', 'mod'])
  async def _moderation(self, ctx):
    plugin = "Moderation"
    embed = discord.Embed(title="**{0} Plugins**".format(plugin), color=default)
    embed.add_field(name=" ` kick [member] `  ", value=" Pag-sipa sa server ng isang miyembro", inline=False)
    embed.add_field(name=" ` ban [member] `  ", value=" Pag-ban sa server ng isang miyembro", inline=False)
    embed.add_field(name=" ` softban [member] `  ", value=" Pag-ban at pag-unban sa server ng isang miyembro", inline=False)
    embed.add_field(name=" ` unban [member] `  ", value=" Pag-unban sa server ng isang miyembro", inline=False)

    embed.add_field(name=" ` mute voice [member] `  ", value=" Pag-mute sa voice channel ng isang miyembro", inline=False)
    embed.add_field(name=" ` mute chat [member] `  ", value=" Pag-mute sa text channel ng isang miyembro", inline=False)
    embed.add_field(name=" ` unmute [member] `  ", value=" Pag-unmute sa voice channel at text channel ng isang miyembro", inline=False)
    
    await ctx.send(embed=embed)
 

def setup(bot):
  bot.add_cog(Helps(bot))