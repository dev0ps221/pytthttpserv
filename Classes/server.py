from thread import start_new_thread
from socket import socket,AF_INET,SOCK_STREAM
class Server:

    def setRefs(self,host,port):
        self.host = host
        self.port = port


    def __init__(self):
        self.socket = socket(AF_INET,SOCK_STREAM)