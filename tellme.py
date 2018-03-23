#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

import click
import platform
import psutil
from huepy import *

print(info(platform.machine()))
print(cyan(platform.platform()))
print(green(platform.uname()))
print(info(psutil.disk_usage('/')))


if __name__ == "__main__":
    App = TellMe()
    App.run()⏎  
