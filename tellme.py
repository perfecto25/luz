#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

import npyscreen as np
import curses

class ExitButton(np.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm(None)

class TellMe(np.NPSApp):
    def main(self):
        F  = np.FormBaseNew(name = "tellme",)
        os  = F.add(np.TitleText, name = "OS:", max_width=19)
        network = F.add(np.TitleText, name = "Network:", max_width=19)
        exit_btn = F.add(ExitButton, name="Exit", max_width=19)
        display = F.add(np.BoxBasic, rely=1, relx=20)
        F.edit()

        print(ms.get_selected_objects())
    

if __name__ == "__main__":
    App = TellMe()
    App.run()⏎  
