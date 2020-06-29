def AlgoSansTableau(x,n):
    y=x
    for i in range(1, n):
        y=y*x
    return y

print(AlgoSansTableau(2.5,8))