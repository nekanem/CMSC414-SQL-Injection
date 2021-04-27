import mysql.connector
import socket

server_port = 12001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', server_port))
server.listen(5)
print("The server is ready")
print("Waiting")
connection_socket, addr = server.accept()
print("accept")
user_name = connection_socket.recv(2048).decode()
pwd = connection_socket.recv(2048).decode()
print("Username received: " + user_name)
print("Password received: " + pwd)
closeConnection = 'logout;'
resultString = ""
openConnection = True

# Establish connection
conn = mysql.connector.connect(user='root', password='*mySQLPa$$W0rd2o21*', host='127.0.0.1', database='hospital')

# Creating a cursor object
cursor = conn.cursor(buffered=True)


# Executing a MySQL function using execute() method
cursor.execute("SELECT DATABASE()")

# Fetch a single row using fetchone() method
data = cursor.fetchone()
print("Connection established to :", data)

# Check if the correct username & password were entered, if not close connection
cursor.execute("select username from employees where username = " + "'" + user_name + "'" + ";")
userName = cursor.fetchone()
try:
    if userName[0] == user_name:
        cursor.execute("select pwd from employees where pwd = " + "'" + pwd + "'" + ";")
        password = cursor.fetchone()
        try:
            if password[0] == pwd:
                while openConnection:

                    # This is where the user will be able to execute commands
                    userQuery = connection_socket.recv(4096).decode() + ";"
                    if userQuery == ";":
                        conn.close()
                        connection_socket.close()
                        openConnection = False
                    else:
                        cursor.execute(userQuery)
                        result = cursor.fetchall()
                        for element in result:
                            resultString = resultString + "$"
                            for userData in element:
                                resultString = resultString + str(userData) + "%"
                        # Send results of query back to client program
                        connection_socket.send(resultString.encode())
            else:
                conn.close()
                connection_socket.close()
        except TypeError:
            print("Incorrect password")
    else:
        conn.close()
        connection_socket.close()
except TypeError:
    print("Incorrect username")

# Closes connection
# conn.close()
# connection_socket.close()
