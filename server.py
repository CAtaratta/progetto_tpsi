import socket
from bwt import calcola_bwt

HOST = "127.0.0.1"
PORT = 65432

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"\nConnnection made with {addr}")
                data = conn.recv(1024)
                if not data:
                    continue
                
                word = data.decode("utf-8")
                print(f"String received from the client: '{word}'")
                
                result = calcola_bwt(word)
                
                conn.sendall(result.encode("utf-8"))
                print(f"BWT results forwarded to the client: '{result}'")

if __name__ == "__main__":
    start_server()