import datetime
import random
import time


def get_guess():
  while True:
    try:
      guess = raw_input('doomsday?:\n')
      return int(guess)
    except ValueError:
      pass


def random_year():
  return random.randrange(1900, 2050)


def quiz_until_correct():
  errors = 0
  while True:
    orig_time = time.time()
    rand_year = random_year()
    print rand_year
    weekday = datetime.date(rand_year, 10, 31).isoweekday()
    guess = get_guess()
    if weekday % 7 == guess % 7:
      display_score(orig_time, errors)
      return
    print 'No. Was {}'.format(weekday % 7)
    errors += 1


def display_score(orig_time, errors):
  print time.time() - orig_time
  if errors:
    print 'with error count: {}'.format(errors)


def main():
  try:
    quiz_until_correct()
  except (EOFError, KeyboardInterrupt):
    pass

if __name__ == "__main__":
  main()
