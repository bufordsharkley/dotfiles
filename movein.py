#!/usr/bin/env python

import os
import shutil, errno

def main():
    dotfiledir = os.path.dirname(os.path.realpath(__file__))
    homedir = '/'.join(dotfiledir.split('/')[:3])
    assert homedir.rsplit('/', 1)[-1] == 'mgm'
    assert os.path.exists(homedir)
    for file in os.listdir(dotfiledir):
        if file == 'README.md' or file == 'movein.py' or file == '.git':
            continue
        os.symlink(os.path.join(dotfiledir, file), os.path.join(homedir, file))
        print 'creating symlink for {}'.format(file)


if __name__ == "__main__":
    main()
