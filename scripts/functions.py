import requests

import datetime
date = datetime.datetime.now().strftime('%H:%M:%S')

from .files import *
from .colors import *

header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    'Content-Type': 'application/json',
    'Cookie': 'guilded_mid=32089b44-dcac-4677-95cf-8648e2a9f338; guilded_ipah=37c9f6c08ecf7fbdd18dd94791db01a7',
    'Guilded-Client-Id': 'f53a9803-4493-4527-b059-c15ae9a24fa7',
    'Guilded-Stag': '3e7d511b58c3b368f343c3012cfefc78',
    'Guilded-Viewer-Platform': 'desktop',
    'Origin': 'https://www.guilded.gg',
    'Referer': 'https://www.guilded.gg/',
    'Sec-Ch-Ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
    'X-Requested-With': 'XMLHttpRequest'
}

def generate():
    proxy = getproxy()
    password = getpassword()
    name = getinfo('input/nicks.txt')
    mail = getinfo('input/emails.txt')

    payload = {
        'email': mail,
        'extraInfo': {'platform': 'desktop'},
        'fullName': 'fddsfs',
        'name': name,
        'password': password
    }

    res = requests.post("https://www.guilded.gg/api/users?type=email", json=payload, headers=header, proxies=proxy)

    if res.status_code == 200:
        print(f"{date} {purple('Generated')} {mail} ")

        logins = f"{mail} | {password} | {name}"

        checker(logins)

        with open('output/generated.txt', 'a') as file:
            file.write(logins + '\n')
    else:
        print(f"{date} {cyan('Failed')} {mail} {res.text} ")

def checker(logins):
    proxy = getproxy()
    mail = logins.split(' | ')[0]
    password = logins.split(' | ')[1]
    name = logins.split(' | ')[2]
    
    payload = {
        "email": mail,
        "getMe": True,
        "password": password
    }

    res = requests.post("https://www.guilded.gg/api/login", json=payload, headers=header, proxies=proxy)

    if res.status_code == 200:
        print(f"{date} {purple('Valid')} {mail} ")

        logins = f"{name} | {mail} | {password}"

        with open('output/valid.txt', 'a') as file:
            file.write(logins + '\n')
    else:
        print(f"{date} {cyan('Dead Account')} {mail} ")
    