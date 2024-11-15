def subscriptn(A,B,C,X):
    if(A+B>=X) or (A+C>=X) or (B+C>=X):
        return "YES"
    else:
        return "NO"
A,B,C,X=map(int,input().split())
print(subscriptn(A,B,C,X))
