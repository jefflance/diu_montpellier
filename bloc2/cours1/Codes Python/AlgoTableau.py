def AlgoTableau(x,n):
    T=[]
    T.append(x)
    for i in range(1, n):
        T.append(T[i-1]*x)
    return T[n-1]

print(AlgoTableau(2.5,8))