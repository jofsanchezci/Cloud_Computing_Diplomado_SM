
# Implementación del Patrón Cliente-Servidor en Python

Este proyecto es una implementación básica del **patrón Cliente-Servidor** en Python utilizando sockets. El servidor acepta conexiones de un cliente, recibe un mensaje y responde con una confirmación.

## Estructura del Proyecto:

- **servidor.py**: Implementa el servidor que espera y procesa conexiones de clientes.
- **cliente.py**: Implementa el cliente que envía un mensaje al servidor y recibe la respuesta.

## Archivos:

1. `servidor.py`: El servidor escucha en un puerto específico, recibe mensajes del cliente y responde con una confirmación.
2. `cliente.py`: El cliente se conecta al servidor, envía un mensaje y recibe la respuesta.

## Cómo ejecutar:

1. **Ejecutar primero el servidor**:
   Abre una terminal y ejecuta el servidor:
   ```bash
   python servidor.py
   ```

2. **Ejecutar el cliente**:
   Abre otra terminal y ejecuta el cliente:
   ```bash
   python cliente.py
   ```

### Ejemplo en código:

#### Servidor:

```python
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Servidor en espera de conexiones...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexión aceptada de {client_address}")
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Mensaje del cliente: {message}")
        response = "Mensaje recibido: " + message
        client_socket.send(response.encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    start_server()
```

#### Cliente:

```python
import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    message = "Hola, servidor!"
    client_socket.send(message.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Respuesta del servidor: {response}")
    client_socket.close()

if __name__ == "__main__":
    start_client()
```

## Descripción del funcionamiento:

- El **servidor** escucha en `localhost` en el puerto `12345` y espera conexiones. Al recibir una conexión, acepta el mensaje del cliente, lo imprime y envía una respuesta al cliente.
- El **cliente** se conecta al servidor, envía un mensaje y recibe la respuesta.

### Resultado esperado:

En la terminal del **servidor**:
```
Servidor en espera de conexiones...
Conexión aceptada de ('127.0.0.1', 54321)
Mensaje del cliente: Hola, servidor!
```

En la terminal del **cliente**:
```
Respuesta del servidor: Mensaje recibido: Hola, servidor!
```

Este proyecto ilustra cómo implementar el patrón Cliente-Servidor usando sockets en Python.
