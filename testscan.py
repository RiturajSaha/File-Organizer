import os
from pathlib import Path 


for i in os.scandir():     #scans the folder
    path=Path(i)
    print(i,end="->")
    print(path,end="->")    #read the name of scanned files present in the folder 
    print(path.suffix.lower())   
    print()
    
