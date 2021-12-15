import discord
from discord.ext import commands
import time
import datetime
import typing

default = discord.Color.blue()

class HeistBot(commands.Cog):
  def __init__(self, client):
    self.client = client
 
  @commands.Cog.listener()
  async def on_ready(self):
    print("importing bot commands - Done!")

  

  @commands.command(pass_context=True, aliases=['botcheck'])
  async def _botcheck(self, ctx):
    embed = discord.Embed(description="Kamusta, nandito lang ako naghihintay ng iyong mga utos!", color=default)
    await ctx.send(embed=embed)

  @commands.command(pass_context=True, aliases=['botinfo'])
  async def _botinfo(self, ctx):
    """Display information about the bot"""
    app = await self.client.application_info()
    botMember = self.client.user

    embed = discord.Embed(description = app.description, color = default)
    embed.set_author(name = "{0} Information".format(app.name), icon_url = botMember.avatar_url)
    embed.add_field(name = "Username", value = botMember, inline = True)
    embed.add_field(name = "Status", value = "Online", inline = True)
    embed.add_field(name = "Activity", value = self.client.activity, inline = True )

    created = self.client.user.created_at
    embed.add_field(name = "BOT Created", value = created.strftime("%d.%m.%Y at %H:%M %p"),inline = True)

    #embed.add_field(name = "Servers", value = len(self.client.guilds))
    embed.add_field(name = "Total Users", value = len(self.client.users))
    await ctx.send(embed = embed)

  @commands.command(pass_context=True, aliases=['server'])
  async def _server(self, ctx):
    #servername = str(ctx.guild.name)
    #description = str(ctx.guild.description)
    donj = 754381164504154203

    icon = str(ctx.guild.icon_url)
    region = str(ctx.guild.region)
    timestamp = ctx.guild.created_at
    date_time = timestamp.strftime("%m/%d/%Y, %H:%M %p")

    embed = discord.Embed(title= "** Server Information **", description="", color=discord.Color.blue())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner ", value=f"{ctx.guild.owner} ", inline=False)
    embed.add_field(name=":regional_indicator_a:  Server ID ", value=f"{ctx.guild.id}", inline=False)
    embed.add_field(name=":birthday:  Created at ", value="{0}".format(date_time), inline=False)
    embed.add_field(name=":earth_americas:  Server Region ", value="{0}".format(region.upper()), inline=True)
    embed.add_field(name=":busts_in_silhouette:  Members", value=f"{ctx.guild.member_count} members", inline=True)
    await ctx.send(embed=embed)
  
  @commands.command(pass_context=True, aliases=['clear'])
  @commands.guild_only()
  async def _clear(self, ctx, amount: str = None):
    if amount == 'all':
      embed = discord.Embed(description ="Cleared all messages")
      msg = await ctx.send(embed = embed)
      await msg.add_reaction('🆗')

      await ctx.channel.purge()

    else:

      if not amount:        
        embed = discord.Embed(description ="Cleared {0} message".format(amount))
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('🆗')

        await ctx.channel.purge(limit=1)

      else:
        embed = discord.Embed(description ="Cleared {0} messages".format(amount))
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('🆗')

        await ctx.channel.purge(limit=(int(amount) + 1))

  @commands.command(pass_context=True, aliases=['ping', 'pong'])
  async def _ping(self, ctx):
    before = time.monotonic()
    before_ws = int(round(self.client.latency * 1000, 1))
    message = await ctx.send("Loading...")
    ping = int((time.monotonic() - before) * 1000)
    await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {ping}ms")

  @commands.command("invite")
  #@commands.bot_has_permissions(create_instant_invite = True)
  #@commands.has_permissions(create_instant_invite = True)
  async def invite(self, ctx):
    """Generate an invite to this server"""
    invites = await ctx.guild.invites()
    channel = ctx.channel

    botInvites = list(x for x in invites if x.inviter.id == self.client.user.id and x.channel.id == channel.id)

    invite = None
    if (len(botInvites) == 0): # Create new invite in this channel
      await ctx.send("Creating a new invite link.")
      invite = await channel.create_invite(reason = "Bot created invite using !invite")
    else:
      await ctx.send("Previous invite link found, retrieving that one.")
      invite = botInvites[0]

    await ctx.send(invite)


  @commands.command("reload")
  @commands.is_owner()
  async def reload(self, ctx, *, extension: typing.Optional[str] = None):
    """Reload an extension or all extensions"""
    if (extension is None): # Reload all extensions
      for ext in self.config["extensions"]:
        self.client.reload_extension(ext)
      await ctx.send("All extensions reloaded.")
    else: # Reload single extension
      extension = str.lower(extension)
      self.client.reload_extension(extension)
      await ctx.send("{0} extension reloaded.".format(extension))

  @commands.command("load")
  @commands.is_owner()
  async def load(self, ctx, *, extension: str):
    """Load a new extension"""
    extension = str.lower(extension)
    self.client.load_extension(extension)
    await ctx.send("{0} extension loaded.".format(extension))

  
def setup(bot):
  bot.add_cog(HeistBot(bot))