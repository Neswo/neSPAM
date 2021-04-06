import requests
import pickle
import os
import time

ccwebhook = "undefined"
cctoken = "undefined"
fileisfound = "undefined"
loadisenabled = False

def webhookspam():
    global ccwebhook
    if loadisenabled == False:
        ccwebhook = input("(Webhook)> ")
    ccmessage = input("(Message)> ")
    ccnbr = int(input("(Number of messages)> "))

    save()

    truc = 1
    while truc <= ccnbr:
        requests.post(ccwebhook, json={'content':f'{ccmessage}'})
        print("\n\n║ neSPAM | Discord spammer | By NESWO")
        print('║ Message sent ->',truc,'of',ccnbr,')','| Progress:',100*truc//ccnbr,"%")
        truc += 1
        time.sleep(0.5)
    else:
        os.system('cls')
        os.system('color A')
        print("║ neSPAM | Discord spammer | By NESWO")
        print('║',ccnbr,'messages has been sent with success !\n')
        os.system('pause')
        os.system('color 07')
        os.system('cls')

def userspam():
    global cctoken
    if loadisenabled == False:
        cctoken = input("(Token)> ")
    ccmessage2 = input("(Message)> ")
    ccidchannel = input("(Channel ID)> ")
    ccnbr2 = int(input("(Number of messages)> "))

    ccheaders = {
        'Authorization':cctoken
    }

    save()

    truc = 1
    while truc <= ccnbr2:
        requests.post(f'https://discordapp.com/api/v6/channels/{ccidchannel}/messages', headers=ccheaders, json={'content': f'{ccmessage2}'})
        print("\n\n║ neSPAM | Discord spammer | By NESWO")
        print('║ Message sent ->',truc,'of',ccnbr2,')','| Progress:',100*truc//ccnbr2,"%")
        truc += 1
        time.sleep(1)
    else:
        os.system('cls')
        os.system('color A')
        print("║ neSPAM | Discord spammer | By NESWO")
        print('║',ccnbr2,'messages has been sent with success !\n')
        os.system('pause')
        os.system('color 07')
        os.system('cls')

def save():
    savedata = {
        "ccwebhook": ccwebhook,
        "cctoken": cctoken,
    }
    with open('savefile','wb') as savefile:
        savepickler = pickle.Pickler(savefile)
        savepickler.dump(savedata)

def load():
    global ccwebhook
    global cctoken

    with open('savefile','rb') as savefile:
        savedepickler = pickle.Unpickler(savefile)
        dataloader = savedepickler.load()
        cctoken = dataloader["cctoken"]
        ccwebhook = dataloader["ccwebhook"]

print(".  .                       \n|\ |                       \n| \| ,-. ,-. ;-. ,-: ;-.-. \n|  | |-' `-. | | | | | | | \n'  ' `-' `-' |-' `-` ' ' ' \n             '             ")
print("--------------------------\n- simple discord spammer -\n--------------------------\n- 1 - Webhook mode\n- 2 - User mode\n--------------------------\n")

choice = str(input("(Choice)> "))

dir_path = os.path.dirname(os.path.realpath(__file__))

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.startswith("savefile"):
            fileisfound = True
            print(">> Save file found, do you want to use your precedent webhook/token ?\n/!\ You may have only one mode saved, if you don't remember using this mode, please start from 0\n")
            answer = input("(Y/N)> ").upper()
            if answer == "Y":
                load()
                print(">> Ok, loading precedent webhook/token\n")
                loadisenabled = True
            if answer == "N":
                print(">> Ok, starting from 0\n")
        if fileisfound == False:
            print(">> No save file found, starting from 0\n")


if choice == "1":
    webhookspam()
    
if choice == "2":
    userspam()