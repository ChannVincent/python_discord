import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('#cmd'):
        print(f'cmd')
        await message.channel.send('cmd!')

    if message.content.startswith('#start'):
        print(f'start')
        await message.channel.send('start!')

    if message.content.startswith('#end'):
        print(f'end')
        await message.channel.send('end!')

client.run(os.getenv('TOKEN'))