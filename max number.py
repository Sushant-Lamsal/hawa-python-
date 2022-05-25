a=[999,3,45,36,1,99,525,10,101]
sorted_a=[]
while len(a)>0:
    maxno=0
    for i in a:
        if maxno<i:
            maxno=i
    sorted_a.append(maxno)
    a.remove(maxno)
print(sorted_a)    


a=[999,3,45,36,1,99,525,10,101]
sorted_a=[]
while len(a)<0:
    minno=o
    for i in a:
        if minno>i:
            minno=i
    sorted_a.append(minno)
    a.remove(minno)
print(sorted_a)

a=(1,2,3,4,5)
b=list(a)
b=tuple(b)
print(a)

a=(1,2,3,4,5)
a[0]=2
a.remove()
print(a(0))

a=[1,2,[5,6],8,9]
print(a[2])
print(a[2][0])

a=[1,2,[5,6,[8,7]],8,9]
print(a[2])
print(a[2][2])
 
a={1,2,3,4}
b={1,2,5,6}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a^b)
print((a.symmetric_difference(b)))


a=[1,2,3,4,5,5,3]
print(set(a))
print(list(set(a)))


a={2,3,4,5,5,3,8}
a.update((2,2,5))
a.discard(7)
a.remove(7)
a.pop(5)
a.clear()
print(a)
