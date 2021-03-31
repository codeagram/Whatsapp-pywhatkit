#!/usr/bin/env python3

import pywhatkit as kit
import pyautogui as pg
from datetime import datetime
import os, sys
from time import sleep


class Whatsapp:

    def __init__(self, phone_numbers):

        self.phone_numbers = phone_numbers

    def get_time(self):

        time_dict = {}
        current_time = datetime.now()

        time_dict['current_hour'] = current_time.hour
        time_dict['current_minute'] = current_time.minute

        return time_dict

    def send_message(self):

        time = self.get_time()
        hour = time['current_hour']
        print(hour)
        minute = time['current_minute']
        minute+=2
        print(minute)
        message = "Hello"

        for number in self.phone_numbers:
            kit.sendwhatmsg(number, message, hour, minute)
            pg.click(1000, 400)
            pg.press("enter")
            minute+=1

        sleep(3)
        self.close_browser()

    def close_browser(self):

        if sys.platform == 'linux':
            browserExe = "chrome"
            os.system("pkill "+browserExe)
        elif sys.platform == 'windows':
            browserExe = "chrome.exe"
            os.system("taskkill /f /im "+browserExe)


# Append phone numbers to the list
numbers = []
pywhat = Whatsapp(numbers)
pywhat.send_message()
