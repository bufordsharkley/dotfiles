import datetime
import random
import time

DAYS = dict(zip(('sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'), range(7)))
REVERSE_DAYS = {v: k for k, v in DAYS.items()}

JAN_ONE = datetime.date(1900, 1, 1).toordinal()
TODAY = datetime.date.today()


def get_guess():
  while True:
    try:
      guess = raw_input('weekday?:\n')
      return DAYS[guess.lower()[:3]]
    except KeyError:
      pass


def quiz_until_correct():
  while True:
    random_offset = random.randrange(0, 366 * 140)
    rand_day = datetime.datetime.fromordinal(JAN_ONE + random_offset).date()
    if rand_day > TODAY:
      continue
    print rand_day
    weekday = rand_day.isoweekday()
    guess = get_guess()
    if weekday % 7 == guess % 7:
      return
    print 'No. Was {}'.format(REVERSE_DAYS[weekday % 7])


def main():
  try:
    orig_time = time.time()
    quiz_until_correct()
  except (EOFError, KeyboardInterrupt):
    pass
  print time.time() - orig_time

if __name__ == "__main__":
  main()
