import socket

bind_ip = '0.0.0.0'
bind_port = 80

def listenTCP():
  try:
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(('', bind_port))
    tcp_server_socket.listen(128)

    return tcp_server_socket
  except:
    return 0

def listenRequired(server):
  client, client_addr = server.accept()

  print('Connected by ', client_addr)

  request = client.recv(1024)
  print(request)

  return client

def httpResponse(client):
  respond = 'GET HTTP/1.1\r\n'
  respond += 'Content-Type: text/html; charset=utf-8\r\n'
  respond += 'Server: TCP_HTTP/0.0.1\r\n'
  respond += '\r\n'
  respond += 'Hello Python'

  client.send(respond.encode('utf=8'))

  client.close()

def main():
  server = listenTCP()

  print("server runing in ", bind_port)

  while server != 0:
    client = listenRequired(server)

    httpResponse(client)
  else:
    print('Server close')

if __name__ == "__main__":
  main()
