import codecs
with codecs.open("text.txt","r+",encoding="utf-8") as file:

    # db=file.read()
    # file.seek(0)
    # db="Mercedes AMG\n"+db
    # file.write(db)
    db=file.readlines()
    db.insert(2,"Polo\n")
    file.seek(0)
    file.writelines(db)

