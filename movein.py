#!/usr/bin/env python

import os
import shutil, errno

import click

@click.option("--verbose", "verbose", is_flag=True, default=True)
@click.option("--clobber", "-c", is_flag=True, default=False)
@click.confirmation_option(prompt="Are you sure you want to modify files in the home folder?")
@click.command()
def main(verbose, clobber):
    dotfiledir = os.path.dirname(os.path.realpath(__file__))
    homedir = '/'.join(dotfiledir.split('/')[:3])
    assert homedir.rsplit('/', 1)[-1] in ['mgm', 'mollineaux']
    assert os.path.exists(homedir)
    for file in os.listdir(dotfiledir):
        if file == 'README.md' or file == 'movein.py' or file == ".git":
            continue
        homefile = os.path.join(homedir, file)
        while True:
            try:
                os.symlink(os.path.join(dotfiledir, file), homefile)
                if verbose:
                    click.echo("Successfully created!")
                break
            except OSError as e:
                if e.errno == 17: # already exists
                    if verbose:
                        click.echo("{} already exists...".format(file), nl=False)
                    if not clobber:
                        click.echo(" not changing it")
                        break
                    if os.path.islink(homefile):
                        os.remove(homefile)
                    elif os.path.isdir(homefile):
                        shutil.rmtree(homefile)
                    else:
                        os.remove(homefile)
                    if verbose:
                        click.echo(" removed!")


if __name__ == "__main__":
    main()
