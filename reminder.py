import hashlib

"""
Formats a date in the form: mm-dd-yyyy
Returns the a dictionary with the proper mappings if successful
Returns False if not
"""
def format_date(reminder_date):
  date_lst = reminder_date.replace(" ", "0").split('-')
  if len(date_lst) != 3:
    return False
  if not all([len(date_lst[0]) == 2, len(date_lst[1]) == 2, len(date_lst[2]) == 4]):
    return False
  for elem in date_lst:
    try:
      int(elem)
    except:
      return False
  date_dict = {
    'month' : date_lst[0],
    'day' : date_lst[1],
    'year' : date_lst[2]
  }
  return date_dict

"""
Reminder objects have five attributes
message: reminder message
month: month that reminder is scheduled for
day: day that reminder is scheduled for
year: year that reminder is scheduled for
sha_hash: unique id generated from message, month, day, and year
"""
class Reminder:
  def __init__ (self, message, mm, dd, yyyy):
    self.message = message
    self.month = mm
    self.day = dd
    self.year = yyyy
    m = hashlib.sha256()
    m.update(bytes(message+mm+dd+yyyy, 'utf-8'))
    self.sha_hash = str(m.digest())

  """
  Creates a reminder object with a given message and date
  If failed to create, returns False
  """
  @staticmethod
  def create_reminder(message, reminder_date):
    formatted_date = format_date(reminder_date)
    if not formatted_date:
      return False
    return Reminder(message, formatted_date['month'], formatted_date['day'], formatted_date['year'])
    
"""
#Test cases for format_date
test_dates = ['', '09-22-2019', '9-22-2019', '10']
assert format_date(test_dates[0]) == False
assert format_date(test_dates[1]) != False
assert format_date(test_dates[2]) == False
assert format_date(test_dates[3]) == False
print('All tests passed!')
"""