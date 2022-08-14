import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #This line will set up a TCP and UDP connection where data packets or datagrams will be streamed into the server
serverName = input("Enter domain or IP address: ")

rep = os.system('ping ' + serverName)  #This line creates a system command which can be executed in the command prompt

if rep == 0:
    print("The server is currently running in good state!")
else:
    print("Servers are vulnerable")

