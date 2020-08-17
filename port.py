import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Plz enter any IP u want to scan:")
port = int(input("Plz enter any Port u want to scan:"))

def portScanner(port):
    if s.connect_ex((host,port)):
        print("The port is closed");
    else:
        print("The port is open")

portScanner(port)