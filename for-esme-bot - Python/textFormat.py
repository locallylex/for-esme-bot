esmetxt=open("esme.txt","r")
esme=esmetxt.readlines()
esmetxt.close()

str=esme[0]
str=str.split('\t')
str=str[0]+"   "+str[1]

print(str) 

