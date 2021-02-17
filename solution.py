from socket import *
import sys


def webserver(port):

    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.bind(('localhost', port))
    serversocket.listen(5)
    served = False

    while not served:
        connectionsocket, addr = serversocket.accept()

        try:

            message = connectionsocket.recv(1024).decode()
            filename = message.split()[1]
            f = open(filename[1:], "r")
            outputdata = f.read()
            connectionsocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            for i in range(0, len(outputdata)):
                connectionsocket.send(outputdata[i].encode())
            connectionsocket.send("\r\n\r\n".encode())
            connectionsocket.close()

        except IOError:

            connectionsocket.send("HTTP/1.1 404 File Not Found\r\n\r\n".encode())
            connectionsocket.send("404 File Not Found".encode())
            connectionsocket.close()
        served = True

    serversocket.close()
    sys.exit()
   

if __name__ == "__main__":
    webserver(port=13331)
