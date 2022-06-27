#!/usr/bin/env python3
from Classes.Server import Server


server = Server()
server.setRefs('',800)
server.listen()