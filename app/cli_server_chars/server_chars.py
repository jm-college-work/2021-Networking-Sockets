"""
Client-Server 1: Server
Internetworking Group Project (Group D)

Group Members:
    Matthew Ross    (K00252681)
    Marcello Nardi  (K00253266)
    Joe Morais      (K00254840)
"""

import socket
import sys
import re

def messagecheck(s):
    match = re.match('([A-Z]|[a-z]| )*', s)
    if(s == match.group()):
        return True
    else:
        return False

# Create the TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to port
port_number = 1080
server_name = 'localhost'
server_addr = (server_name, port_number)
print('Binding socket to server ' + server_name + ' on port ' + str(port_number))
s.bind(server_addr)

counter = 0
while True:
    counter += 1    

    # Listen for connections
    s.listen(1)

    # Wait for connection to be established
    print('Waiting for client to connect...')
    connection, client_aaddress = s.accept()

    # Receive data
    data = connection.recv(1024)
    print('RECEIVED:', data.decode('utf-8'))    

    # Check input   
    if(data.decode('utf-8') == 'exit'):        
        break   
    else:
        print('Sending response to client...')
        if(messagecheck(data.decode('utf-8'))):    
            connection.sendall(data)
        else:
            connection.sendall('False'.encode()) 

connection.close()
print('The connection was closed!') 