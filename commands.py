import os
import invite
import re
import shutil

def add(cmd):
    if len(cmd) < 3:
        invite.root.print_screen("[!] ERROR [!] COMMAND : add fileExtension name")
    else:
        extension = cmd[1]
        file_name = ''
        if len(cmd) == 2:
            file_name = cmd[2]
        elif len(cmd) > 2:
            file_name = cmd[2]
            for arg in cmd[3:]:
                file_name += ' ' + arg
        try:
            file = open(file_name + '.' + extension, 'x')
            file.close()
        except FileExistsError:
            print("[!] ERROR [!] un fichier avec ce nom existe déjà")
            invite.root.print_screen("[!] ERROR [!] There is already a file named {} in this path".format(file_name))

def rem(cmd):
    if len(cmd) < 2:
        invite.root.print_screen("[!] ERROR [!] COMMAND : rem fileName")
    else:
        file_name = ''
        if len(cmd) == 2:
            file_name = cmd[1]
        elif len(cmd) > 2:
            file_name = cmd[1]
            for arg in cmd[2:]:
                file_name += ' ' + arg
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("[!] ERROR [!] Name error")
            invite.root.print_screen("[!] ERROR [!] This file doesn't exist")

def cd(cmd):
    if len(cmd) < 2:
        invite.root.print_screen("[!] ERROR [!] COMMAND : cd folderName")
    else:
        path = ''
        if len(cmd) == 2:
            path = cmd[1]
        elif len(cmd) > 2:
            for arg in cmd[1:]:
                path += ' ' + arg
        try:
            print(path)
            os.chdir(path)
        except FileNotFoundError:
            print("[!] ERROR [!] Name error")
            invite.root.print_screen("[!] ERROR [!] This folder doesn't exist")

def cdlist(cmd):
    if len(cmd) > 1:
        invite.root.print_screen("[!] ERROR [!] COMMAND : cdlist")
    else:
        path = os.getcwd()
        try:
            files = os.listdir(path)
            for file in files:
                invite.root.print_screen(' -' + file)
        except FileNotFoundError:
            print("[!] ERROR [!] Name error")
            invite.root.print_screen("[!] ERROR [!] This folder doesn't exist")

def ren(cmd):
    if len(cmd) < 2:
        invite.root.print_screen("[!] ERROR [!] COMMAND : ren oldName;newName")
    else:
        old_name = ''
        new_name = ''
        files_name = cmd[1]
        for arg in cmd[2:]:
            files_name += ' ' + arg
        files_name = files_name.split(';')
        old_name = files_name[0]
        new_name = files_name[1]       
        try:
            os.rename(old_name, new_name)
        except FileNotFoundError:
            invite.root.print_screen("[!] ERROR [!] File doesn't exist")

def addfold(cmd):
    if len(cmd) < 2:
        invite.root.print_screen("[!] ERROR [!] COMMAND : addfold foldName")
    else:
        fold_name = cmd[1]
        for arg in cmd[2:]:
            fold_name += ' ' + arg
        os.mkdir(os.getcwd() + '/' + fold_name + '/')

def remfold(cmd):
    if len(cmd) < 2:
        invite.root.print_screen("[!] ERROR [!] COMMAND : remfold foldName")
    else:
        fold_name = cmd[1]
        for arg in cmd[2:]:
            fold_name += ' ' + arg
        shutil.rmtree(os.getcwd() + '/' + fold_name + '/')