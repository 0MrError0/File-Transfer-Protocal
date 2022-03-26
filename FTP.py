import socket
import os
import subprocess
from datetime import datetime,date
import time
import sys
import shutil

today=date.today()
now=datetime.now()

DEFAULT_PORT=20     

class Display_Layout:
    def layout():
        subprocess.run('clear',shell=True)
        print("              (ffffffffffff)                                    ")
        print("             (f            f)   SECURE TRANSFER \              ")
        print("   ---------(f  _  ___   _  f) ------------------\             ")
        print(" ---------(ff  |_   |   |_)  ff) ----------------/            ")
        print("         (ff  _|____|___|__   ff)       \       /              ")
        print("   -----(ff  File Transfer     ff)------ \                         ")
        print("    ---(ff          Protocol    ff)----- /                        ")
        print("      (ff                        ff)    /                    ")
        print("     (ffffffffffffffffffffffffffffff)                        ")
        print("              __(   |   )__                                ")
        print("             (_____________)                           ")
        print("                                                       ")
        print("                            VERSION :: 0.1                ")
        print("                            DEVELOPED BY ::-              ")
        print("                                             MR ERROR {SOLO BOY}    ")

class Display_Menu:
    def Display_Input():
        #subprocess.run('cls',shell=True)
        print("\n")
        print("\n")
        print(" "*8,"-"*25)
        print("          [01] SEND FILE ")
        print("          [02] RECIVE FILE ")
        print("          [03] CHECK HISTORY ")
        print("          [04] HELP")
        print("          [05] ABOUT")
        print("          [06] EXIT")
        print(" "*8,"-"*25)
        ch=input("          [*] Enter Your Choice :: ")
        return ch

class File_Configure:
    def File_DATA_Configur():
        for i in range(1,9,1):
            subprocess.run('clear',shell=True)
            print("[*] Setting up Configuration Process |")
            time.sleep(0.01)
            subprocess.run('clear',shell=True)
            print("[*] Setting up Configuration Process /")
            time.sleep(0.01)
            subprocess.run('clear',shell=True)
            print("[*] Setting up Configuration Process -")
            time.sleep(0.01)
            subprocess.run('clear',shell=True)
            print("[*] Setting up Configuration Process \\")
            time.sleep(0.01)
        os.makedirs("/storage/emulated/0/Android/Config/")
        print("[*] Directory Created sucessfully")
        file=open("/storage/emulated/0/Android/Config/data.txt",'x')
        file.close()
        print("[*] File Axcess Granted")
        time.sleep(2)
        with open("/storage/emulated/0/Android/Config/data.txt",'w') as Write_Content:
            Write_Content.write("  DATE     FILE NAME        HOST NAME      PORT NO       STATUS     TIME \n")
            print("[*] File Written Sucessfully")
            time.sleep(2)
            return 0
        print("[*] Run This Application Again ")
        return 0

class Connection:
    def Start_Connection_send(IP_ADDR,PORT):
        socket_Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_Connection.bind((IP_ADDR,PORT))
        socket_Connection.listen(1)
        print(" "*8,"Wating for RECEVER To Connect !!")
        Client, ADDRESS = socket_Connection.accept()
        value=0
        i=0
        while value!=1:
            try:
                file_Name=input("Enter The File :: ")
                Client.send(bytes(file_Name,'utf-8'))
                file=open("/storage/emulated/0/Android/Config/"+file_Name,'rb')
            except:
                print(" "*8,"[*] FILE NOT FOUND !!")
                layout()
                display()
            for i in range(1,101,1):
                n=i+1
                subprocess.run('clear',shell=True)
                print(" "*8,"-"*55)
                print(" "*8,"FILE NAME "+"       HOST NAME "+"        PORT NO "+"     STATUS")
                print(" "*8,"-"*55)
                print(" "*8,file_Name ,"        ",IP_ADDR,"       ",PORT,"  ","      ",i,"%")
                print(" "*8,"-"*55)
                print("")
                time.sleep(0.001)
                if i==100:
                    File_Data=file.read(1024)
                    Client.send(File_Data)
                    date=today.strftime("%b-%d-%y")
                    t=now.strftime("%H:%M:%S")
                    file.close()
                    print("[*] File Sucessfully SENDED ")
                    PORT=str(PORT)
                    all_data=["\n      ",date,"      ",file_Name,"        ",IP_ADDR,"       ",PORT,"  ","      ","S 100%     ",t,"\n"]
                    data_file=open("/storage/emulated/0/Android/Config/data.txt",'a')
                    data_file.writelines(all_data)
                    data_file.close()
                    time.sleep(2)
                    value=int(input("        Enter 1 to Go Back :: "))
                    if value==1:
                        socket_Connection.close()
                        Control()
                    else:
                        socket_Connection.close()
                        Control()
                else:
                    pass
        
    def Start_Connection_recv(IP_ADDR,PORT):
        socket_Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_Connection.connect((IP_ADDR,PORT))
        print(" "*8,"[*]Connected TO SENDER !!")
        value=0
        i=0
        while value!=1:
            File_Name=socket_Connection.recv(1024).decode()
            for i in range(1,101,1):
                n=i+1
                subprocess.run('clear',shell=True)
                print("-"*55)
                print(" "*8,"FILE NAME "+"       HOST NAME "+"        PORT NO "+"     STATUS")
                print(" "*8,"-"*55)
                print(" "*8,File_Name,"        ",IP_ADDR,"       ",PORT,"  ","      ",i,"%")
                print(" "*8,"-"*55)
                print("")
                time.sleep(0.001)
                if i==100:
                    file=open("/storage/emulated/0/Android/Config/"+File_Name,'wb')
                    File_Data=socket_Connection.recv(1024)
                    d=today.strftime("%b-%d-%y")
                    t=now.strftime("%H:%M:%S")
                    file.write(File_Data)
                    file.close()
                    print(" "*8,"[*] File Sucessfully RECIVED ")
                    PORT=str(PORT)
                    all_data=["\n      ",d,"      ",File_Name,"        ",IP_ADDR,"       ",PORT,"  ","      ","R 100%     ",t,"\n"]
                    data_file=open("/storage/emulated/0/Android/Config/data.txt",'a')
                    data_file.writelines(all_data)
                    data_file.close()
                    time.sleep(2)
                    value=int(input("        Enter 1 To Go Back :: "))
                    if value==1:
                        socket_Connection.close()
                        Control()
                    else:
                        socket_Connection.close()
                        Control()
                else:
                    pass
