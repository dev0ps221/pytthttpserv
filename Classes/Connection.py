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
        self.headerline = '\n'.join(self.data.split('\r\n\r\n')[1].split('\n')[1:])
        print(self.headerline)
        print(' is headerline ')

class Connection:


    def handleRequest(self,data):
        rawdata = data
        request = Request(data)
        
        statusline = "HTTP1.1 200 ok\r\n"
        headerline = "\r\n\r\n"
        bodyline = " okay ;) \r\n\n"
        response = statusline 
        response+=headerline 
        response+=bodyline
        
        return response

    def interact(self):
        while self.conti:
            data = self.socket.recv(65000)
            response = self.handleRequest(data)
            self.socket.send(response.encode())



    def __init__(self,man,data,conn_time):
        self.conti = 1
        self.manager = man
        self.conn_time = conn_time
        self.rawdata = data
        self.socket = self.rawdata[0]
        self.address = self.rawdata[1]
        self.connecthost = self.address[0]
        self.connectport = self.address[1]
        self.interact()



class ConnectionManager:
    connections = []
    def getConnections(self):
        return self.connections
    def newConnection(self,data):
        try:
            self.connections.append(Connection(self,data,datetime.now()))
        except KeyboardInterrupt as e:
            print("Requested exit..shutting down server")
            print('killing server threads')
            for thread in self.server.threads:
                thread.join()
            for connection in self.connections:
                connection.conti = 0
            self.socket.close()
            print('done')
            print('server socket destroyed')
            print('exiting..')
            exit(1)
            
    def __init__(self,server):
        self.server = server
        self.socket = self.server.socket


