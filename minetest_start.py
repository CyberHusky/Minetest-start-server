import os, sys
import time
import subprocess

if sys.version_info[0] == 3:
    # for Python3
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import *   ## notice lowercase 't' in tkinter here
    #from filedialog import askopenfilename 
else:
    # for Python2
    import Tkinter as tk
    from Tkinter import *   ## notice capitalized T in Tkinter
    from tkFileDialog import askopenfilename 


def start_1():
    command = 'E:\Download\minetest-5.5.1-win64\minetest-5.5.1-win64\\bin\minetest --server --port 30006 --world test'
    print(command)
    #os.system('cmd /k "Your Command Prompt Command"')

    #os.system('cmd /k "' + command + '"')

    #command2 = 'cmd /k "' + command + '"'
    command3 = command
    proc = subprocess.Popen(command3, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = proc.communicate()
    print(out)
    print(err)

    print('server starts')
    #time.sleep(5)    


def print_btn():
    print('Button pushed')


if __name__ == '__main__':

    #global default_music # directory of music file

    # === Window ===
    window = tk.Tk()
    window.title('SchoolBell. V1.0a')
    window.resizable(300, 300)
    #window.geometry('500x200')


    button_start_1 = Button(window, font=("Ubuntu", 8), text = "Server 1",
                                command = start_1).grid(row = 1, column = 1)
   
    button_2 = Button(window, font=("Ubuntu", 8), text = "Print",
                                command = print_btn).grid(row = 2, column = 1)

        

