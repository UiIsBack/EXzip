from pystyle import *
from pyunpack import Archive
import os
from zipfile import ZipFile
import sys, time
banner = '''

ooooooooooo ooooo  oooo             o88              
 888    88    888  88   ooooooooooo oooo ooooooooo   
 888ooo8        888          8888    888  888    888 
 888    oo     88 888     8888       888  888    888 
o888ooo8888 o88o  o888o o888ooooooo o888o 888ooo88   
                                         o888      


'''

droppedFile = sys.argv[1]
def unpackzip():
    try:
        with ZipFile(droppedFile, 'r') as zipObj:

            zipObj.extractall('.')
            print(f"{Col.yellow}[+]{Col.green}Unpacked zip {zipObj.filename}"); 
    except:
        print(f"{Col.yellow}[-]{Col.red}Error!")
        time.sleep(2); sys.exit()
def unpackrar():
    try:
        Archive(droppedFile).extractall('.')
        print(f"{Col.yellow}[+]{Col.green}Unpacked rar {droppedFile}")
    except:
        print(f"{Col.yellow}[-]{Col.red}Error!")
        time.sleep(2); sys.exit()
Write.Print(f"{banner}", Colors.purple_to_blue, interval=0)
if droppedFile.endswith(".zip"):
    unpackzip()  
elif droppedFile.endswith(".rar"):
    unpackrar()
else:
    print(f"{Col.yellow}[-]{Col.red}Extension not supported:("); time.sleep(4); sys.exit()
try:
 os.remove(droppedFile)
except:
    print(f"{Col.yellow}[-]{Col.red}error"); time.sleep(3)
time.sleep(3)
