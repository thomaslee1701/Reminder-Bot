import discord
import os
from reminder_utilities import add_reminder

client = discord.Client()

ADD_REMINDER_COMMAND = '//add reminder'

@client.event
async def on_ready():
  print('Logged in as Reminder Bot')

"""
Messages have a couple of attributes:
author: author of the message
content: message content
channel: the channel that the message was sent in. channel.send
sends a message to that channel
"""
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if not message.content.startswith('//'):
    return
  message_contents = message.content
  if message.content.startswith(ADD_REMINDER_COMMAND):
    #crops off the command part of the command
    message_contents = message_contents[len(ADD_REMINDER_COMMAND):]
    #selects just the message and date
    message_message = message_contents[:len(message_contents)-10][1:]
    message_date = message_contents[len(message_contents)-10:]

    

    if len(message_contents) != 4:
      await message.channel.send('Incorrect operands! //add reminder **message date**')
    else:
      added_reminder = add_reminder(message_contents[2], message_contents[3])
      if added_reminder:
        message_to_send = "Successfully added reminder...\n{message}\n{reminder_date}".format(message=added_reminder.date, reminder_date=added_reminder.month + '-' + added_reminder.day + '-' + added_reminder.year)
      else:
        message_to_send = 'Failed to add reminder!\nCommon mistakes include: not formatting date to be mm-dd-yyyy'
      await message.channel.send(message_to_send)
  

client.run(os.getenv('TOKEN'))