import openai

with open("keys.txt") as f:
	lines = f.read().split('\n')
	openai.api_key = lines[0]
	DISCORD_TOKEN = lines[0]

f.close()

response = openai.Image.create(
	prompt="A beautiful african woman",
	n=1,
	size="1024x1024"
)
image_url = response ['data'][0]['url']
print(image_url)
