#!/usr/bin/env python3

from gzip import  compress
class Response:

    statusCode = ''
    statusText = ''
    statusline = ''
    headerline = ''
    bodyline   = '' 
    body       = ''

    def setHeaders(self):
        for header in self.headerline.split('\r\n'):
            name = header.split(':')[0]
            val = ':'.join(header.split(':')[1:])
            self.headers[name] = val 
        self.setHeaderLine()
    
    def setStatus(self,code,text):
        self.setStatusCode(code if code else self.statusCode)
        self.setStatusText(text if text else self.statusText)

    def setStatusLine(self):
        self.statusline = f"{self.requestprotocolversion} {self.statusCode} {self.statusText}\n"
    
    def setStatusCode(self,code):
        self.statusCode = code
        self.setStatusLine()
    
    def setStatusText(self,text):
        self.statusText = text
        self.setStatusLine()
    
    def setBody(self,body):
        self.body = f"{body}" if body else self.body 
        self.setBodyLine()

    def setBodyLine(self):
        self.bodyline = f"{self.body}"

    def setHeaderLine(self):
        self.headerline = '\n'.join(f"{name}:{self.headers[name]}" for name in self.headers)
        self.headerline+='\n\n'
    
    def setHeader(self,name,val):
        self.headers[name]=val
        self.setHeaderLine()

    def send(self,data):
        self.setBody(data)
        response = self.getResponse()
        print('this is our final response string ',response)
        response = response if type(response) == bytes else response.encode()
        self.socket.sendall(response)

    


    def sendFile(self,filepath):
        responseText = ""
        if filepath:
            with open(filepath,'rb') as f:
                responseText = f.read()
                f.close()
            # responseText = responseText if type(responseText) == bytes else responseText.encode()
            self.setHeader('Content-Length',len(responseText))
            self.setHeader('Content-Encoding','gzip')
            self.send(compress(responseText))
        else:
            self.setStatus(500,"Internal Server Error") 
            self.send('\r\n')
    
    def getResponse(self):
        return f"""{self.statusline}{self.headerline}{self.bodyline}""" 

    def getHeaders(self):
        return self.headers

    def __init__(self,data,socket):
        self.socket = socket
        self.rawdata = data
        self.data = data.decode()
        self.requestline = self.data.split('\r\n')[0]
        self.requestmethod = self.requestline.split(' ')[0]
        self.requesttarget = self.requestline.split(' ')[1] if len(self.requestline.split(' ')) > 1 else ''
        self.requestprotocolversion = self.requestline.split(' ')[2] if len(self.requestline.split(' ')) > 2 else ''
        self.reqheaderline = '\r\n'.join(self.data.split('\r\n\r\n')[0].split('\r\n')[1:])
        self.reqbodyline = self.data.split('\r\n\r\n')[1]
        self.headers = {}
        self.setHeaders()
