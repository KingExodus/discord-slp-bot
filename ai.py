import discord
from discord.ext import commands

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.cleverbot.com')
driver.find_element_by_id('noteb').click()

def get_response(message):
  driver.find_element_by_xpath('//*[@id="avatarform"]/input[1]').send_keys(message + Keys.RETURN)
  while True:
    try:
      driver.find_element_by_xpath('//*[@id="snipTextIcon"]')
      break
    except:
      continue

  response = driver.find_element_by_xpath('//*[@id="line1"]/span[1]').text
  return response
  
class AI(commands.Cog):
  def __init__(self, client):
    self.client = client
 
  @commands.Cog.listener()
  async def on_ready(self):
    print("importing ai bot - Done!")

  async def on_message(self, message):
    if message.author != self.user:
      response = get_response(message.content)
      await message.channel.send(f"{message.author.mention} {response}")

def setup(bot):
  bot.add_cog(AI(bot))

