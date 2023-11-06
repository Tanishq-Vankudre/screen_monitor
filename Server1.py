import tkinter as tk
import socket
import threading
from vidstream import StreamingServer

# Create a Tkinter window to display video streams
window = tk.Tk()
window.title("Screen Sharing Server")
window.geometry("800x600")

# Create a frame to hold video streams
frame = tk.Frame(window)
frame.pack()

# Initialize Vidstream server
server = StreamingServer("your_server_ip", 9999)

def start_server():
    server.start_server()

# Start the server in a separate thread
server_thread = threading.Thread(target=start_server)
server_thread.start()

# Function to receive and display video frames
def receive_and_display():
