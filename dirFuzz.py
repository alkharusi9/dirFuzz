#!/usr/bin/python3 


import sys,os
import time
import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner():
	print('''

       __ _               ______                
  ____/ /(_)_____        / ____/__  __ ____ ____
 / __  // // ___/______ / /_   / / / //_  //_  /
/ /_/ // // /   /_____// __/  / /_/ /  / /_ / /_
\__,_//_//_/          /_/     \__,_/  /___//___/ 
   
      #Coded by: Alsalt Alkharosi @0x_pwner

''')


def dirFuzz():
    target = sys.argv[1]
    file_name = sys.argv[2]
    wordlist = open(file_name, 'r')
    output = open('targets.vcs', 'w')

    print(bcolors.OKBLUE + '[!] Please wait, looking for valid directories....' + bcolors.ENDC)
    time.sleep(1)
    print(bcolors.OKBLUE + '[!] Still scanning.....' + bcolors.ENDC)
    time.sleep(2)
    for x in wordlist.readlines():
        try:
            directory = x.strip('\n')
            url = 'http://'+ target + '/' + directory   # You may change (http://) to (https://) if the target requires SSL.
            r = requests.get(url)
            if r.status_code == 200:
                print(bcolors.OKGREEN + '[+]' + url + '\n' + bcolors.ENDC)
                output.write(bcolors.OKGREEN + '[+]' + url + bcolors.ENDC)

            else:
                print(bcolors.FAIL + '[-]' + url + bcolors.ENDC)
        except Exception as e:
            print(e)

        except KeyboardInterrupt:
            print(bcolors.WARNING + '[!] You clicked CTRL+C to stop the scan!' + bcolors.ENDC)
            break

if __name__=='__main__':
	banner()
	dirFuzz()
