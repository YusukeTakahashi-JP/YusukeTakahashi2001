import sys,os
import datetime


def main():
    PATH_file = "dummy.txt"
    time = str(datetime.datetime.now())
    with open(PATH_file,'a') as f:
        print(time,file=f)
    
    os.system("git add .")
    os.system("git commit -m {time}")
    os.system("git push")
    return 0

if __name__ == "__main__":
    main()