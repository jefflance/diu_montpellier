def AlgoDetC(x,n):
    if n==1:
        return x
    else :
        z=AlgoDetC(x,n//2)
        if(n%2==0): 
            return z*z
        else:
            return x*z*z
    

print(AlgoDetC(2.5,8))