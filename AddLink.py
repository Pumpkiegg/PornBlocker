import os
directory = os.path.abspath('')

with open('firstTime.txt','r') as file:
    fT = file.readlines()
    
first=False

if(fT[0]=='True'):
    print("> Thank you for downloading!\n> Be proud of yourself for pushing porn out of your life!")
    first=True
    
fT[0] = 'x'

with open('AddLinkExe.py', 'r') as file:
    lines = file.readlines()
s=input("\n> Input the name of the site you would like to block\n> ")
lines[0] = 'j="'+s+'"\n'
lines[1] = 'fT=False\n'
if(first):
    lines[1]='fT=True\n'
with open('AddLinkExe.py', 'w') as file:
    file.writelines(lines)
    
os.system(directory+"\\AddLinkExe.py")
with open('firstTime.txt','w') as file:
    file.writelines(fT)
