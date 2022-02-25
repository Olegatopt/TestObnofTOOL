import os
import sys
import colorama
import time
from time import sleep
from colorama import init, Fore, Back
init(autoreset=True)
print("ВНИМАНИЕ ВЫПОЛНЯЕТСЯ ПРОВЕРКА КОМПОНЕНТОВ ОНИ САМИ СКАЧАЮТСЯ ЕСЛИ БУДЕТ НУЖНО")
os.system("pip install -r requirements.txt")
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
file = open('Input.txt', encoding='utf-8')
print(Back.GREEN + '', Back.BLACK + "                                              ", Back.GREEN + '')
print(Back.GREEN + '', Back.BLACK + "                                              ", Back.GREEN + '')
print(Back.GREEN + '', Fore.GREEN + "ANONYM HACK | (@nicecoolw)" , Back.GREEN + '')
print(Back.GREEN + '', Fore.GREEN + "Инструменты от ANONYM HACK (@nicecoolw)" + ' ', Back.GREEN + '')
print(Back.GREEN + '', Fore.GREEN + "Инструменты от ANONYM HACK (@nicecoolw)",  Back.GREEN + '')
print(Back.GREEN + '', Fore.GREEN + "Инструменты от ANONYM HACK (@nicecoolw)",  Back.GREEN + '')
print(Back.GREEN + '', Fore.GREEN + "Инструменты от ANONYM HACK (@nicecoolw)", Back.GREEN + '')
print(Back.GREEN + '', Fore.GREEN + "Инструменты от ANONYM HACK (@nicecoolw)", Back.GREEN + '')
print(Back.GREEN + '', Fore.GREEN + "Инструменты от ANONYM HACK (@nicecoolw)", Back.GREEN + '')
print(Back.GREEN + '', Fore.GREEN + "Инструменты от ANONYM HACK (@nicecoolw)" + '    ', Back.GREEN + '')
print(Back.RED + '', Fore.RED + "     0.4.3 beta       ", Back.RED + '')
print(Back.GREEN + '', Fore.GREEN + "Добавлено: Исправлен Zphisher, Испрвлены мелкие баги, Добавлен лого", Back.RED + '')
print(Back.GREEN + '', " =============================================", Back.GREEN + '')
print(Back.GREEN + '', "        Made by", Fore.CYAN + "@nicecoolw                " + '      ', Back.GREEN + '')
print(Back.GREEN + '', "        Updates:", Fore.CYAN + "https://t.me/naviborsb" + '      ', Back.GREEN + '')
print(Back.GREEN + '', " =============================================", Back.GREEN + '')
print(Back.GREEN + '', Back.BLACK + "                                              ", Back.GREEN + '')
print(Back.GREEN + '', Fore.YELLOW  + "                  Инструменты" + '                 ', Back.GREEN + '')
print(Back.GREEN + '', Back.BLACK + "                                              ", Back.GREEN + '')
print(Back.GREEN + '', Fore.LIGHTMAGENTA_EX  + " 1.[probiv | AH (beta)]       2.[NiceBomb | beta]       3.[удалено]" + '', Back.GREEN + '')
print(Back.GREEN + '', Back.BLACK + "                                              ", Back.GREEN + '')
print(Back.GREEN + '', Fore.MAGENTA  + " '''''''''''''''''''''''''''''''''''''''''''' ", Back.GREEN + '')
while True:
    inp = int(input(Back.BLACK + ' ' + Back.BLACK + '  <$> ' + Fore.LIGHTBLACK_EX))
    try:
        if inp == 1:
            print(Fore.GREEN + 'Вы выбрали [probiv | AH (beta)]')
            sleep(2)
            if os.sys.platform == "win32":
                os.system("cls")
            else:
                os.system("clear")
            import probivAH
    except Exception:
        print(Fore.RED + 'Ошибка/Неверный формат!')
        sleep(2)
        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        os.execl(sys.executable, sys.executable, *sys.argv)
    try:
        if inp == 2:
            print(Fore.GREEN + 'Вы выбрали [NiceBomb | beta]')
            sleep(2)
            if os.sys.platform == "win32":
                os.system("cls")
            else:
                os.system("clear")
            import nicebomber
    except Exception:
        print(Fore.RED + 'Ошибка/Неверный формат!')
        sleep(2)
        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        os.execl(sys.executable, sys.executable, *sys.argv)
    try:
        if inp == 3:
            print(Fore.GREEN + 'удалено')
            sleep(2)
            if os.sys.platform == "win32":
                os.system("cls")
            else:
                os.system("clear")
    except Exception:
        print(Fore.RED + 'Ошибка/Неверный формат!')
        sleep(2)
        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        os.execl(sys.executable, sys.executable, *sys.argv)
        
        #pip install -r requirements.txt import zphisher




input()
