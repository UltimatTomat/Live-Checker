import subprocess
import requests
import time
from datetime import datetime
import pyautogui as pg

channelName = input("Streamer name: ")
Url = "https://www.twitch.tv/" + channelName.lower()
Message1 = " is live."
Message2 = " is not live."
Char1 = "["
Char2 = "]"
Char3 = "] "

def timeLog(str):
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M:%S")
    formatted_time = f"{Char1}{current_time}{Char2}"
    print(formatted_time, str)

def getTime():
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M:%S")
    global formatted_time
    formatted_time = f"{Char1}{current_time}{Char3}"
   
def antiShutdown():
    time.sleep(15)
        pg.moveTo(500, 500)
        time.sleep(15)
        pg.moveTo(600, 600)

while True:
    contents = requests.get('https://www.twitch.tv/' + channelName.lower()).content.decode('utf-8')
    
    if 'isLiveBroadcast' in contents:
        Message = f"{channelName}{Message1}"
        timeLog(Message)
        subprocess.Popen([r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", Url])
        time.sleep(30)
        pg.click(1112, 653)
        time.sleep(3)
        getTime()
        pg.write(formatted_time, interval=0.1)
        time.sleep(0.1)
        pg.write("This is UltimatTomat's very awesome LiveChecker bot. !lurk\n", interval=0.1)
        time.sleep(2)
        pg.write("Here you can see the code: ...\n", interval=0.1)
        break
    else:
        Message = f"{channelName}{Message2}"
        timeLog(Message)
        antiShutdown()
        time.sleep(15)

#Works with any streamer.
