#!/usr/bin/env python3
from datetime import datetime

class Request:

    def setHeaders(self):
        for header in self.headerline.split('\r\n'):
            print(header)
            name = header.split(':')[0]
            val = ':'.join(header.split(':')[1:])
            self.headers[name] = val 
    
    def getHeaders(self):
        return self.headers

    def setSomeInfosProps(self):
        self.setHeaders()
        self.method = self.requestmethod
        self.target = self.requesttarget
        self.version = self.requestprotocolversion
        self.httpVersion = self.requestprotocolversion

    def __init__(self,data):
        self.rawdata = data
        self.data = data.decode()
        self.requestline = self.data.split('\n')[0]
        self.requestmethod = self.requestline.split(' ')[0]
        self.requesttarget = self.requestline.split(' ')[1]
        self.requestprotocolversion = self.requestline.split(' ')[2]
        self.headerline = '\r\n'.join(self.data.split('\r\n\r\n')[0].split('\r\n')[1:])
        self.bodyline = self.data.split('\r\n\r\n')[1]
        self.headers = {}
        self.setSomeInfosProps()
        


class Response:

    def setHeaders(self):
        for header in self.headerline.split('\r\n'):
            name = header.split(':')[0]
            val = ':'.join(header.split(':')[1:])
            self.headers[name] = val 
    
    def setStatus(self,code,text):
        self.setStatusCode(if code code else self.statusCode)
        self.setStatusText(if text text else self.statusText)

    def setStatusLine(self):
        self.statusline = f"{self.requestprotocolversion} {self.statusCode} {self.statusText}\r\n"
    
    def setStatusCode(self,code):
        self.statusCode = code
        self.setStatusLine()
    
    def setStatusText(self,text):
        self.statusText = text
        self.setStatusLine()
    
    def send():
        data

    def getHeaders(self):
        return self.headers

    def __init__(self,data,socket):
        self.socket = socket
        self.rawdata = data
        self.data = data.decode()
        self.requestline = self.data.split('\n')[0]
        self.requestmethod = self.requestline.split(' ')[0]
        self.requesttarget = self.requestline.split(' ')[1]
        self.requestprotocolversion = self.requestline.split(' ')[2]
        self.headerline = '\r\n'.join(self.data.split('\r\n\r\n')[0].split('\r\n')[1:])
        self.bodyline = self.data.split('\r\n\r\n')[1]
        self.headers = {}
        self.setHeaders()


class Connection:


    def handleRequest(self,data):
        rawdata = data
        request = Request(data)
        response = Response(data,self.socket)
        


        return request,response


    def interact(self):
        while self.conti:
            data = self.socket.recv(65000)
            request,response = self.handleRequest(data)
            


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


