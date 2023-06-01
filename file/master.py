import socket
import pickle
import os
import random
import time

os.system('clear')

#! FUNCTIONS
def randomizeDivisible(M, n):
    # randomize values of all divisible by 10
    for row in range(n):
        for col in range(n):
            if (row % 10 == 0) and (col % 10 == 0):
                M[row][col] = float(random.randint(1,1000))

    return M

def createMatrix(n):
	M = [[0 for column in range(n)]for row in range(n)]
	randomizeDivisible(M, n)

	return M

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

def terrain_inter_col(M, n, col):
    for index in range(n):
        if M[index][col] == 0:
            x = index
            M[index][col] = round((y1 + ((x-x1)/(x2-x1)) * (y2-y1)), 2)

        else:
            x1 = index
            x2 = index + 10

            try:
                y1 = M[x1][col]
                y2 = M[x2][col]
            except:
                pass

    return M

def printMatrix(M, n):
    for i in range(n):
        for j in range(n):
            print(M[i][j], end="\t")

        print()

def main(n, client_num, host, port):

    server_socket = socket.socket()        
    print ("Socket successfully created")

    server_socket.bind((host, port))        
    print("socket binded to %s" %(port))

    # put the socket into listening mode
    print ("socket is listening")           
    server_socket.listen(5)    


    M = createMatrix(n)
    # printMatrix(M, n)
    col = 0
    while col < n:
        M = terrain_inter_col(M, n, col)
        col += 10

    num_per_group = n // client_num
    remainder = n % client_num
    elements = [num_per_group] * client_num

    # Distribute the remainder evenly
    for i in range(remainder):
        elements[i] += 1

    print(elements)

    # put into a list the starting indexes of the submatrices
    start_index = 0
    start_list = [0] # starting will always be 0th index
    for item in range(len(elements)):
        start_list.append(start_index + elements[item])
        start_index += elements[item]

    print(start_list)

    for index in range(len(start_list)-1):
        # print(start_list[index], start_list[index+1])
        temp = M[start_list[index]:start_list[index+1]]
        
        
        # for i in temp:
        #     print(i)
        # print()


    start_time = time.time()  


    counter = 0
    while counter < client_num:
        client_socket, addr = server_socket.accept()    
        print('Got connection from', addr)
        
        temp = M[start_list[counter]:start_list[counter+1]]
        data=pickle.dumps(temp)
        client_socket.sendall(len(data).to_bytes(4, 'big'))
        client_socket.sendall(data)

        ack = client_socket.recv(4096)
        print(ack.decode())


        data_size = int.from_bytes(client_socket.recv(4),'big')
        data = bytearray()
    


        
        client_socket.close()
        counter += 1

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print("Elapsed time:", elapsed_time, "seconds")
    

    print("You have reached the maximum number of clients.")