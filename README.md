# 📺 Screen Monitor Using VidStream

[![Python](https://img.shields.io/badge/python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Library](https://img.shields.io/badge/vidstream-required-brightgreen)]()
[![License](https://img.shields.io/badge/license-MIT-yellow)](./LICENSE)

A simple Python-based screen sharing system that allows real-time screen streaming between computers over a network. 🖥️➡️🖥️

## ✨ Features

- **📡 Real-time screen sharing** - Stream your screen to another computer
- **🌐 Network-based** - Works over local network
- **⚡ Simple setup** - Just configure IP and port, then run
- **🛑 Clean shutdown** - Type 'STOP' to terminate the session

## 📋 Requirements

- Python 3.x
- `vidstream` library

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/Tanishq-Vankudre/screen_monitor
cd screen_monitor
```

2. Install required dependencies:
```bash
pip install vidstream
```

## ⚙️ Configuration

Before running, you need to configure the IP addresses and ports in both files:

### In `receiver.py`:
```python
receiver = StreamingServer('your_server_ip', your_port)
```
Replace:
- `'your_server_ip'` with the receiver machine's IP address
- `your_port` with desired port number (e.g., `9999`)

### In `sender.py`:
```python
sender = ScreenShareClient('your_receiver_ip', your_port)
```
Replace:
- `'your_receiver_ip'` with the receiver machine's IP address
- `your_port` with the same port number used in receiver

## 🎯 Usage

1. **📥 Start the receiver** (on the machine that will receive the screen):
```bash
python receiver.py
```

2. **📤 Start the sender** (on the machine whose screen will be shared):
```bash
python sender.py
```

3. **🛑 To stop**: Press Enter and type `'STOP'` in either terminal

## 📁 Files

- `sender.py` - Screen sharing client (sends screen)
- `receiver.py` - Streaming server (receives screen)

## 🌐 Network Setup

- 🔗 Make sure both machines are on the same network
- 🔥 Ensure the specified port is not blocked by firewall

## 🔧 Troubleshooting

- **❌ Connection refused**: Check if receiver is running and IP/port are correct
- **📦 Import error**: Install vidstream with `pip install vidstream`
- **🔒 Permission denied**: Run with administrator privileges if needed
- **🔥 Firewall issues**: Allow Python through firewall or disable temporarily

## 👨‍💻 Contributors

- **Anish Ajit Jarag** - [GitHub](https://github.com/anish-jarag)
- **Tanishq Vishal Vankudre** - [GitHub](https://github.com/Tanishq-Vankudre)

## 📄 License

This project is open source and available under the MIT License.
