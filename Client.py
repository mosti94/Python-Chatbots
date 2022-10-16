# Client code

import socket
from threading import Thread
import random
import sys
#Global variable

ip = " "
port = 0
flag = True                                                                                                             # Flag variable ta print statement from the host
nickname = None
actions = ["work", "play", "eat", "cry", "sleep", "fight", "steal", "bick", "yell", "complain", "sing", "hugg", "walk"] # Action list contains the word that the bots can use
bad_things = ["crying", "stealing", "fighting", "bickering", "yelling", "complaining"]                                  # List of bad word
good_things = ["singing", "hugging", "playing", "working", "jogging", "walking", "sleeping", "eating"]                  # List of good words
alternatives = ["coding", "singing", "sleeping", "fighting"]                                                            # Alternative list for dora bots
bots = ["host", "bob", "dora", "alice", "chuck"]                                                                        # List of Bots including host making sure that we can only add this connection
# we are using checking the commandline arguments and giving different output if the host is not giving all the
# arguments. we are receive the name of the bot from the commandline arguments.
if len(sys.argv) == 4:                                                                                                  # Checks the length from the input from the terminal
    ip = str(sys.argv[1])                                                                                               # Taking the second value that the user uses as the IP address
    port = int(sys.argv[2])                                                                                             # Taking the third value as the port number
    for bot in bots:                                                                                                    # Looping through the bots list and checking that the third value is inside the bots list
        if sys.argv[3].lower() in bots:
            nickname = sys.argv[3]                                                                                      # Taking the Third value as the nickname
        else:
            print("please  enter host to write to chatbots or enter bob, dora, alice or chuck to activate the chatbots")# Print statement
            exit()                                                                                                      # Exit program

elif len(sys.argv) < 2:                                                                                                 # Checking the if the user only enter the script name
    print("\n Please type -h , --help  for guide")                                                                      # Print statement guide
    exit()                                                                                                              # Exit program

elif sys.argv[1] == "-h" or sys.argv[1] == "--help":                                                                    # Checking if the first value inside the string is h or help
    print("""
        Enter the Correct Format IP, Port, Bot.  In which Bot is the Name of the Client.
        For Userinput Client Type 'Host' and for Activating Bots use the name Bob, Dora, Alice, Chuck.
    """)                                                                                                                # Print statement
    exit()                                                                                                              # Exit the program

else:                                                                                                                   # Print statement if the user enter client script only
    print("\n Please Enter Correct format: IP, Port, Bot  or press -h , --help for Guide")                              # Print statement
    exit()                                                                                                              # Exit program


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                                              # Starting a socekt instance for the client
client.connect((str(ip), int(port)))                                                                                    # Connect to the server with the local IP and port number that the user enter


# The four different chatbots that we are creating

# def alice chat bot take the word from the host gives it the ending and search it inside the god and the bad list.
# if it finds any match it should return a random string format from the statements below including
# else ot should return a standard text.
def alice(a):
    action = a + "ing"
    if action in bad_things:
        return random.choice([
            "Again with the {}! \U0001F641 \U0001F641".format(a + "ing"),
            "Are you serious? {} is the last thing we need".format(a + "ing"),
            "{} is a bad thing I'm not gonna do this!".format(a + "ing")])
    elif action in good_things:
        return random.choice([
            "Somebody suggested {}? Sure, I'm up for anything!".format(a + "ing"),
            "I think {} sounds great!".format(a + "ing"),
            "I'm Ready Let do {}\U0001F60D".format(a + "ing")])

    else:
        return "Alright! I'm Doing this."


# def bob chat bot take the word from the host gives it the ending and search it inside the god and the bad list.
# if it finds any match it should return a random string format from the statements below including
# else ot should return a standard text.
def bob(a):
    action = a + "ing"
    if action in bad_things:
        return random.choice([
            " Not sure about {}. Don't I get a choice? \n".format(a + "ing"),
            "{} seems negative. And I wanted more choices! That's it then? We're {}? Then let's get to "
            "it!\U0001F4A5 "
            "\U0001F4A5	".format(
                a + "ing", a + "ing"),
            " {} seems horrible. And I wanted more choices! Since nobody seems to have any better ideas I guess "
            "we're "
            "{}\U0001F937 \U0001F937".format(
                a + "ing", a + "ing")])
    elif action in good_things:
        return random.choice([
            "{} seems great. And complaining seems lame. Awesome! I've been longing for some {} all week!.".format(
                a + "ing", a + "ing"),
            "I think {} seems a good Idea".format(a + "ing")])

    else:
        return "its seems Good Idea to me"


