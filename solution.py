from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    badRequestMessage = "400 Bad Request \r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((mailserver, port))
    serverSocket.listen()

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket, addr = serverSocket.accept()
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    try:
      mailFromCommand = 'MAIL FROM bob@nyu.edu\r\n'
      clientSocket.send(mailCommand.encode())
      recv2 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
      rcptToCommand = 'RCPT TO alice@nyu.edu\r\n'
      clientSocket.send(mailCommand.encode())
      recv3 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
      dataCommand = 'DATA\r\n'
      clientSocket.send(dataCommand.encode())
      recv4 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send message data.
    # Fill in start
      clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
      clientSocket.send(endmsg.encode())
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
      dataCommand = 'QUIT\r\n'
      clientSocket.send(dataCommand.encode())
      recv5 = clientSocket.recv(1024).decode()
    except IOError:
      connectionSocket.send(badRequestMessage.encode())
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')