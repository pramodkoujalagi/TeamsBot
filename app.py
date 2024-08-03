import datetime
import pyautogui
import subprocess
import time
import os
import subprocess
import time
import pandas as pd
from datetime import datetime
import threading
import sys
import webbrowser


lst = [
    # ["https://teams.microsoft.com/l/meetup-join/19%3ameeting_MGFiOTkyY2UtZDdhOC00ZjBmLTg0ZWQtODMwNjRjNDMzMWVj%40thread.v2/0?context=%7b%22Tid%22%3a%2293ae660e-4895-4413-a75e-c5a4de429c0e%22%2c%22Oid%22%3a%224c662de1-8439-4464-8b56-77427d05eb03%22%7d", "09:43"],
    ["https://teams.microsoft.com/l/meetup-join/19%3ameeting_MmIzOGM4ZGYtYWU2Mi00YTE4LTk4MTktYTYzMzQ3NWM2YTE3%40thread.v2/0?context=%7b%22Tid%22%3a%2293ae660e-4895-4413-a75e-c5a4de429c0e%22%2c%22Oid%22%3a%220b19c512-90ff-4614-ae4f-3628c3dc053b%22%7d", "10:59"],
    # ["link3", "3:01"]
]

def join():
    isStarted = False
    for i in lst:
        while isStarted is False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                time.sleep(6)
                def click(image, description, confidence=0.8):
                    if not os.path.exists(image):
                        print(f"Error: {image} does not exist.")
                        return False
                    
                    while True:
                        try:
                            location = pyautogui.locateCenterOnScreen(image, confidence=confidence)
                            if location is not None:
                                pyautogui.click(location)
                                print(f"{description}")
                                return True
                            else:
                                print(f"Couldn't find {description}, retrying...")
                                time.sleep(1)
                        except pyautogui.ImageNotFoundException:
                            print(f"Image not found for {description}, retrying...")
                            time.sleep(1)

                # if not click("teams_app.png", "Joining using Teams app!"):
                #     return
                if not click("mic.png", "Turned off the mic"):
                    return
                if not click("join_now.png", "Joined the meeting!"):
                    return
                # if not click("name.png", "Entering the name"):
                #     return
                # pyautogui.typewrite("IdentifAI")
                # if not click("wjoin.png", "Joining"):
                #     return
                # time.sleep(10)
                # if not click("wjoinwca.png", "Joining with computer audio"):
                #     return
                time.sleep(5)

                # # Enter chat
                # pyautogui.press('tab')
                # pyautogui.press('tab')
                # pyautogui.press('tab')
                # pyautogui.press('tab')
                # pyautogui.press('tab')
                # pyautogui.press('enter')

                # chat_msg1 = ("Hello! I'm IdentifAI, your friendly assistant dedicated to ensuring the authenticity of users on this call. With advanced verification techniques, I'll be seamlessly working in the background to confirm everyone's identity. I'll only be here for a few minutes to carry out verifications and will then exit the call quietly, maintaining the privacy and flow of your discussions!")
                # pyautogui.typewrite(chat_msg1)
                # time.sleep(3)

                # pyautogui.press('enter')
                # time.sleep(3)
                # print("Sent a message in chat")

                # pyautogui.press('tab')
                # pyautogui.press('enter')
                # pyautogui.press('tab')
                # pyautogui.press('enter')
                isStarted = True

join()