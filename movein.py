import argparse
import errno
import os
import shutil
import sys


def main(clobber=False):
    dirs = os.path.dirname(os.path.realpath(__file__)).split('/')
    # add until you hit home, then add one more
    homedir = os.path.expanduser('~')
    usrname = homedir.rsplit('/', 1)[1]
    try:
        assert usrname in ['mgm', 'mollineaux']
    except AssertionError:
        raise Exception(usrname)
    assert os.path.exists(homedir)
    dotfiledir = '/'.join(dirs)
    for file in os.listdir(dotfiledir):
        if file == 'README.md' or file == 'movein.py' or file == ".git":
            continue
        homefile = os.path.join(homedir, file)
        while True:
            try:
                os.symlink(os.path.join(dotfiledir, file), homefile)
                print("Successfully created!")
                break
            except OSError as e:
                if e.errno == 17:  # already exists
                    print("{} already exists...".format(file))
                    if not clobber:
                        print(" not changing it")
                        break
                    if os.path.islink(homefile):
                        os.remove(homefile)
                    elif os.path.isdir(homefile):
                        shutil.rmtree(homefile)
                    else:
                        os.remove(homefile)
                    print(" removed!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Move the dotfiles into ~')
    parser.add_argument('--clobber', '-c', dest='clobber', action='store_true',
                        help='overwrite current files in home directory')
    args = parser.parse_args()
    main(args.clobber)
