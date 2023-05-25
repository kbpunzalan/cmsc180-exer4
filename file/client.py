# Import socket module
import socket
import pickle     
import os

#! FUNCTIONS
def printMatrix(M, n):
    for i in range(n):
        for j in range(n):
            print(M[i][j], end="\t")

        print()

def terrain_inter_row(M, n, row):
    for index in range(n):
        if M[row][index] == 0:
            x = index # provide x based on the x-coordinate
            
            # apply the formula for FCC
            M[row][index] = round((y1 + ((x-x1)/(x2-x1)) * (y2-y1)), 2)
        else:
            # print(index, "index")
            x1 = index
            x2 = index + 10

            try:
                y1 = M[row][x1]
                y2 = M[row][x2]
            except:
                pass



os.system('clear')       
 
# Create a socket object
client_socket = socket.socket()        
 
# Define the port on which you want to connect
port = 5003
 
# connect to the server on local computer
client_socket.connect(('127.0.0.1', port))

data = []
while True:
    packet = client_socket.recv(4096)
    if not packet: break
    data.append(packet)

M = pickle.loads(b"".join(data))

message = "ack"
client_socket.send(message.encode())
print(message)

# fill remaining rows (inner box)
for row in range(1, len(M)):
    if row % 10 == 0:
        continue
    terrain_inter_row(M, len(M), row)


print()
for i in M:
    print(i)
# printMatrix(M, 11)
print()


# close the connection
client_socket.close()