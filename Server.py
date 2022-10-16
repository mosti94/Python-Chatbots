import socket
import sys
from threading import Thread
import threading
import time

ip = ""
port = 0
lock = threading.Lock()
clients = []
nick_name = []
thread_store = []

# Im are using an if elif statement to check the command line arguments below and comparing the arguments and to get
# a port number.
if len(sys.argv) < 2:                                                                                                   # Check the length from the terminal input
    print("\n Please Enter Port  or type -h , --help  for guide")                                                       # Print help guide
    exit()                                                                                                              # Exit the program

elif str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":                                                          # Check the value from the second element inside the list
    print("\nEnter the Port Number (int value) ranging 0 to 65536")                                                     # Print guide enter port number
    exit()                                                                                                              # Exit program
elif len(sys.argv) == 2:                                                                                                # Correct formatting of the list check the length
    ip = socket.gethostbyname(socket.gethostname())                                                                     # Im are using the gethostbyname and gethostname function from the socket to get the ip address for the end device
    port = int(sys.argv[1])                                                                                             # Converting the second argument to integer.

# creates a socket with the IPv4 and bind the local Ip and the port number given to us from the command line
# prepare the socket to listen to other connections.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                                              # Creating a Socket instance with the using the address family of ipv4 and the TCP prootocol
server.bind((ip, port))                                                                                                 # Binding the server to the IP address from the end device and port number from the input
print("\nServer is established")                                                                                        # Print statement Server connection
print(f"\n IP: {ip}    |  Port {port}")                                                                                 # Print statement IP number and Port number
server.listen(5)                                                                                                        # Setting the server to listening mode, allowing other socket instance to connect the server.

def host_message(client, message):                                                                                      # Function sending message to all except itself
    for host in clients:                                                                                                # Looping through the client connection
        if host != client:                                                                                              # Checking that the bot isn't there
            host.send(message)                                                                                          # Sending the message


def broadcast(message):                                                                                                 # Broadcast function sending the message to all connected clients
    for client in clients:                                                                                              # Looping through connected clients
        client.send(message)                                                                                            # Sending message to all


def controller(client):                                                                                                 # controller function in charge of the handling client connection
    while True:                                                                                                         # Loop runs continuously
        try:                                                                                                            # Try to run the message from the client
            message = client.recv(1024)                                                                                 # Receive message from clients
            kick_message = message.decode("utf-8")                                                                      # Decode the message to text
            if kick_message == "":                                                                                      # If the person we kicked got an empty message we will en the thread
                return 0                                                                                                # Code run successfully
            kick_message = kick_message.split()                                                                         # Create a list from the client message
            increment = 0                                                                                               # Counter for the connected clients
            if "kick" in kick_message:                                                                                  # check if the message kick is inside the list
                for bot_name in nick_name:                                                                              # Looping through the nick name list
                    if bot_name == kick_message[2]:                                                                     # check if the bot is connected to the server
                        clients[increment].send("kick".encode("utf-8"))                                                 # Send message to the connected client message kick
                        del clients[increment]                                                                          # Deleting the socket instance from the client list
                        del nick_name[increment]                                                                        # Deleting the nickname from the list
                        thread_store[increment].join()                                                                  # Terminating the thread
                        message = f"{bot_name} has been kicked...".encode("utf-8")                                      # Print message
                        print(f"{bot_name} has been kicked from the chatroom...")                                       # Print message
                        client.send(message)
                    increment += 1
            lock.acquire()                                                                                              # Force the thread to run synchronously/lock
            host_message(client, message)                                                                               # Transmit to all except itself
            time.sleep(0.5)                                                                                             # Delay the thread for 0.5 seconds
            lock.release()                                                                                              # Release the thread from lock
        except:                                                                                                         # If any error happens with the client connection
            index = clients.index(client)                                                                               # Get the index from the client connection
            clients.remove(client)                                                                                      # remove it from the list
            client.close()                                                                                              # closes the socket connection
            client_name = nick_name[index]                                                                              # Finds the index from the nickname
            broadcast('{} has left the chatroom!\n'.format(client_name).encode("utf-8"))                                # Print message left the chatroom
            print('\n{} has left the chatroom!'.format(client_name))                                                    # Prints on the server as well
            nick_name.remove(client_name)                                                                               # Remove nickname from the list
            break


# The while loop is in  charge to accepts the bots connection and sending the data over to the list.
# it is as well in charge of transmitting with bots or the host is connecting to the socket.

while True:
    # bot is the socket object lets us communicate
    # address is the port and address.

    bot, address = server.accept()                                                                                      # Accepting the incoming client/sockets

    bot.send('NICKNAME'.encode("utf-8"))                                                                                # Send the message NICKNAME to the socket
    nickname = bot.recv(1024).decode("utf-8")                                                                           # Receiving the nickname from the socket instance
    if nickname in nick_name:                                                                                           # Checking if the nickname is in the nickname message
        bot.send('disconnect'.encode("utf-8"))                                                                          # Send message to the socket that client is connected/accepted
        bot.close()                                                                                                     # Close the connection

    else:
        print("\nConnected with {}".format(str(address)))                                                               # Print IP and Port message
        nick_name.append(nickname)                                                                                      # Append the nickname to the server
        clients.append(bot)                                                                                             # Append the request to the bot list
        print("\nNickname is {}".format(nickname))                                                                      # print
        broadcast("\n{} has connected!".format(nickname).encode("utf-8"))                                               # Transmit that a bot has connected to all clients
        thread = Thread(target=controller, args=(bot,))                                                                 # Start a new thread to check the new client connection
        thread.start()
        thread_store.append(thread)