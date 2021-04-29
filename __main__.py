import HTTPServer

LISTEN_IP = '0.0.0.0'
LISTEN_PORT = 80

def main():
  server = HTTPServer.listenTCP(LISTEN_IP, LISTEN_PORT)

  while server != 0:
    client = HTTPServer.listenClient(server)

    HTTPServer.httpResponse(client)
  else:
    print('Server close')

if __name__ == "__main__":
  main()
