#!/usr/bin/env python3
from thread import start_new_thread
from socket import socket,AF_INET,SOCK_STREAM
from .Connection import ConnectionManager
class Server:

    def setRefs(self,host,port):
        self.host = host
        self.port = port

    def listen(self):
        if(hasattr(self,'host') && hasattr(self,'port')):
            if(self.port):
                self.socket.bind((self.host,self.port))
                self.listen()
                while True:
                    conn = self.accept()
                    start_new_thread(this.connections.newConnection,(data,))
        else:
            print('server configuration is invalid...')
    def __init__(self):
        self.socket = socket(AF_INET,SOCK_STREAM)
        self.connections = ConnectionManager(self.socket)