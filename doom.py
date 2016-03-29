import datetime
import random
import time

DAYS = dict(zip(('sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'), range(7)))
REVERSE_DAYS = {v: k for k, v in DAYS.items()}

JAN_ONE = datetime.date.today().replace(day=1, month=1).toordinal()


def get_guess():
  while True:
    try:
      guess = raw_input('weekday?:\n')
      return DAYS[guess.lower()[:3]]
    except KeyError:
      pass


def main():
  try:
    orig_time = time.time()
    while True:
      random_offset = random.randrange(0, 366)
      rand_day = datetime.datetime.fromordinal(JAN_ONE + random_offset).date()
      print rand_day
      weekday = rand_day.isoweekday()
      guess = get_guess()
      if weekday % 7 == guess % 7:
        break
      print 'No. Was {}'.format(REVERSE_DAYS[weekday % 7])
    print time.time() - orig_time
  except (EOFError, KeyboardInterrupt):
    pass

if __name__ == "__main__":
  main()
