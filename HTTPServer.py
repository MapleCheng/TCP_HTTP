import socket

def listenTCP(IP, PORT):
  try:
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind((IP, PORT))
    tcp_server_socket.listen(128)

    print("The server is running on PORT", PORT)

    return tcp_server_socket
  except:
    return 0

def listenClient(server):
  client, client_addr = server.accept()

  print('Connected by ', client_addr)

  request = client.recv(1024)

  return client

def httpResponse(client):
  respond = 'GET HTTP/1.1 200\r\n'
  respond += 'Content-Type: text/html; charset=utf-8\r\n'
  respond += 'Server: TCP_HTTP/0.0.1\r\n'
  respond += '\r\n'
  respond += 'Hello Python'

  client.send(respond.encode('utf=8'))

  client.close()
