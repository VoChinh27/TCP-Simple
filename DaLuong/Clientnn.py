import socket

def start_client():
    # Tạo socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Kết nối đến server
    client_socket.connect(('localhost', 12345))

    try:
        while True:
            # Gửi tin nhắn đến server
            message = input("Nhập tin nhắn (hoặc 'exit' để thoát): ")
            if message.lower() == 'exit':
                break
            client_socket.send(message.encode())

            # Nhận phản hồi từ server
            response = client_socket.recv(1024).decode()
            print(f"Nhận từ server: {response}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()