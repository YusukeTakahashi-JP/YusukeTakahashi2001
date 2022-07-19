import sys,os
import datetime


def main():
    PATH_file = "C:\\Users\\yusuk\\Desktop\\YusukeTakahashi2001\\dummy.txt"
    time = str(datetime.datetime.now())
    with open(PATH_file,'a') as f:
        print(time,file=f)
    
    os.system("git add .")
    os.system("git commit -m {time}")
    os.system("git push")
    return 0

main()