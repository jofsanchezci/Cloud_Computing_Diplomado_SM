# servidor.py
import socket

def start_server():
    # Crear un socket de servidor (IPv4 y TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincular el socket a la dirección y puerto
    server_socket.bind(('localhost', 12345))

    # Escuchar conexiones entrantes (máximo 5 conexiones en cola)
    server_socket.listen(5)
    print("Servidor en espera de conexiones...")

    while True:
        # Aceptar una conexión
        client_socket, client_address = server_socket.accept()
        print(f"Conexión aceptada de {client_address}")

        # Recibir el mensaje del cliente
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Mensaje del cliente: {message}")

        # Enviar una respuesta al cliente
        response = "Mensaje recibido: " + message
        client_socket.send(response.encode('utf-8'))

        # Cerrar la conexión con el cliente
        client_socket.close()

if __name__ == "__main__":
    start_server()
