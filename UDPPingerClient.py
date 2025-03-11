# UDPPingerClient.py
from socket import *
import time

# Server address and port
serverName = 'localhost'
serverPort = 12000

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Define the message to send
message = b'ping'

# Record the time when the message is sent
rtt_start = time.time()

# Send the ping message to the server
clientSocket.sendto(message, (serverName, serverPort))

# Receive the server's response
response, serverAddress = clientSocket.recvfrom(1024)

# Record the time when the response is received
rtt_end = time.time()

# Calculate the round trip time (RTT) in seconds
rtt = (rtt_end - rtt_start)

# Print the response from the server
print(f"Received from server: {response}")

# Print the round trip time
print(f"RTT: {rtt} seconds")

# Close the socket
clientSocket.close()
