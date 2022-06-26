#!/usr/bin/env python3

class Response:

    def setHeaders(self):
        for header in self.headerline.split('\r\n'):
            name = header.split(':')[0]
            val = ':'.join(header.split(':')[1:])
            self.headers[name] = val 
    
    def setStatus(self,code,text):
        self.setStatusCode(code if code else self.statusCode)
        self.setStatusText(text if text else self.statusText)

    def setStatusLine(self):
        self.statusline = f"{self.requestprotocolversion} {self.statusCode} {self.statusText}\r\n"
    
    def setStatusCode(self,code):
        self.statusCode = code
        self.setStatusLine()
    
    def setStatusText(self,text):
        self.statusText = text
        self.setStatusLine()
    
    def setBody(self,body):
        self.body = body if type(body) == bytes else body.encode() 

    def send(self,data):
        self.setBody(body)
        
    def sendFile(self,filepath):
        responseText =""
    
    def getResponse(self):


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
        self.reqbodyline = self.data.split('\r\n\r\n')[1]
        self.headers = {}
        self.setHeaders()
