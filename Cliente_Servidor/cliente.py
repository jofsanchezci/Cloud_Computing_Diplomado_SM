# cliente.py
import socket

def start_client():
    # Crear un socket de cliente (IPv4 y TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar al servidor en localhost y el puerto 12345
    client_socket.connect(('localhost', 12346))

    # Enviar un mensaje al servidor
    message = "Tercer Mensaje   !"
    client_socket.send(message.encode('utf-8'))

    # Recibir la respuesta del servidor
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Respuesta del servidor: {response}")

    # Cerrar la conexión
    client_socket.close()

if __name__ == "__main__":
    start_client()
