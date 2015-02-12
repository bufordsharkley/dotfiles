#!/usr/bin/env python

import os
import shutil, errno

HOMEDIR = '/home/mgm'

def main():
    assert os.path.exists(HOMEDIR)
    dotfiledir = os.path.dirname(os.path.realpath(__file__))
    print dotfiledir
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            raise


if __name__ == "__main__":
    main()
