import os
import requests
from dhooks import Webhook
import time

os.system("title Discord Webhook Deleter")

def banner():
    print("""

Discord Webhook Deleter

        Input Webhook URL

    """)

def nuker():
    start = input(">")
    hook = Webhook(start)
    hook.send("This webhook has forcefully been deleted :joy:")
    x = requests.delete(start)

def end():
    print("Successfully nuked webhook\n")
    print("Closing in 10 seconds...")
    time.sleep(10)
    os.system("exit")


banner()
nuker()
end()