class History:
    def DATA_HISTORY():
        print(" "*8,"-"*70)
        with open("/storage/emulated/0/Android/Config/data.txt","r") as file_data:
            file_data_Contents=file_data.read()
            print(" "*8,file_data_Contents)
        print(" "*8,"-"*70)
        g=input("        [*] Enter 1 To Go Back :: ")
        if g=='1':
            Control()
        else:
            Control()


class Help:        
    def HELP():
        print("\n")
        print(" "*8,"[*] Enter 1 For To SEND FILE")
        print(" "*8,"[*] Enter 2 For To RECIVE FILE")
        print(" "*8,"[*] Enter 3 For To CHECK HISTORY")
        print(" "*8,"[*] Enter 4 For To Get Help")
        print(" "*8,"[*] Enter 5 For To Get INFO")
        print(" "*8,"[*] Enter 6 For To EXIT")
        g=input("        [*] Enter 1 To Go Back :: ")
        if g=='1':
            Control()
        else:
            Control()

class FORMAT:            
    def Format_Config():
        subprocess.run('clear',shell=True)
        try:
            shutil.rmtree("/storage/emulated/0/Android/Config/")
            print("[*] Sucessfully Formated")
            time.sleep(2)
            print("[*] Run This APPLICATION Again")
        except OSError as e:
            print("Error : ",e)

class BOOT_CHECK_FILE:
    def Check_File_Exists():
        Checking_Exists=os.path.isfile("/storage/emulated/0/Android/Config/data.txt")
        if Checking_Exists==True:
            return 1
        else:
            print(" "*8,"[*] LOADING DATA")
            File_Configure.File_DATA_Configur()
            sys.exit(0)
            return 0
class INFO:
    def info():
        print("[*] Developed By Mr Error The Solo Boi")
	#print("[*] Developed By Mr Error The Solo Boi")
        g=input("        [*] Enter 1 To Go Back :: ")
        if g=='1':
            Control()
        else:
            Control()


def Control():
    r=BOOT_CHECK_FILE.Check_File_Exists()
    if r==1:
        Display_Layout.layout()
        User_Choice=Display_Menu.Display_Input()
        if User_Choice=='1':
               IP_ADDR=input("        [*] Enter RECEVER's IP ADDRESS :: ")
               PORT=int(input("        [*] Enter PORT Number default 20 :: "))
               Connection.Start_Connection_send(IP_ADDR,PORT)
        elif User_Choice=='2':
            IP_ADDR=input("        [*] Enter RECEVER's IP ADDRESS :: ")
            PORT=int(input("        [*] Enter PORT Number default 20 :: "))
            Connection.Start_Connection_recv(IP_ADDR,PORT)
        elif User_Choice=='3':
            History.DATA_HISTORY()
        elif User_Choice=='4':
            Help.HELP()
        elif User_Choice=='5':
            INFO.info()
        elif User_Choice=='6':
            sys.exit(0)
        elif User_Choice=='FORMAT'or'format':
            n=input("        [*] Are You Sure ALL THE DATA HISTORY WILL BE DELETED (Y/N):: ")
            if n=='y'or'Y':
                FORMAT.Format_Config()
            else:
                Control()
        else:
            print("Invalid Command")
            time.sleep(3)
            Display_Layout.layout()
            Control()
        
    else:
        print("[*] Cant LOAD")

Control()

        
        