# def dora chat bots take the word from the host gives it the ending and search it inside the god and the bad list.
# if it finds any match it should return a random string format from the statements below including
# else ot should return a standard text.
def dora(a, b=None):
    action = a + "ing"
    b = random.choice(alternatives)
    if action in bad_things:
        return random.choice([
            "Yea, {} is an option. Or we could do some {}.".format(a + "ing", b),
            "Oh, {}, excellent idea. Could also nag maybe?".format(a + "ing", b),

            "Right, {} is one alternative I guess. Or we could {}".format(a + "ing", b)])
    elif action in good_things:
        return "Meh. I did some {} last night. I'll complain maybe.".format(a + "ing")
    else:
        return "Yea, is a good option. Or we could do some {}".format(a + "ing", b)


# def chuck chat bot take the word from the host gives it the ending and search it inside the god and the bad list.
# if it finds any match it should return a random string format from the statements below including
# else ot should return a standard text.
def chuck(a):
    action = a + "ing"

    if action in bad_things:
        return random.choice(
            ["Awesome! I've been longing for some {} all week!".format(a + "ing"),
             "So {} it is then. I don't mind\U0001F913 \U0001F913".format(a + "ing"),
             "YESS! Time for {}".format(a + "ing")])

    elif action in good_things:
        return random.choice([
            "What? {} sucks. Not doing that.".format(a + "ing"),
            "Are you serious? {} is the last thing we need.".format(a + "ing")])

    return "I don't care!"


def tracker():                                                                                                          # Tracker function is in charge of the message that we receive from the server
    global flag                                                                                                         # because we are making change in variable that is declared out of function
    while True:                                                                                                         # The wile loop runs continously and checks the message.
        if True:
            message = client.recv(1024).decode("utf-8")                                                                 # Receive message from the
            if message == 'disconnect':                                                                                 # If the message that we receive equals disconnect
                print(f"Sorry {nickname} is already connected to the chatroom...")                                      # Print statement the chatbot is already connected
                flag = False                                                                                            # Change value to false host doesnt write to the chatbot
                return 0                                                                                                # end program

            if message == 'kick':                                                                                       # If message equals kick
                print(f"You have been kicked...")                                                                       # means that you have been kicked out
                flag = False                                                                                            # Change value to false host doesnt write to the chatbot
                return 0                                                                                                # End program
            if message == 'NICKNAME':                                                                                   # If message equals nickname
                client.send(nickname.encode("utf-8"))                                                                   # Send nickname
            elif nickname.lower() != "host":                                                                            # If the nickname is not the host
                if "host:" in message.lower():                                                                          # take the value from the host
                    message = message.split(":")                                                                        # split the message after colon
                    letter = message[1].split()                                                                         # split again after the second value
                    word = None
                    for word_in_letter in actions:                                                                      # loop thourgh the action list
                        if word_in_letter in letter:                                                                    # Comparing the letter with the message if there is ant match
                            word = word_in_letter                                                                       # The word get the value from the action list

                    if word is None:                                                                                    # If word is not insidet the action list
                        word = "Noth"                                                                                   # Use fixed word

                    if nickname.lower() == "bob":                                                                       # Her we are sending the sentence from the clients that are connected to the server
                        m = '{}: {}'.format(nickname, bob(word))
                        client.send(m.encode("utf-8"))
                    elif nickname.lower() == "alice":
                        m = '{}: {}'.format(nickname, alice(word))
                        client.send(m.encode("utf-8"))
                    elif nickname.lower() == "dora":
                        m = '{}: {}'.format(nickname, dora(word))
                        client.send(m.encode("utf-8"))
                    elif nickname.lower() == "chuck":
                        m = '{}: {}'.format(nickname, chuck(word))
                        client.send(m.encode("utf-8"))
                else:
                    print(message)

            else:
                print(message)


def host():                                                                                                             # host function is in  charge of the write ability for the host
    while True:

        message = '{}: {}'.format(nickname, input(''))                                                                  # Host send a message to the server
        client.send(message.encode("utf-8"))
        if flag == True:                                                                                                # If flag is true  print message
            print(f"{message}")
        else:
            break


tracker_thread = Thread(target=tracker).start()                                                                         # we are using two threads to start the tracker function and the host function for the host.

if nickname.lower() == "host":                                                                                          # Only host can write
    host_thread = Thread(target=host).start()
