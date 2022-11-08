import requests as r
import json
import time
from threading import Thread
import csv
from random import choice
import random
import colorama
from colorama import Fore, Back, Style
colorama.init()

def func_post_art(chat_id, message, user_token):
    header = {
        'authorization': user_token
    }
    chat_id = chat_id
    s = r.Session()
    s.headers = header
    files = {'file': open(f'arts/{message}', 'rb')}
    resp = s.post(f'https://discord.com/api/v9/channels/{chat_id}/messages', files=files)

def func_post_mem(chat_id, message, user_token):
    header = {
        'authorization': user_token
    }
    chat_id = chat_id
    s = r.Session()
    s.headers = header
    files = {'file': open(f'memes/{message}', 'rb')}
    resp = s.post(f'https://discord.com/api/v9/channels/{chat_id}/messages', files=files)

print(Fore.LIGHTGREEN_EX)
print('''
                               ....
                                    %
                            L
                            "F3  $r
                           $$$$.e$"  .
                           "$$$$$"   "
  (FovImageBot)              $$$$c  /
        .                   $$$$$$$P
       ."c                      $$$
      .$c3b                  ..J$$$$$e
      4$$$$             .$$$$$$$$$$$$$$c
       $$$$b           .$$$$$$$$$$$$$$$$r
          $$$.        .$$$$$$$$$$$$$$$$$$
           $$$c      .$$$$$$$  "$$$$$$$$$r


*** Hello, I'm FovImageBot, for my work fill the files:
 	user_tokens.txt, art_chats.txt, mem_chats.txt and put 
 	arts and memes in the same name directory and number 
 	them from one ***
''')
print(Fore.LIGHTWHITE_EX)

array_users_first = []
array_users_last = []

array_mchats_first = []
array_mchats_last = []
array_achats_first = []
array_achats_last = []

array_mfile_first = []
array_mfile_last =[]
array_afile_first = []
array_afile_last =[]

project_num = int(input('Enter the number of projects: '))
for i in range (0, project_num):
    u1 = int(input(f'Enter the number of first user in {i+1} project: '))
    u1 -= 1
    array_users_first.append(u1)
    u2 = int(input(f'Enter the number of last user in {i+1} project: '))
    array_users_last.append(u2)

    mc1 = int(input(f'Enter the number of first mem-chat in {i+1} project: '))
    mc1 -= 1
    array_mchats_first.append(mc1)
    mc2 = int(input(f'Enter the number of last mem-chat in {i+1} project: '))
    array_mchats_last.append(mc2)
    ac1 = int(input(f'Enter the number of first art-chat in {i+1} project: '))
    ac1 -= 1
    array_achats_first.append(ac1)
    ac2 = int(input(f'Enter the number of last art-chat in {i+1} project: '))
    array_achats_last.append(ac2)

    mf1 = int(input(f'Enter the number of first mem-file in {i+1} project: '))
    array_mfile_first.append(mf1)
    mf2 = int(input(f'Enter the number of last mem-file in {i+1} project: '))
    array_mfile_last.append(mf2)
    af1 = int(input(f'Enter the number of first art-file in {i+1} project: '))
    array_afile_first.append(af1)
    af2 = int(input(f'Enter the number of last art-file in {i+1} project: '))
    array_afile_last.append(af2)

user_token_set: list = open('user_tokens.txt', 'r', encoding='utf-8').read().splitlines()
memes_chat_set: list = open('mem_chats.txt', 'r', encoding='utf-8').read().splitlines()
arts_chat_set: list = open('art_chats.txt', 'r', encoding='utf-8').read().splitlines()
delay_min = int(input('Enter min delay for sending images: '))
delay_max = int(input('Enter max delay for sending images: '))
total_sent = 0

print()
print('*** Starting to send images ***')
print()

while True:
    for i in range(0, project_num):

        user_number = random.randint(array_users_first[i], array_users_last[i] - 1)
        user_token = user_token_set[user_number]

        memes_chat_number = random.randint(array_mchats_first[i], array_mchats_last[i] - 1)
        current_chat_id = memes_chat_set[memes_chat_number]


        mem_number = random.randint(array_mfile_first[i], array_mfile_last[i])
        func_post_mem(current_chat_id, f'{mem_number}.jpg', user_token)
        print(Fore.LIGHTBLUE_EX + f'Sending mem in {memes_chat_number} chat from user {user_number}')
        total_sent += 1

        sleep_time = random.randint(3,8)
        time.sleep(sleep_time)

        arts_chat_number = random.randint(array_achats_first[i], array_achats_last[i] - 1)
        current_chat_id = arts_chat_set[arts_chat_number]

        art_number = random.randint(array_afile_first[i], array_afile_last[i])
        func_post_art(current_chat_id, f'{art_number}.jpg', user_token)
        print(Fore.LIGHTBLUE_EX + f'Sending art in {arts_chat_number} chat from user {user_number}')
        total_sent += 1


        print(Fore.LIGHTWHITE_EX + f'*** Total sent {total_sent} images ***')

    delay = random.randint(delay_min, delay_max)
    print()
    print(Fore.LIGHTCYAN_EX + f'{delay} seconds pause')
    print()
    time.sleep(delay)
