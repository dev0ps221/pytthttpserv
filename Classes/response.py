#!/usr/bin/env python3

class Response:

    statusCode = ''
    statusText = ''
    statusline = ''
    bodyline   = '' 
    body       = ''

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
        self.body = f"{body}\r\n\r\n" if body else self.body 

    def send(self,data):
        self.setBody(data)
        response = self.getResponse()
        response = response if type(response) == bytes else response.encode()
        self.socket.send(response)

    def sendFile(self,filepath):
        responseText = ""
        if filepath:
            with open(filepath) as f:
                responseText = f.readlines()
                f.close()
            self.send(responseText)
        else:
            self.setStatus(500,"Internal Server Error") 
            self.send('')
    
    def getResponse(self):
        response = f"{self.statusline}{self.headerline}\r\n\r\n{self.bodyline}"

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
