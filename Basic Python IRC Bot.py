import socket  # imports module allowing connection to IRC
import threading  # imports module allowing timing functions

# sets variables for connection to twitch chat
authlist = "Donkeymasher"
#People who can give the bot commands

bot_owner = 'Donkeymasher'
#Owner of the bot -- This doesn't matter for twitch --

nick = 'Goldencarrotbot'
#Name of the bot (Must be a twitch account)

channel = '#donkeymasher'
#Channel bot will be working

server = 'irc.twitch.tv'
#Server where bot will be working

password = ''
#Authentication key

queue = 0
#sets variable for anti-spam queue functionality -- I don't know if this works --

irc = socket.socket()
#basically this calls the socket function which you pass your server and port into look below.

irc.connect((server, 6667))
#connects to the server

#sends variables for connection to twitch chat
irc.send('PASS ' + password + '\r\n')
irc.send('USER ' + nick + ' 0 * :' + bot_owner + '\r\n')
irc.send('NICK ' + nick + '\r\n')
irc.send('JOIN ' + channel + '\r\n')

data = ""
Hcount = 0
caps_1 = ""
msg_1 = ""
while True:

    def message(msg):
        irc.send("PRIVMSG " + channel + " :" + msg + "\n")

    data = irc.recv(1204)  #gets output from IRC server
    user = data.split(':')[1]
    user = user.split('!')[0]#determines the sender of the messages
    msg_1 = data[77:]
    print(user)
    print(data)
    print(msg_1)


    if '!Ping' in data:
        irc.send(data.replace('Ping', 'Pong'))  #responds to PINGS from the server

    if 'balls' in msg_1:
        message("YOLO")

    if 'huggles' in msg_1:
        Hcount = (Hcount + 1)
        message('Right back at you')

    if '!Hello' in msg_1:  #!test command
        irc.send(data.replace('!hello', 'Hi'))

    if 'Yo' in msg_1 and 'donkeymasher' in user:
        message('Hey Donkey')

    if '!SHCount' in msg_1:
        message(str(Hcount))

    if str.isupper(msg_1) == 1:
        message(str.title(user)+' please do not talk in full caps')
