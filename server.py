#!/usr/bin/env python3
from Classes.Server import Server


server = Server()
server.setRefs('',8000)
server.listen()