#!/usr/bin/env python3
from sys import exit
from threading import Thread
from socket import socket,AF_INET,SOCK_STREAM
from .Connection import ConnectionManager




class Server:
    threads = []
    def setRefs(self,host,port):
        self.host = host
        self.port = port

    def listen(self):
        try:

            if hasattr(self,'host'):
                if hasattr(self,'port'):
                    if(self.port):
                        self.socket.bind((self.host,self.port))
                        self.socket.listen()
                        while True:
                            conn = self.socket.accept()
                            thread = Thread(target=self.connections.newConnection,args=(conn,))
                            thread.start()
                            self.threads.append(thread)
            else:
                print('server configuration is invalid...')
        except KeyboardInterrupt as e:
            print("Requested exit..shutting down server")
            print('killing server threads')
            for thread in self.threads:
                thread.join()
            self.socket.close()
            print('done')
            print('server socket destroyed')
            print('exiting..')
            exit(1)
            
    def __init__(self):
        self.socket = socket(AF_INET,SOCK_STREAM)
        self.connections = ConnectionManager(self)