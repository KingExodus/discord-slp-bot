import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = "!", description ="Online ako kili-kili!", intents = intents)
bot.remove_command('help')

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


bot.run(os.getenv(DISCORD_TOKEN), bot=True, reconnect=True)