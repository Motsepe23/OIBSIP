import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# Bind to the port
s.bind(('', port))

# Wait for client connection
s.listen(5)

while True:
    # Establish connection with client
    c, addr = s.accept()
    print('Got connection from', addr)

    # Send a thank you message to the client
    c.send('Thank you for connecting')

    # Close the connection
    c.close()


    import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# Connect to the server
s.connect(('localhost', port))

# Receive welcome message from server
print(s.recv(1024))

# Close the connection
s.close()


import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# Bind to the port
s.bind(('', port))

# Wait for client connection
s.listen(5)

# List to store connected clients
clients = []

while True:
    # Establish connection with client
    c, addr = s.accept()
    print('Got connection from', addr)

    # Add the client to the list
    clients.append(c)

    # Send a thank you message to the client
    c.send('Thank you for connecting'.encode())

    # Receive and broadcast messages from the client
    while True:
        try:
            message = c.recv(1024).decode()
            if not message:
                break
            print(message)
            for client in clients:
                client.send(message.encode())
        except:
            continue

    # Remove the disconnected client from the list
    clients.remove(c)

    # Close the connection
    c.close()
