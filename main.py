import discord
import os

from reminder_utilities import add_reminder, initialize_db, list_all_reminders

client = discord.Client()

ADD_REMINDER_COMMAND = '//add reminder'
LIST_ALL_COMMAND = '//list all'
@client.event
async def on_ready():
  initialize_db()
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
  if message.author == client.user:
    return
  if not message.content.startswith('//'):
    return

  message_contents = message.content.split()
  if len(message_contents) >= 2 and message_contents[0] + " " + message_contents[1].lower() == ADD_REMINDER_COMMAND:
    message_message = " ".join(message_contents[2:len(message_contents)-1])
    message_date = message_contents[len(message_contents)-1]
    added_reminder = add_reminder(message_message, message_date)
    if added_reminder:
      message_to_send = "Successfully added reminder:\nMESSAGE: {message}\nDATE: {reminder_date}".format(message=added_reminder.message, reminder_date=added_reminder.month + '-' + added_reminder.day + '-' + added_reminder.year)
    else:
      message_to_send = 'Failed to add reminder!\nCommon mistakes include: not formatting date to be mm-dd-yyyy'
    await message.channel.send(message_to_send)
  if len(message_contents) == 2 and message_contents[0] + " " + message_contents[1] == LIST_ALL_COMMAND:
    message_to_send = list_all_reminders()
    await message.channel.send(message_to_send)
  

client.run(os.getenv('TOKEN'))