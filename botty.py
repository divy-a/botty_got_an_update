import discord
import os
from dotenv import load_dotenv
import requests
import uuid
load_dotenv()





intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('LOGGED IN :  {0.user}'.format(client))


@client.event
async def on_message(message):
    if instance_id != str(requests.get(f'''{os.getenv('URL')}/get_instance_id''').text):
        return
    
    if message.author == client.user:
        return

    try:
        response = requests.get(f'''{os.getenv('URL')}/controller?q={message.content}''')
        await message.channel.send(response.text)
    except Exception as ex:
        await message.channel.send('Something went wrong.')


if __name__ == '__main__':
    instance_id = str(uuid.uuid4().hex)
    response = requests.get(f'''{os.getenv('URL')}/update_instance_id?id={instance_id}''')
    client.run(os.getenv('TOKEN'))
