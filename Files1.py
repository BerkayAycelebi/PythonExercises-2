import codecs
with codecs.open("text.txt","a",encoding="utf-8") as file:
    #a=file.read()
    #a=file.readline()
    #b=file.readline()
    c=file.readlines()
    #print(a,b)
    counter=1
    for i in c:
        print(counter,":",i)
        counter+=1


