#!/bin/python3

import socket

host='127.0.0.1'
port = 7777

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #AF INET for ipv4 conn and 
														#SOCK_STREAM is for  post he said


s.connect((host,port)