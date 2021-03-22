from replit import db
from reminder import Reminder

def add_reminder(message, reminder_date, db_dict='reminders'):
  reminders_lst = db[db_dict]
  new_reminder = Reminder.create_reminder(message, reminder_date)
  if not new_reminder:
    return False
  reminders_lst.append(new_reminder)
  db[db_dict] = reminders_lst.sort(key=lambda r: r.month + r.day + r.year)
  return new_reminder

def remove_reminder(id):
  for key in db.keys():
    db_dict = db[key]
    for reminder in db[key]:
      if reminder.id == id:
        db_dict.remove(reminder)
        db[key] = db_dict
        return True
  return False
  
def list_weekly_reminders():
  pass

def list_reminders(x):
  pass

def list_all_reminders():
  pass