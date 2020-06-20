import os
from pathlib import Path 


for i in os.scandir():     
    path=Path(i)
    print(i,end="->")
    print(path,end="->")     
    print(path.suffix.lower())   
    print()
    
