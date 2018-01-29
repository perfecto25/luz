#!/usr/bin/python

from __future__ import print_function
import curses
screen = curses.initscr()

screen.border(0)
screen.addstr(12, 25, "tellme")
screen.refresh()
screen.getch()
curses.endwin()