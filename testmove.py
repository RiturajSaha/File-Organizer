import shutil, os

os.mkdir("dest")            
file=open("file2.txt","w+") 
file.close()

src='file2.txt'
d='dest'
shutil.move(src,d)         
