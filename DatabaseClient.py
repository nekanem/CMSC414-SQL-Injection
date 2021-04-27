import socket

server_name = '127.0.0.1'
server_port = 12001
elementArray = ""
resultArray = ""
exitProgram = 'logout'
# create a socket object and connect
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_name, server_port))

# Ask user for their credentials and take in input form console
user_name = input('Username: ')
pwd = input('Password: ')

# send server credentials
client.send(user_name.encode())
client.send(pwd.encode())

openConnection = True
print('Enter quit to log out')
while openConnection:
    userQuery = input('Query: ')
    if userQuery == "quit":
        print("Logging out")
        openConnection = False
    else:
        client.send(userQuery.encode())
        result = client.recvfrom(4096)
        elementArray = result[0].decode().split('$')
        for x in range(1, len(elementArray)):
            if x in range(1, len(elementArray)):
                resultArray = elementArray[x].split('%')
                y = 1
                for element in resultArray:
                    if y in range(1, len(resultArray)-1):
                        print(element, end=', ')
                        y = y + 1
                    else:
                        print(element, end='')
            print('')

# end
client.close()
