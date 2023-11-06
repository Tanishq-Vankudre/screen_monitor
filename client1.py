import socket
from vidstream import ScreenShareClient

# Create a client for screen sharing
client = ScreenShareClient("your_server_ip", 9999)

client.start_stream()

while True:
    pass
