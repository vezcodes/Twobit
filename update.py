import requests
import os
import shutil
import re
import psutil

from tqdm import tqdm
from zipfile import ZipFile
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore, Style

from main import THIS_VERSION



def search_for_updates():
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    os.system("title Checking For Updates. . .")
    for i in tqdm(range(100),
                    desc="Searching for updates. . .",
                    ascii=False, ncols=100):
                    sleep(0.003)
    r = requests.get("https://github.com/vezcodes/Twobit/releases/latest", headers=header)
    os.system('cls')
    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]
    if THIS_VERSION not in result_string:
        os.system("title New Update Found!")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'''
                ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                              {Fore.LIGHTRED_EX}Looks like this Twobit {THIS_VERSION} is outdated '''.replace('█', f'{Fore.WHITE}█{Fore.RED}'), end="\n\n")
        choice = str(input(
            f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}You want to update to the latest version? Y/N: {Fore.LIGHTRED_EX}'))

        if choice.upper() == 'Y':
            print(f"{Fore.WHITE}\nUpdating. . .{Fore.RESET}")
            os.system(f'title Updating...')

        else:
            try:
                new_version = requests.get("https://github.com/VezCodez/Twobit/archive/refs/heads/master.zip")
                with open("Twobit-master.zip", 'wb')as zipfile:
                    zipfile.write(new_version.content)
                with ZipFile("Twobit-master.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("Twobit-master.zip")
                cwd = os.getcwd()+'\\Twobit-master'
                shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                shutil.rmtree(cwd)
                os.system('title Successfully Updated!')
                print(f"{Fore.GREEN}Update Successfully Finished!{Fore.RESET}")
                sleep(1)
                os.startfile("run.bat")
                exit()
            except Exception as err:
                os.system('cls')
                print(f"{Fore.LIGHTRED_EX}An error occured while Updating Twobit-{THIS_VERSION}\n\nIf this keeps occuring try and download it manually here github.com/VezCodes/Twobit\n\n\"{err}\"")
                sleep(7)
                input
                return