# n = int(input("Enter n: "))
s = int(input("Enter s: "))
# p = int(input("Enter n: "))
import master
import slave

with open("config.txt") as f:
    n = int(f.readline())
    t_minus_1 = int(f.readline())
    port = int(f.readline())
    host = f.readline()


if s == 0:
    print("Sever")
    master.main(n, t_minus_1, host, port)
else:
    print("Client")
    slave.main(n, host, port)