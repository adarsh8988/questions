a=input("write a number")

user1 = open("a.txt","w")
user1.write(a)
print(user1)

user1.close()


b=input("write a number")

user2 = open("b.txt","w")
user2.write(b)
print(user2)

user2.close()



a = open("a.txt","r")
b = open("b.txt","r")
val = a.readline()
val1 = int(val)
val0 = b.readline()
val2 = int(val0)

res = val1 + val2

st = str(res)
# print(res)

c = open("c.txt","w")
c.write(st)
print(c)

c.close()



a.close()
b.close()

c = open("c.txt","r")
show = c.readline()
print(show)
c.close()


