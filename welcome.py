import discord
from discord.ext import commands
import requests
import datetime
from PIL import Image, ImageFont, ImageDraw

default = discord.Color.blue()

class Welcome(commands.Cog):
  def __init__(self, client):
    self.client = client
 
  @commands.Cog.listener()
  async def on_ready(self):
    print("importing welcome commands - Done!")

  @commands.Cog.listener()
  async def on_member_join(self, member):
    #guild_server = self.client.get_guild(757440289932705842)
    #welcome_channel = guild_server.get_channel(892900914682265600)
    #rules_channel = guild_server.get_channel(892901239451443210)

    server_name = member.guild.name
    welcome_channel = member.guild.get_channel(892900914682265600)#881944086569967696
    rules_channel = member.guild.get_channel(902096229805199370)#881937933165281342
    
    embed = discord.Embed(title=f"🚀✨ ** WELCOME TO {server_name.upper()}** ✨🚀", description=f"Hi {member.mention}, you're the member #{len(list(member.guild.members))}!", color = default)
    embed.add_field(name = "\u200b", value = f"Please proceed to <#902096229805199370> channel to see {str(server_name)} server rules.", inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")    
    embed.timestamp = datetime.datetime.utcnow()
    #embed.set_footer(text = f'{str(member)} just joined the server.')
    await welcome_channel.send(embed=embed)
    """
    # Images
    track_background_image = Image.open('welcome_template_3.png').convert('RGBA')
    album_image = Image.open(requests.get(member.avatar_url, stream=True).raw).convert('RGBA')

    # Fonts
    title_font = ImageFont.truetype('theboldfont.ttf', 42)
    name_font = ImageFont.truetype('theboldfont.ttf', 36)
    count_font = ImageFont.truetype('theboldfont.ttf', 32)
    #start_duration_font = ImageFont.truetype('theboldfont.ttf', 12)
    #end_duration_font = ImageFont.truetype('theboldfont.ttf', 12)

    # Positions
    title_text_position = 150, 420
    name_text_position = 180, 470
    album_text_position = 150, 520
    #start_duration_text_position = 150, 122
    #end_duration_text_position = 515, 122

    # Draws
    draw_on_image = ImageDraw.Draw(track_background_image)
    draw_on_image.text(title_text_position, f'🚀✨  WELCOME TO {(server_name).upper()}  ✨🚀', 'white', font=title_font)

    draw_on_image.text(name_text_position, f'{member.name}', 'white', font=name_font)

    draw_on_image.text(album_text_position, f'Member #{len(list(member.guild.members))}', 'white', font=count_font)

    #draw_on_image.text(start_duration_text_position, '0:00', 'white', font=start_duration_font)
    #draw_on_image.text(end_duration_text_position,
    #  f"{dateutil.parser.parse(str(spotify_result.duration)).strftime('%M:%S')}",
    #  'white', font=end_duration_font)

    # Background colour

    album_color = album_image.getpixel((250, 100))
    background_image_color = Image.new('RGBA', track_background_image.size, album_color)
    x, y = track_background_image.size
    background_image_color.paste(track_background_image, (0, 0), track_background_image)
    

    # Resize
    album_image_resize = album_image.resize((352, 352))
    
    background_image_color.paste(album_image_resize, (225, 30), album_image_resize)
    background_image_color.paste(track_background_image, (0, 0), track_background_image)

    # Save image
    background_image_color.save('welcomer.png', 'PNG')

    await welcome_channel.send(file=discord.File('welcomer.png'))
    """

    #setting embed
    #em = discord.Embed(color=0x12d600, description=f"Thank you {member.mention}, you're the member number {len(list(member.guild.members))}!")
    #em.set_image(url=f"{member.avatar_url}")
    #em.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")    
    #em.timestamp = datetime.datetime.utcnow()
    
    #await welcome_channel.send(embed=em)



  @commands.Cog.listener()
  async def on_member_remove(self, member):
    #pass
    welcome_channel = member.guild.get_channel(881944086569967696)#892900914682265600)
    await welcome_channel.send(f"😥 {member.name} has left. Bye")

  @commands.Cog.listener()
  async def on_member_leave(self, member):
    pass


intents = discord.Intents.default()
intents.members = True

def setup(bot):
  bot.add_cog(Welcome(bot))