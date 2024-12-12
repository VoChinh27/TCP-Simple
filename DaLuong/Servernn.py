import socket
import threading

def handle_client(client_socket, addr):
    print(f"Kết nối từ {addr}")

    with client_socket:
        while True:
            # Nhận dữ liệu từ client
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Nhận từ client {addr}: {message}")

            # Phản hồi lại client
            response = f"Server đã nhận: {message}"
            client_socket.send(response.encode())

    print(f"Đóng kết nối với {addr}")

def start_server():
    # Tạo socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Gán địa chỉ và cổng
    server_socket.bind(('localhost', 12345))
    
    # Lắng nghe kết nối
    server_socket.listen(5)
    print("Server đang lắng nghe...")

    try:
        while True:
            # Chấp nhận kết nối từ client
            client_socket, addr = server_socket.accept()
            
            # Tạo một luồng mới để xử lý client
            client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_handler.start()

    except KeyboardInterrupt:
        print("\nServer đang dừng...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()