#!/usr/bin/env python3
from os import getcwd,path
from datetime import datetime
from .request import Request
from .response import Response


here = getcwd()

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
            if(request.method == "GET"):
                targetpath = f"{self.manager.server.viewspath}{request.target if request.target != '/' else '/'}"
                print(f" tryna get {targetpath}")
                matchedIndex = []
                if(path.isdir(targetpath)):
                    print(targetpath,' is our targetpath deh')
                    print(self.manager.server.getDirContent(targetpath))
                    dircontent = self.manager.server.getDirContent(targetpath)
                    if len(dircontent):
                        for filename in dircontent:
                            print(filename)
                            for indexfile in self.manager.server.indexFiles:
                                print(indexfile)
                                matchedIndex.append(indexfile)
                    if len(matchedIndex):
                        response.setStatus(200,'OK')
                        response.setHeader('Content-Type',"text/html; charset=utf-8")
                        response.sendFile(f"{targetpath}/{matchedIndex[0]}")
                    else:
                        print(matchedIndex,' is matched')
                        response.setStatusCode(404)
                        response.setStatusText('Not Found')
                        response.send('Path not accessible\r\n')
                else:
                    if path.isfile(targetpath):
                        response.sendFile(targetpath)




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


