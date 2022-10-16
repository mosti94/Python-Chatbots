# Python-chatbots

Individual portfolio assignment in the course "DATA2410 - Networking and cloud computing" at Oslo Metropolitan University.
Created a Python chat room with bots and a host that can talk to each other through a TCP socket

## Server 
The server is in charge of handling the requests from the clients and return the results to
other clients.
To run the Server: 
* The users download the program they can go to file explorer. There they must find the
  directory and enter the cmd command on their address bar.
* Enter the following to get guidance for the Server.py program

  ```
  server.py -h or server.py -–help
  ```
* For starting the Server enter:
  ```
  Server.py 1
  ```
  

After the server is established, the user can start connecting different clients to the server by entering te Ip address from the terminal and the port number.
Now the user has to open a new command line and write client.py

## Client
The client is the end device that connects to the server and communicates with each other. <br/>
chatboots name:bob, alice, dora, chuck and the host who can write to in the program
* Enter the following to get guidance for the Server.py program

  ```
  Client.py -h or Client.py -–help
  ```
* For starting the Server enter:
  ```
  CLient.py 1 ip addresse portnumber chatbot
  ```
  