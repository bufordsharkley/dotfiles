from __future__ import print_function

import os
import stat
import subprocess
import sys


STATIONS = {'wfmu': 'http://wfmu.org/wfmu.pls',
            'kzsu': 'http://kzsu-streams.stanford.edu/kzsu-1-hi.mp3',
            'kspc': 'http://stream.kspc.org:8080/stream192',
            'kqed': 'http://streams.kqed.org/',
            'kfjc': 'http://aac.kfjc.org/high.m3u',
            #'kqed': 'http://streams.kqed.org/kqedradio.m3u',
           }

FIFO_FILE = '/tmp/radiofifo'


def _check_status_of_fifo(path):
    if not os.path.exists(path):
        resp = raw_input('{} does not exist. Create?\n'.format(path))
        if resp.strip().lower() == 'y':
            os.mkfifo(path)
        sys.exit(1)
    if not stat.S_ISFIFO(os.stat(path).st_mode):
        raise RuntimeError('{} is not a FIFO'.format(path))
    try:
        devnull = open(os.devnull, 'w')
        subprocess.check_call(['lsof', path], stdout=devnull, stderr=devnull)
    except subprocess.CalledProcessError:
        command = ('gnome-terminal --command="mplayer '
                   '-slave -idle -input file={}"').format(path)
        subprocess.check_call(command, shell=True)


def resolve_station_to_command(station):
    stream = STATIONS[station.lower()]
    return 'loadfile {}\n'.format(stream)

def resolve_other_command(args):
    if args[0] == 'mute':
        return 'volume 0 1'
    elif args[0] == 'unmute':
        return 'volume 100 1'
    else:
        raise NotImplementedError

def change_channel(args):
    try:
        command = resolve_station_to_command(args[0])
    except KeyError:
        command = resolve_other_command(args)

    _check_status_of_fifo(FIFO_FILE)

    try:
        with open(FIFO_FILE, 'w') as f:
            f.write(command + '\n')
    except KeyError:
        print('No station with that name', file=sys.stderr)


def main():
    sys.argv.pop(0)
    if not sys.argv:
        print('Usage: radio [CALL LETTERS]', file=sys.stderr)
        sys.exit(1)
    change_channel(sys.argv)


if __name__ == "__main__":
  main()
