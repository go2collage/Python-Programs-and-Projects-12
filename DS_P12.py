# Python Program / Project

def Magic(s,Size):
    for  i in range(0,size):
        for j in range( 0,size):
            s[i][j] = 0
    nr = 0  
    nc = Size // 2 
    s[nr][nc] = 1
    for  i in range(2,(Size*Size)+1):
        Row = nr
        Col = nc
        nr=nr-1
        if (nr < 0 ):
            nr = Size - 1
        nc=nc-1
        if ( nc < 0 ):
            nc = Size - 1
        if ( s[nr][nc] != 0):
            nr = Row+1
            nc =Col
        s[nr][nc] = i


# Driver Code
size = int(input("Enter the size of the matrix (No. of Rows): "))
row = 0
col = 0
sq = [[0 for col in range(size)] for row in range(size)]

if (size % 2 == 0):
    print("Error, Number of rows/cols should be odd.")
    print("Press any key to terminate.")
    exit()

else:
    Magic(sq, size)
    print("Magic Square is: ")
    for i in range(0, size):
        for j in range(0, size):
            print(sq[i][j], end=" ")
        print()
    sum = 0

    # Displaying the sum
    for j in range(0, size):
        sum = sum + sq[0][j]

    print("\n Sum = ", sum)