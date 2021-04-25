import socket

server_name = '127.0.0.1'
server_port = 12001

# create a socket object and connect
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_name, server_port))

#Ask user for their credentials and take in input form console
print("Username: ")
user_name = input()
print("Password: ")
pwd = input()

#send server credentials
client.send(user_name.encode())
client.send(pwd.encode())

#end
client.close()
