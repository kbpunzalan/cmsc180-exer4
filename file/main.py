import master
import slave


import os
os.system('cls')

s = int(input("Enter s: "))
if __name__ == "__main__":
    with open("config.txt") as f:
        n = int(f.readline()) + 1
        t_minus_1 = int(f.readline())
        port = int(f.readline())
        host = f.readline()

    if s == 0:
        print("Sever")
        master.main(n, t_minus_1, host, port)
    else:
        print("Client")
        slave.main(n, host, port)