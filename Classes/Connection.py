#!/usr/bin/env python3
from datetime import datetime

class Request:

    def __init__(self,data):
        self.rawdata = data
        self.data = data.decode()
        self.requestline = self.data.split('\n')[0]
        self.requestmethod = self.requestline.split(' ')[0]
        self.requesttarget = self.requestline.split(' ')[1]
        self.requestprotocolversion = self.requestline.split(' ')[2]

class Connection:


    def handleRequest(self,data):
        rawdata = data
        response = ''
        request = Request(data)
        
        print('METHOD | TARGET')
        print(request.requestmethod," | ",request.requesttarget)
        
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
            print('done')
            print('server socket destroyed')
            print('exiting..')
            exit(1)
            
    def __init__(self,server):
        self.server = server
        self.socket = self.server.socket


