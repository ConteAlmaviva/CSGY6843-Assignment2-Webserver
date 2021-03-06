#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):

   serverSocket = socket(AF_INET, SOCK_STREAM)
   #Prepare a server socket
   #Fill in start
   serverSocket.bind(('localhost', port))
   serverSocket.listen(5)
   #Fill in end

   while True:
     #Establish the connection
     connectionSocket, addr = serverSocket.accept()
     try:
       message = connectionSocket.recv(1024).decode()
       filename = message.split()[1]
       f = open(filename[1:], "r")
       outputdata = f.read()
       #Send one HTTP header line into socket
       #Fill in start
       connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
       #Fill in end
       #Send the content of the requested file to the client
       for i in range(0, len(outputdata)):
         connectionSocket.send(outputdata[i].encode())
       connectionSocket.send("\r\n\r\n".encode())
       connectionSocket.close()


     except IOError:
       #Send response message for file not found (404)
       #Fill in start
       connectionSocket.send("HTTP/1.1 404 File Not Found\r\n\r\n".encode())
       #Fill in end
       connectionSocket.send("404 File Not Found".encode())
       #Close client socket
       #Fill in start
       connectionSocket.close()
       #Fill in end

   serverSocket.close()
   sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":

   webServer(13331)

