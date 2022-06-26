#!/usr/bin/env python3
from datetime import datetime

class Connection:


    def handleRequest(self,data):
        rawdata = data
        data = data.decode()
        response = ''
        requestline = data.split('\n')[0]
        print(requestline)
        return response

    def interact(self):
        while True:
            data = self.socket.recv(65000)
            response = self.handleRequest(data)
            self.socket.send(response.encode())



    def __init__(self,data,conn_time):
        self.conn_time = conn_time
        self.rawdata = data
        self.socket = self.rawdata[0]
        self.address = self.rawdata[1]
        self.connecthost = self.address[0]
        self.connectport = self.address[1]
        print('new connection with data')
        print(self.connectport,self.connecthost,self.socket)
        self.interact()



class ConnectionManager:
    connections = []
    def newConnection(self,data):
        try:
            self.connections.append(Connection(data,datetime.now()))
        except KeyboardInterrupt as e:
            print("Requested exit..shutting down server")
            print('killing server threads')
            for thread in self.server.threads:
                thread.join()
            self.socket.close()
            self.socket.destroy()
            print('done')
            print('server socket destroyed')
            print('exiting..')
            exit(1)
            
    def __init__(self,server):
        self.server = server
        self.socket = self.server.socket


