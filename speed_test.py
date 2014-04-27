#!/usr/bin/python

import threading
import subprocess

ping_times = 3

class Server(object):
    def __init__(self,category,region,ip,usage):
        self.category = category
        self.region = region
        self.ip = ip
        self.usage = usage

class PingReault(object):
    def __init(self,server,minimum,maximum,average):
        self.server = server
        self.minimum = minimum
        self.maximum = maximum
        self.average = average

class PingThread(threading.Thread):
    def __init__(self,server):
        threading.Thread.__init__(self)
        self.server = server
   
    def run(self):
        output = subprocess.check_output("ping -c " + str(ping_times) + " " + server.ip + " | grep round-trip",shell=True)
        result = output.split("=").split("\/")
        print result

if __name__ == "__main__":
    servers = []
    ip_list = file("result.txt","r")

    for line in ip_list.readlines():
        server_info = line.split(" ")
        if len(server_info) == 4:
            server = Server(server_info[0],server_info[1],server_info[2],server_info[3])
            servers.append(server)
 
    print("There are " + str(len(servers)) + " servers available")
    
    for server in servers:
        pingThread = PingThread(server)
        pingThread.start()
