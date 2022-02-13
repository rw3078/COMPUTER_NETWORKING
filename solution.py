# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  ipAddress = "127.0.0.1"
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind((ipAddress, port))
  #Fill in start
  serverSocket.listen()
  #Fill in end

  while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:

      try:
        bufSize = 4096
        print('Ready to receive message...')
        message = connectionSocket.recv(bufSize).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        print(outputdata)
        
        #Send one HTTP header line into socket.
        #Fill in start
        httpHeaderLine = "HTTP/1.1 200 OK"
        connectionSocket.send(httpHeaderLine.encode())
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start
        responseMessage = "404 Not Found \r\n"
        connectionSocket.send(responseMessage.encode())
        #Fill in end
        

        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)