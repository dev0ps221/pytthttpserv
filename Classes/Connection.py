

class Connection:

    def __init__(self,data,conn_time):
        self.conn_time = conn_time
        self.data = data
        print('new connection with data')
        print(data)

class ConnectionManager:
    connections = []
    def newCon(self,data):
       self.connections.append(new Connection(data),Date())
    def __init__(self,socket):
        self.socket = socket

