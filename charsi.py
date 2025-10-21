import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [•] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/K15UhqX9npaEFy8Hf1fcrm?mode=ems_copy_c')
charsi=platform.architecture()[0]
if charsi=="32bit":
    os.system('clear')
    print('\033[91;1m [•] 32 Bit Device Not Working')
elif charsi=="64bit":
    __import__("zahoorfuckedbycharsi")
