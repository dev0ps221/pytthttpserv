#!/usr/bin/env python3
from time import sleep
from os import system
from sys import exit
from threading import Thread
from socket import socket,AF_INET,SOCK_STREAM
from .Connection import ConnectionManager


def cls():
    system("clear")


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
                        self.listening = True
                        while self.quit == False:
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
            self.quit = True
            print('done')
            print('server socket destroyed')
            print('exiting..')
            exit(1)

    def recap(self):
        while self.quit == False:
            cls()
            if(self.listening):
                print(f"-------------------------------------------------")
                print(f"Le server http est actif sur le port | {self.port}")

                print(f"Nombre de connections : {self.connections.getConnections()}")
                print(f"-------------------------------------------------")
            else:
                print("Le server n'est pas actif..")
                print("Voici les parametres actuellement définis:")

                if(hasattr(self,'port')):
                    print(f"port : {self.port}")

                if(hasattr(self,'host')):
                    print(f"hostaddress : {self.host}")
            
            sleep(2)                   



    def __init__(self):
        self.quit = False
        self.listening = False
        self.socket = socket(AF_INET,SOCK_STREAM)
        self.connections = ConnectionManager(self)
        self.recapThread = Thread(target=self.recap,args=())
        # self.recapThread.start()
