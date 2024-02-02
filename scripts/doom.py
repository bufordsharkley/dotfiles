import datetime
import os
import random
import time

import click


DAYS = dict(zip(('sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'), range(7)))
# special shorthand because my h is broken
DAYS['r'] = 4
#REVERSE_DAYS = {v: k for k, v in reversed(DAYS.items())}
REVERSE_DAYS = {v: k for k, v in DAYS.items()}


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    if ctx.invoked_subcommand is None:
        main_quiz()


def main_quiz():
    elapsed = quiz_until_correct()
    with open(os.path.expanduser('~/.doomtimertracker.txt'), 'a') as f:
        f.write(f"{elapsed:.5}\n")


def get_guess():
    while True:
        try:
            guess = click.prompt('weekday?')
            if guess == 'emergency':
                return 'emergency'
            return DAYS[guess.lower()[:3]]
        except:  # Crude, dangerous method to avoid ctrl-c
            pass


def random_date_format(date):
    formats = ('%B %d, %Y', '%Y-%m-%d', '%B %-d, %Y')
    choice = random.sample(formats, 1)[0]
    return date.strftime(choice)


def random_date():
    this_year = datetime.date.today().year
    couple_from_now = this_year + 4
    # Baseline:
    years = [x for x in range(1860, 2032)]
    # 1920s-on, weigh far more:
    years += [x for x in range(1920, couple_from_now)] * 5
    # atomic age:
    years += [x for x in range(1948, couple_from_now)] * 5
    # "recent"
    years += [x for x in range(1972, couple_from_now)] * 5
    # "memory"
    years += [x for x in range(1992, couple_from_now)] * 5
    years += [x for x in range(this_year - 2, this_year + 2)] * 100
    years += [this_year] * 300
    random_year = random.choice(years)
    jan1 = datetime.date(random_year, 1, 1).toordinal()
    dec31 = datetime.date(random_year, 12, 31).toordinal()
    return datetime.date.fromordinal(random.randint(jan1, dec31))


def quiz_until_correct():
    errors = 0
    while True:
        orig_time = time.time()
        rand_day = random_date()
        print(random_date_format(rand_day))
        weekday = rand_day.isoweekday()
        guess = get_guess()
        if guess == 'emergency':
            return 9999
        if weekday % 7 == guess % 7:
            return display_score(orig_time, errors)
        print('No. Was {}'.format(REVERSE_DAYS[weekday % 7]))
        errors += 1


def display_score(orig_time, errors):
    elapsed = time.time() - orig_time
    print(f"{elapsed:.5}")
    if errors:
        print('with error count: {}'.format(errors))
    return elapsed


@main.command('prez')
def prez_mode():
    # Using numbers allowed here (though it doesn't matter)
    for ii in range(7):
        DAYS[str(ii)] = ii
    this_year = datetime.date.today().year
    couple_from_now = this_year + 4
    # Baseline:
    prez_years = [x for x in range(1860, 2032, 4)]
    # 1920s-on, weigh far more:
    prez_years += [x for x in range(1920, couple_from_now, 4)] * 5
    # atomic age:
    prez_years += [x for x in range(1948, couple_from_now, 4)] * 5
    # "recent"
    prez_years += [x for x in range(1972, couple_from_now, 4)] * 5
    # "memory"
    prez_years += [x for x in range(1992, couple_from_now, 4)] * 5
    while True:
        choice = random.choice(prez_years)
        print(choice)
        answer = datetime.datetime(choice, 10, 31).isoweekday()
        guess = input('weekday?:\n')
        print(answer % 7)


if __name__ == "__main__":
  main()
