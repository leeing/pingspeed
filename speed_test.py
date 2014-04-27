#!/usr/bin/python

import threading
import subprocess

ping_times = 3

speed_test_result = []

class Server(object):
    def __init__(self,category,region,ip,usage):
        self.category = category
        self.region = region
        self.ip = ip
        self.usage = usage
    def to_string():
        print("server IP = " + self.ip)

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
        try:
            output = subprocess.check_output("ping -c " + str(ping_times) + " " + self.server.ip + " | grep round-trip",shell=True)
            result = output
            print(self.server.ip + "\t" + result.split("=")[1])
            speed_test_result.append(result)
        except:
            None

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

    for test_result in speed_test_result:
        print test_result
