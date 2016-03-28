import datetime
from datetime import date
import random

JAN_ONE = datetime.date.today().replace(day=1, month=1).toordinal()
while True:
  random_offset = random.randrange(0, 366)
  rand_day = datetime.datetime.fromordinal(JAN_ONE + random_offset).date()
  print rand_day
  weekday = rand_day.isoweekday()
  guess = raw_input('weekday?:\n')
  if weekday % 7 == int(guess):
    break
  print 'no {}'.format(weekday)
