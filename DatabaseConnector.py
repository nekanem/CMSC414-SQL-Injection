import mysql.connector
import socket



server_port = 12001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', server_port))
server.listen(5)
print("The server is ready")
for x in range(0, 1):
    # while 1:
    print("Waiting")
    connection_socket, addr = server.accept()
    print("accept")
    user_name = connection_socket.recv(2048).decode()
    pwd = connection_socket.recv(2048).decode()
    print("Username received: " + user_name)
    print("Password received: " + pwd)


    # Establish connection
    conn = mysql.connector.connect(user='root', password='*mySQLPa$$W0rd2o21*', host='127.0.0.1', database='hospital')

    # Creating a cursor object
    cursor = conn.cursor()

    # Executing a MySQL function using execute() method
    cursor.execute("SELECT DATABASE()")

    # Fetch a single row using fetchone() method
    data = cursor.fetchone()
    print("Connection established to :", data)

    # Check if the correct username & password were entered
    cursor.execute("select username from employees where username = " + "'" + user_name + "'" + ";")
    userName = cursor.fetchone()
    try:
        if userName[0] == user_name:
            cursor.execute("select pwd from employees where pwd = " + "'" + pwd + "'" + ";")
            password = cursor.fetchone()
            try:
                if password[0] == pwd:
                    cursor.execute("SHOW tables;")
                    result = cursor.fetchall()
                    print(result)
                    cursor.execute("select * FROM employees;")
                    testing = cursor.fetchone()
                    print(testing)

                else:
                    conn.close()
                    connection_socket.close()
            except TypeError:
                print("Incorrect password")
    except TypeError:
        print("Incorrect username")

        # Closes connection
        conn.close()
        connection_socket.close()
