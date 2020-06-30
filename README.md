
# Append-TEXT-to-txt
here we gonna learn how to add some text to txt by using python
With file access mode ‘a’, open() function first checks if file exists or not. If the file doesn’t exist, then it creates an empty file and opens it. Whereas, if the file already exists then it opens it. In both cases, it returns a file object, and it has write cursor, which points to the end of the opened file. Now, if you write anything to the file using this file object, then it will be appended to the end.
We can open the file in append access mode i.e. ‘a’, using ‘with open’ statement too, and then we can append the text at the end of the file.
Append data to a file as a new line in Python
Solution for this is a little tricky here. let’s start with the basic approach and then we will discuss drawback in it and see how to improve over it,

Basic approach

Open the file in append mode (‘a’). Write cursor points to the end of file.
Append ‘\n’ at the end of the file using write() function
Append the given line to the file using write() function.
Close the file

another way File access mode ‘a+’, creates opens the file for both read and writing. Also if file it doesn’t exist, and then it creates the file too.
Initially, both read & write cursors will be pointing to the end of the file. We moved the read cursor to the top of file to check if the file is empty or not.
If the file is not empty, then append ‘\n’ at the end of the file first and then append the line.

the two example will find it in code right there.... 
for more information you can visit this page https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
all luck 
Abdullah
