import shutil, os
os.mkdir("dest")            #creates folder named "dest"
file=open("file2.txt","w+") #creates "file2.txt"
file.close()

src='file2.txt'
d='dest'
shutil.move(src,d)          #moves "file2.txt" to "dest" folder
