import socket

HOST = '127.0.0.1'
PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server started on {HOST}:{PORT}, waiting for connection...")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")

        data_parts = []
        try:
            while True:
                packet = conn.recv(4096)
                if not packet:
                    break
                data_parts.append(packet)
        except ConnectionResetError:
            print("Connection was reset while receiving.")
           

        data = b"".join(data_parts)
        text = data.decode('utf-8', errors='ignore')

        print("\n--- Received Data ---")
        print(text)
        print("---------------------")

        try:
            conn.sendall(b"Server: Data received and printed successfully.")
        except ConnectionResetError:
            print("Connection was reset before sending response.")
