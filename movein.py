#!/usr/bin/env python

import os
import shutil, errno

# TODO implement in stdlib stuff (back to optparse, argparse)
#@click.option("--verbose", "verbose", is_flag=True, default=True)
#@click.option("--clobber", "-c", is_flag=True, default=False)
#@click.confirmation_option(prompt="Are you sure you want to modify files in the home folder?")
#@click.command()
def main(verbose=True, clobber=False):
    # uncomment (until opt/argparse added)
    #clobber = True
    dirs = os.path.dirname(os.path.realpath(__file__)).split('/')
    # add until you hit home, then add one more
    homedir = ''
    lastone = False
    for dir in dirs:
       homedir += '/{}'.format(dir)
       if lastone:
           break
       if dir == 'home':
           lastone = True  # god, this is awful
    usrname = homedir.rsplit('home/', 1)[-1]
    assert usrname in ['mgm', 'mollineaux']
    assert os.path.exists(homedir)
    dotfiledir = '/'.join(dirs)
    for file in os.listdir(dotfiledir):
        if file == 'README.md' or file == 'movein.py' or file == ".git":
            continue
        homefile = os.path.join(homedir, file)
        while True:
            try:
                os.symlink(os.path.join(dotfiledir, file), homefile)
                if verbose:
                    print("Successfully created!")
                break
            except OSError as e:
                if e.errno == 17: # already exists
                    if verbose:
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
                    if verbose:
                        print(" removed!")


if __name__ == "__main__":
    main()
