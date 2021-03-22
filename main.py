import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as Reminder Bot')

"""
Messages have a couple of attributes:
author: author of the message
content: message content'
channel: the channel that the message was sent in. channel.send
sends a message to that channel
"""
@client.event
async def on_message(message):
  if message.user == client.user:
    return
  pass



client.run(os.getenv('TOKEN'))