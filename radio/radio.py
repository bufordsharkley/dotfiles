import os
import sys
import stat


STATIONS = {'wfmu': 'http://wfmu.org/wfmu.pls',
            'kzsu': 'http://kzsu-streams.stanford.edu/kzsu-1-hi.mp3',
            'kspc': 'http://stream.kspc.org:8080/stream192',
            'kqed': 'http://streams.kqed.org/',
            'kfjc': 'http://aac.kfjc.org/high.m3u',
            #'kqed': 'http://streams.kqed.org/kqedradio.m3u',
           }
#gnome-terminal --command="mplayer -slave -idle -input file=/tmp/radiofifo"

FIFO_FILE = '/tmp/radiofifo'


def _is_a_fifo(path):
  return stat.S_ISFIFO(os.stat(path).st_mode)


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
  if not _is_a_fifo(FIFO_FILE):
    raise RuntimeError(FIFO_FILE)
  try:
    with open(FIFO_FILE, 'w') as f:
      f.write(command + '\n')
  except KeyError:
    print 'No station with that name'


def main():
  sys.argv.pop(0)
  if not sys.argv:
    raise Exception('nlsdfsdf')
  change_channel(sys.argv)


if __name__ == "__main__":
  main()
