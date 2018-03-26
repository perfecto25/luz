#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

import click
import platform
import psutil
from huepy import *
from .commands import disk

@click.group()
@click.version_option()
def cli():
    ''' Luz CLI '''
    pass

cli.add_command(disk.disk)


# @cli.command()
# @click.option('--json', default=None, help='print output in JSON format')
# def os():
#     ''' Operating System information '''
#     click.echo('OS info here')

# @cli.command()
# def Tellme(search_object):
#     click.echo(cyan(search_object) + ': disk')
#     click.echo(search_object)
#     # print(info(platform.machine()))
#     # print(cyan(platform.platform()))
#     # print(green(platform.uname()))
#     # print(info(psutil.disk_usage('/')))


# if __name__ == "__main__":
#     Tellme() 
