fil=open('file.txt',"w")
fil.write('this is a car')
fil.close()
fil=open('file.txt',"a")
fil.readline()
print(fil)