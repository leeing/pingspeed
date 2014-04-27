#!/usr/bin/python

import threading
import subprocess

ping_times = 10

speed_test_result = []

class Server(object):
    def __init__(self,category,region,ip,usage):
        self.category = category
        self.region = region
        self.ip = ip
        self.usage = usage

    def to_string():
        print("server IP = " + self.ip)

class PingResult(object):
    def __init__(self,server,minimum,maximum,average):
        self.server = server
        self.minimum = minimum
        self.maximum = maximum
        self.average = average

    def __cmp__(self,other):
	return self.average - other.average

    def __str__(self):
	return self.server.ip + "\t" + str(self.average) + str(self.minimum) + "\t" + str(self.maximum) + "\t"\
	    + self.server.region + "\t" + self.server.usage + self.server.category + "\t" 

class PingThread(threading.Thread):
    def __init__(self,server):
        threading.Thread.__init__(self)
        self.server = server
   
    def run(self):
        try:
	    cmd = "ping -c " + str(ping_times) + " " + self.server.ip + " | grep round-trip"
            output = subprocess.check_output(cmd,shell=True)
            result = output.split("=")[1].split("/")
            #print(self.server.ip + "\t" + str(result[0:-1]))
	    pingResult = PingResult(self.server,float(result[0]),float(result[2]),float(result[1]))
            speed_test_result.append(pingResult)
        except Exception,ex:
            print ex

if __name__ == "__main__":
    servers = []
    thread_pool = []
    ip_list = file("result.txt","r")

    for line in ip_list.readlines():
        server_info = line.split(" ")
        if len(server_info) == 4:
            server = Server(server_info[0],server_info[1],server_info[2],server_info[3])
            servers.append(server)
 
    print("There are " + str(len(servers)) + " servers available")
    
    for server in servers:
        thread_pool.append(PingThread(server))

    for thread in thread_pool:
        thread.start()

    for thread in thread_pool:
        thread.join()

    speed_test_result.sort()
    for test_result in speed_test_result:
        print test_result
