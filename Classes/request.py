#!/usr/bin/env python3

class Request:

    def setHeaders(self):
        for header in self.headerline.split('\r\n'):
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
        print(data,' is the request')
        self.data = data.decode()
        self.requestline = self.data.split('\n')[0]
        self.requestmethod = self.requestline.split(' ')[0]
        self.requesttarget = self.requestline.split(' ')[1] if len(self.requestline.split(' ')) > 1 else ""
        self.requestprotocolversion = self.requestline.split(' ')[1] if len(self.requestline.split(' ')) > 2 else ""
        self.headerline = '\r\n'.join(self.data.split('\r\n\r\n')[0].split('\r\n')[1:])
        self.bodyline = self.data.split('\r\n\r\n')[1] if len(self.data.split('\r\n\r\n')) > 1 else self.data.split('\r\n\r\n')[2] if len(self.data.split('\r\n\r\n')) > 2 else ''
        self.headers = {} 
        self.setSomeInfosProps()
        

