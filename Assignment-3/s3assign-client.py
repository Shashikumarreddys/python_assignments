import socket
import os

HOST = '127.0.0.1'
PORT = 5050

file_path = input("Enter full file path to send: ").strip()

if not os.path.exists(file_path):
    print("File not found.")
    exit()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to server {HOST}:{PORT}")

    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            s.sendall(chunk)

    s.shutdown(socket.SHUT_WR)

    resp_parts = []
    try:
        while True:
            part = s.recv(4096)
            if not part:
                break
            resp_parts.append(part)
    except ConnectionResetError:
        print("Connection was reset while waiting for server response.")

    if resp_parts:
        print("Server Response:", b"".join(resp_parts).decode('utf-8', errors='ignore'))
    else:
        print("No response from server.")
