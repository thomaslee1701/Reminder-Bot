from replit import db
from reminder import Reminder

"""
Adds a reminder with inputted message and date into the
specified database
"""
def add_reminder(message, reminder_date, db_dict='reminders'):
  reminders_lst = db[db_dict]
  new_reminder = Reminder.create_reminder(message, reminder_date)
  if not new_reminder:
    return False
  reminders_lst.append(new_reminder)
  reminders_lst.sort(key=lambda r: r.month + r.day + r.year)
  db[db_dict] = reminders_lst
  return new_reminder

"""
Removes the reminder with the specified id from database
"""
def remove_reminder(id):
  for key in db.keys():
    db_dict = db[key]
    for reminder in db[key]:
      if reminder.id == id:
        db_dict.remove(reminder)
        db[key] = db_dict
        return reminder
  return False
  
def list_weekly_reminders():
  pass

def list_reminders(x):
  pass

"""
Returns a string with all the reminders listed in order of ascending date
"""
def list_all_reminders():
  ret_str = ""
  for key in db.keys():
    for reminder in db[key]:
      ret_str += "Reminder: {message}\n" \
                 "Date: {reminder_date}\n"\
                 "SHA_HASH: {sha_hash}\n"\
                 .format(message=reminder.message, reminder_date=reminder.month + '-' + reminder.day + '-' + reminder.year, sha_hash=reminder.sha_hash)
      ret_str += '------------------------------\n'
  return ret_str

"""
initializes the lists in db if they do not already exist
"""
def initialize_db():
  if 'reminders' not in db.keys() or type(db['reminders']) != list:
    db['reminders'] = []
  if 'weekly_reminders' not in db.keys() or type(db['weekly_reminders']) != list:
    db['weekly_reminders'] = []
  