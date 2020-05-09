
#
# Ramkrushna Bolewar
#
# This script takes resolution as an input and take action based on system config
#

import sys

L = int(input())
N = int(input())

if (1 <= L <= 10000) and (1 <= N <= 1000):
    pass
else:
    sys.exit()

while N:
    print("Enter " + str(L) + " numbers :", end="")
    T = input()
    W = int(T.split(" ")[0])
    H = int(T.split(" ")[1])

    if (1 <= W <= 10000) and (1 <= H <= 10000):
        pass
    else:
        continue
    
    if W < L or H < L:
        print("UPLOAD ANOTHER")
    elif W == H:
        print("ACCEPTED")
    else:
        print("CROP IT")
    N -= 1
