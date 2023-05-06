import discord
import os
from dotenv import load_dotenv
import requests
load_dotenv()

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('LOGGED IN :  {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        response = requests.get(f'''{os.getenv('URL')}/controller?q={message.content}''')
        await message.channel.send(response.text)
    except Exception as ex:
        await message.channel.send('Something went wrong.')


if __name__ == '__main__':
    client.run(os.getenv('TOKEN'))
