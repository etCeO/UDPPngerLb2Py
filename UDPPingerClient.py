# UDPPingerClient.py
from socket import *
import time

# Server address and port
serverName = 'localhost'
serverPort = 12000

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set the timeout for receiving a response
clientSocket.settimeout(1)

# Define the ping message
message = b'ping'

for i in range(10):
    # For all 10 pings
    try:
        # try this
        # Record when the message is sent
        rtt_start = time.time()

        # Send the ping message to the server
        clientSocket.sendto(message, (serverName, serverPort))

        # Receive server response
        response, serverAddress = clientSocket.recvfrom(1024)

        # Record the time when received
        rtt_end = time.time()

        # Calculate round trip time (RTT) in seconds
        rtt = (rtt_end - rtt_start)

        # PING number
        print(f"Ping {i + 1}...")

        # Print the server response
        print(f"Received from server: {response}")

        # Print the round trip time
        print(f"RTT: {rtt} seconds")

    except timeout:
        # If there is a timeout
        # Print where it happened
        print(f"Ping {i+1} ... REquest TImed OuT")

# Close the socket
clientSocket.close()
