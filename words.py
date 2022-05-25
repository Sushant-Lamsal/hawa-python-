n=int(input("enter a number n "))
m=int(input("enter a number m "))
if n>=0 and m>=0 :
    r=n+m
elif n>=0 and y<0 :
    r=n+m*m
elif n<0 and m>=0 :
    r=n*n+m
else :
    r=n*n+m*m
print(r)

