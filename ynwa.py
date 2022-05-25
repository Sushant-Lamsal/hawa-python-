a="You will never walk alone"
print(a.split())
print(len(a))
print(a[12])
print(a.upper())
print(a.lower())
print(a.strip())
print("dhurba".capitalize())
print(a.replace("You","We"))
b=a.split("never")
print(b)
print("*".join(b))
print(a.isalpha())

b=lambda x,y:x+y
print(b(1,2))

a=[5,7,8,14,17]
print(list(map(lambda x:x/5,a)))
print(list(map(lambda x:x**2,a)))
print(list(map(lambda x:x**3,a)))
print(tuple(map(lambda x:x**2,a)))
print(set(map(lambda x:x**2,a)))
print(tuple(map(lambda x:x**2,a)))
print(list(filter(lambda x:x%7==0,a)))
print(list(filter(lambda x:x%2==1,a)))

##                        {{{DICTIONARY}}}
a={'Dhurba': 980767588,'Santosh':981612176,'Prashant':9846999769}
5##print(a)
print(a['Dhurba'])
a['Dhurba']="Mobile Chaina"
a['Sabin']=9806542271
print(sorted(a))
print(a)
del a['Dhurba']
a.clear()

for i in a :
    print(i)

for i in a.keys():
    print(i)

for i in a.items():
    print(i)

for i in a.values() :
    print(i)

a=[1,2,3,4,5,6,7,8,9,10]
print(a)
dict={'even':(list(filter(lambda x:x%2==1,a))),'odd':(list(filter(lambda x:x%2==0,a)))}
print(dict)


