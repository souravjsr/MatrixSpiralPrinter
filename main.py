from numpy import reshape

def printer(x,n):
    z=x+1
    for i in range(x,n-z):
        print matrix[x][i],
    for j in range(x,n-z):
        print matrix[j][n-z],
    for k in range(n-z,x,-1):
        print matrix[n-z][k],
    for l in range(n-z,x,-1):
        print matrix[l][x],
    #print "\n"
        
if __name__=="__main__":
    val=input("Give the matrix size -- ") 
    matrix = reshape(range(val**2),(val,val))
    print matrix
    mid=val/2
    #print mid
    if (val%2 !=0):
        mid+=1
    for i in range(mid): 
        printer(i,val)
    if (val%2 !=0):
        print matrix[val/2][val/2]