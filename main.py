import os
import json
import urllib.request
import requests
import time

from colorama import Fore, Style
from time import sleep

THIS_VERSION = "1.1"

banner = Fore.BLUE + Style.BRIGHT + f'''
    
████████╗░██╗░░░░░░░██╗░█████╗░██████╗░██╗████████╗
╚══██╔══╝░██║░░██╗░░██║██╔══██╗██╔══██╗██║╚══██╔══╝
░░░██║░░░░╚██╗████╗██╔╝██║░░██║██████╦╝██║░░░██║░░░
░░░██║░░░░░████╔═████║░██║░░██║██╔══██╗██║░░░██║░░░
░░░██║░░░░░╚██╔╝░╚██╔╝░╚█████╔╝██████╦╝██║░░░██║░░░
░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░╚════╝░╚═════╝░╚═╝░░░╚═╝░░░
    By Vez Codez
    https://github.com/VezCodes
    '''
def check_for_update():
    pass

def tool():
    os.system('cls')
    print(banner)
    print(Fore.GREEN + f"Successfully loaded the tool!\nPlease wait for the first following update!")

def login():
    print(banner)
    os.system(f'title [ Twobit by Vez Codez v{THIS_VERSION}]')

    registerURL = ('https://canary.discord.com/api/webhooks/927498438151639060/y0ZlNy0kxIhcQjgTjp0BH_4tMpHA2FhZen4bJ22jrnFxgVLC3txCv_ICz7hiT90odSh3')

    url = ('http://vezcodez.c1.biz/private/login.json')

    r = requests.get(url)

    y = r.json()  
    
    credentials = input(Fore.CYAN + f"]>> Please insert your personal ID to login, or type register to sign-up > ")

    if credentials in y["ids"]:
        print(Fore.GREEN + f"Successfully logged in as {credentials}\nContinuing in 3 seconds. . .")
        time.sleep(3)
        tool()

    
    elif credentials == "register":
        os.system("cls")
        print("1. Go to https://numbergenerator.org/random-8-digit-number-generator\n2. Generate an ID\n3. Put in your gamer tag with the ID\nExample: sfyx12345678\n[!] NO CAPITAL LETTERS!!")
        print(" ")
        register = input(Fore.YELLOW + f"]>> Please enter your personal login ID as shown above > ")
        
        
        data = {"content": f'''@everyone new sign-up request: `{register}`'''}
        response = requests.post(registerURL, json=data)
        time.sleep(1)
        print("Successfully sent request!\nThis process can take up to 6 hours, so be patient!\nClosing in 3 seconds. . .")
        time.sleep(3)
        os.system("exit()")


    else:
        print("[!] An error occured.")



login()