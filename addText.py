db = open("hello.txt", "a")  #here we ask python to open the txt file
# the "a" here mean to append
newTextAdd = input("Please enter the new text")
# here the system will ask you to write the text that you would like to add
db.write("\n" + newTextAdd)
# here it will add the text at last line
db.close()
