#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

#host = input("Please enter the IP you want to scan: ")
host = "192.168.31.113"
port = int(input("Please enter the port you want to scan: "))
#port =


def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)