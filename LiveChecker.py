import subprocess
import requests
import time
from datetime import datetime

channelName = input("Streamer name: ")
contents = requests.get('https://www.twitch.tv/' + channelName.lower()).content.decode('utf-8')
Url = "https://www.twitch.tv/" + channelName.lower()
Message1 = " is live."
Message2 = " is not live."
Char1 = "["
Char2 = "] "

while True:
    if 'isLiveBroadcast' in contents:
        time_now = datetime.now()
        current_time = time_now.strftime("%H:%M:%S")
        formatted_time = f"{Char1}{current_time}{Char2}"
        print(f"{formatted_time}{channelName}{Message1}")
        subprocess.Popen([r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", Url])
        break
    else:
        time_now = datetime.now()
        current_time = time_now.strftime("%H:%M:%S")
        formatted_time = f"{Char1}{current_time}{Char2}"
        print(f"{formatted_time}{channelName}{Message2}")
        time.sleep(30)

#Works with any streamer.
