import requests, os, platform, time
from colorama import Fore, Back, Style

print(Fore.CYAN + """

  ________   ______  _____  _    _  _____ 
 |  ____\ \ / / __ \|  __ \| |  | |/ ____|
 | |__   \ V / |  | | |  | | |  | | (___  
 |  __|   > <| |  | | |  | | |  | |\___ \ 
 | |____ / . \ |__| | |__| | |__| |____) |
 |______/_/ \_\____/|_____/ \____/|_____/ 
    _____ _____        __  __ __  __ ______ _____  
  / ____|  __ \ /\   |  \/  |  \/  |  ____|  __ \ 
 | (___ | |__) /  \  | \  / | \  / | |__  | |__) |
  \___ \|  ___/ /\ \ | |\/| | |\/| |  __| |  _  / 
  ____) | |  / ____ \| |  | | |  | | |____| | \ \ 
 |_____/|_| /_/    \_\_|  |_|_|  |_|______|_|  \_\
                                                  
                                                  
                                        
                                          
                      ░                                                                                                                                                                          
"""
+ Fore.YELLOW + "https://github.com/exodus1337/discord_webhook_spammer.git")
print("")

webhook = input(Fore.RED +">>Please enter the Webhook: ") # input for webhook url
text = input(">>Please enter the Message that should be spammed: ") # asks for message

if platform.system() == "Windows": # checking the OS of the device running the tool
    clearcmd = "cls"
else:
    clearcmd = "clear"

os.system(clearcmd)

data = {
    "content": text # data for webhook as json
}
def send(i):
    res = requests.post(webhook, data=data) # sends data to webhook
    try:
        print(Fore.RED + 'getting ratelimited, waiting ' + str(res.json()["retry_after"]) + 'ms.')
        # response: {'global': False, 'message': 'You are being rate limited.', 'retry_after': 12345)}
        time.sleep(res.json()["retry_after"]/1000)
        res = 'waited ' + Fore.RED + str(res.json()["retry_after"]) + 'ms.'
    except:
        i += 1
        res = "Sent message " + text + " successful."
    print(Fore.MAGENTA + res + Fore.MAGENTA + ' Amount of messages already sent: ' + Fore.CYAN + str(i)) # message for feedback lol
    return i
i = 0
while True: #loop
   i = send(i)
