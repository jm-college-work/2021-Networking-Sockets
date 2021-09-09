"""
Client-Server 1: Client
Internetworking Group Project (Group D)

Group Members:
    Matthew Ross    (K00252681)
    Marcello Nardi  (K00253266)
    Joe Morais      (K00254840)
"""

import socket
import sys

def connect(cli_msg):
    # Create the TCP connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the port where server is listening
    port_number = 1080
    server_name = 'localhost'
    server_addr = (server_name, port_number)
    #print('Connecting to server ' + server_name + ' on port ' + str(port_number))
    s.connect(server_addr)

    # Send data to the server    
    #print('SENDING:', cli_msg)
    s.sendall(cli_msg.encode())

    # Wait for a response from the server
    data = s.recv(1024)
    #print('RECEIVED:', data.decode('utf-8'))

    # Print result
    if (data.decode('utf-8') == cli_msg):
        print('RESPONSE: ' + data.decode())        
    else:
        print('RESPONSE: The string contains non-alphabetic characters!')

    # Close socket connection
    print('Closing socket connection...')
    s.close()

while True:
    user_input = input('Enter a string to send to the server or type \'exit\' to quit.\n  > ')
    if(user_input == 'exit'):
        connect(user_input)
        break
    else:
        connect(user_input)
        


