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
    while True:
        try:
            client, addr = server.accept_client()
            label = tk.Label(frame, text=f"Client {addr[0]}")
            label.pack()
            client_video = client.start_stream()
            client_label = tk.Label(frame)
            client_label.pack()
            while True:
                frame = client_video.read()
                client_label.img = tk.PhotoImage(data=frame)
                client_label.config(image=client_label.img)
                window.update()
        except ConnectionError:
            continue

# Start receiving and displaying video frames in a separate thread
receive_thread = threading.Thread(target=receive_and_display)
receive_thread.start()

window.mainloop()
