#!/usr/bin/env python3
from datetime import datetime

class Connection:

    def __init__(self,data,conn_time):
        self.conn_time = conn_time
        self.rawdata = data
        self.socket = self.rawdata[0]
        self.address = self.rawdata[1]
        print('new connection with data')
        print(data)

class ConnectionManager:
    connections = []
    def newConnection(self,data):
       self.connections.append(Connection(data,datetime.now()))
    def __init__(self,socket):
        self.socket = socket


