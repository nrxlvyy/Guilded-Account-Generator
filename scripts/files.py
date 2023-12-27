import os
import json
import random

def getproxy():
    proxies = open("input/proxies.txt", "r", encoding="utf8").read().splitlines()
    return {'https': f'http://{random.choice(proxies)}'}

def getpassword():
    with open(f'input/config.json') as config:
        data = json.load(config)
        return data.get('password', '')

def getinfo(name):
    with open(name, 'r') as file:
        lines = file.readlines()
        return random.choice(lines).strip()

def removeinfo(name, removeline):
    with open(name, 'r') as file:
        lines = file.readlines()

    with open(name, 'w') as removeline:
        for line in lines:
            if line.strip() != removeline:
                file.write(line)