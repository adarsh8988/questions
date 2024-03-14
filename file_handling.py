x=input('Enter first number')
user1=open('x.txt',"w")
user1.write(x)
print(user1)

y=input('Enter second number')
user2=open('y.txt',"w")
user2.write(y)
print(user2)

user1.close()
user2.close()

x=open('x.txt',"r")
y=open('y.txt',"r")
val=x.readline()
val1=int(val)
val2=y.readline()
val3=int(val2)
res=val1+val3
st=str(res)
# print(res)
x.close()
y.close()

z=open('z.txt',"w")
z.write(st)
print(z)
z=open('z.txt',"r")
show=z.readline()
print(show)
z.close()


