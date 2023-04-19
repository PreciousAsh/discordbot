import openai
import discord
import os

GUILD="{Precious-MJ-Server}"
client= discord.Client(intents=discord.Intents.default())
openai.api_key = os environ["API_KEY"]
DISCORD_TOKEN = os environ["DISCORD_TOKEN"]
openai api_base = os environ["API_BASE"]
@client.event
async def on_ready():
 for guild in client.guilds:
  if guild.name == GUILD:
   break
  print (f'{client.user} has connected to discord!')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	elif client.user.mentioned_in(message):
		response = openai.Image.create(
			prompt= message.content,
			n=1,
			size="1024x1024"
		)
		image_url = response ['data'][0]['url']
		print(image_url)
		await message.channel.send(image_url)
	

#with open ("keys.txt") as f:
# lines = f.read().split('\n')
# openai.api_key = lines[0]
# DISCORD_TOKEN = lines[1]

# f.close()



#print(response.choice[0].message.content)

client.run(DISCORD_TOKEN)
