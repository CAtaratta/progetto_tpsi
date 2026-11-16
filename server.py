import socket

HOST = "127.0.0.1"
PORT = 65432

def burrows_wheeler_transform(text: str) -> str:
    if not text.endswith("$"):
        text += "$"
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    sorted_rotations = sorted(rotations)
    return "".join(rotation[-1] for rotation in sorted_rotations)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server in ascolto su {HOST}:{PORT}...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connessione stabilita con {addr}")
                data = conn.recv(1024)
                if not data:
                    continue
                
                word = data.decode("utf-8")
                print(f"Stringa ricevuta: '{word}'")
                
                result = burrows_wheeler_transform(word)
                conn.sendall(result.encode("utf-8"))
                print(f"Risultato BWT inviato: '{result}'\n")

if __name__ == "__main__":
    start_server()