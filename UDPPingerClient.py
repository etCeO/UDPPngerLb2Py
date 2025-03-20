# UDPPingerClient.py
import time
import random
from socket import *

# Define server address and port
serverName = '127.0.0.1'  # localhost
serverPort = 12000

# Create UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set timeout to 1 second
clientSocket.settimeout(1)

# Send 10 ping messages
for sequence_number in range(1, 11):
    # Get the current time
    sendTime = time.time()
    
    # Format message to follow ASCII representation
    message = "Ping " + str(sequence_number) + " " + str(sendTime)
    
    try:
        # Send message to server
        clientSocket.sendto(message.encode('ascii'), (serverName, serverPort))
        
        # Wait for response from server
        response, _ = clientSocket.recvfrom(1024)
        receiveTime = time.time()
        RTT = receiveTime - sendTime
        
        # Print response and RTT
        print(response.decode('ascii'), "RTT=", round(RTT, 6), "sec")
    except timeout:
        # Handle timeout if no response received
        print("Request timed out")

# Close the socket
clientSocket.close()