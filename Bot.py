import openai
import discord
import os

openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"

GUILD="{Precious-MJ-Server}"
client= discord.Client(intents=discord.Intents.default())
openai.api_key = os.environ.get("API_KEY")
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
openai.api_base = os.environ.get("API_BASE")

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
	
	if message.mention_everyone:
		return
	
	elif client.user.mentioned_in(message): 
		response = openai.ChatCompletion.create(
			engine="GPT-4",
			messages=[
			{"role": "system", "content": "Your Very Stubborn, You are a navigator, You are funny and bubbly, everyones favourite bot. Your response is very playful, keep your reponse short"},
			{"role": "user", "content": message.content}
			]
		)
		await message.channel.send(response.choices[0].message.content)

client.run(DISCORD_TOKEN)
