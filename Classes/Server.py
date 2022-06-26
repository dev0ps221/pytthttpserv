#!/usr/bin/env python3
from threading import Thread
from socket import socket,AF_INET,SOCK_STREAM
from .Connection import ConnectionManager



class Server:

    def setRefs(self,host,port):
        self.host = host
        self.port = port

    def listen(self):
        if hasattr(self,'host'):
            if hasattr(self,'port'):
                if(self.port):
                    self.socket.bind((self.host,self.port))
                    self.socket.listen()
                    while True:
                        conn = self.socket.accept()
                        thread = Thread(target=self.connections.newConnection,args=(conn,))
                        thread.start()
        else:
            print('server configuration is invalid...')
    def __init__(self):
        self.socket = socket(AF_INET,SOCK_STREAM)
        self.connections = ConnectionManager(self.socket)