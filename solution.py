from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    fromHeaderLine = "From: "
    toHeaderLine = "To: "

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()

    # Send HELO command and print server response.
    heloCommand = 'HELO someschool.edu\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFromCommand = 'MAIL FROM: <alice@someschool.edu>\r\n'
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptToCommand = 'RCPT TO: <bob@hamburger.edu>\r\n'
    clientSocket.send(rcptToCommand.encode())
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
    clientSocket.send((fromHeaderLine + "alice@someschool.edu \n" 
    + toHeaderLine + "bob@hamburger.edu" ).encode())
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
      
    clientSocket.close()      
    # Fill in end
    
def has_reply_from_server(response_status, expected_status):
    if response_status != expected_status:
        print('{} reply not received from server.'.format(expected_status))


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')