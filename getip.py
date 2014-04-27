#!/usr/bin/python

import re

ip_file = open("filter.txt",'r')

i = 0
for line in ip_file.readlines():
    i = i + 1
    if i%5 == 0:
        print("\n")
    else:
        print line
    
