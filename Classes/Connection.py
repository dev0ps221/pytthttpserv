#!/usr/bin/env python3
from datetime import datetime

class Connection:


    def handleRequest(self,data):
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
       self.connections.append(Connection(data,datetime.now()))
    def __init__(self,socket):
        self.socket = socket


