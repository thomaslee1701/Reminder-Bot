"""
Formats a date in the form: mm-dd-yyyy
Returns the a dictionary with the proper mappings if successful
Returns False if not
"""
def format_date(reminder_date):
  date_lst = reminder_date.split('-')
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

class reminder:
  def __init__ (self, message, mm, dd, yyyy):
    self.message = message
    self.month = mm
    self.day = dd
    self.year = yyyy
  @staticmethod
  def create_reminder(reminder_date):
    formatted_date = format_date(reminder_date)
    if not formatted_date:
      return False
    return reminder(formatted_date['month'], formatted_date['day'], formatted_date['year'])
    
"""
#Test cases for format_date
test_dates = ['', '09-22-2019', '9-22-2019', '10']
assert format_date(test_dates[0]) == False
assert format_date(test_dates[1]) != False
assert format_date(test_dates[2]) == False
assert format_date(test_dates[3]) == False
print('All tests passed!')
"""