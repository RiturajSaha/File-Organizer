# -*- coding: utf-8 -*-
"""
Created on Sat Apr 6 9:35:04 2020

@author: R2J
"""

import os 
import pathlib 
import shutil

fileFormats = {
	           "Web": [".html5", ".html", ".htm", ".xhtml"], 
	
               "Picture": [".jpeg", ".jpg", ".tiff", ".gif",
                           ".bmp", ".png", ".bpg", "svg",".heif", ".psd"], 
	
               "Video": [".avi", ".mkv",".flv", ".wmv",
                         ".mov", ".mp4", ".webm", ".vob", 
                         ".mng",".qt", ".mpg", ".mpeg", ".3gp"], 
	
              "Document": [".oxps", ".epub", ".pages", ".docx",
                           ".txt", ".pdf", ".doc", ".fdf",
                           ".ods",".odt", ".pwi", ".xsn",
                           ".xps", ".dotx", ".docm", ".dox",
                           ".rvg", ".rtf", ".rtfd", ".wpd", 
                           ".xls", ".xlsx", ".ppt","pptx"], 
	
               "Compressed": [".a", ".ar", ".cpio", ".iso", 
                              ".tar", ".gz", ".rz", ".7z",
                              ".dmg", ".rar", ".xar", ".zip"], 
	
               "Audio": [".aac", ".aa", ".aac", ".dvf",
                         ".m4a", ".m4b", ".m4p", ".mp3",
                         ".msv", "ogg", "oga", ".raw", 
                         ".vox", ".wav", ".wma"], 
              } 

fileTypes = list(fileFormats.keys())
fileFormats = list(fileFormats.values())

for file in os.scandir():
  
    fileName=pathlib.Path(file)
    fileFormatType=fileName.suffix.lower()
    
    src=str(fileName)
    dest="Other"
    
    if fileFormatType =="" :
        continue
    else:
      for formats in fileFormats:
          if fileFormatType in formats:
             if os.path.isdir(fileTypes[fileFormats.index(formats)])== False :
                  os.mkdir(fileTypes[fileFormats.index(formats)])
                  dest=fileTypes[fileFormats.index(formats)]
        
      else:
         if os.path.isdir("Other")== False :
              os.mkdir("Other")
              
    print(src," moved to ",dest," !")
    shutil.move(src,dest)

# In FilePrganizer.exe 
# FileOrganizer.py is changed to FilePrganizer.exe
# to make it work in exe file    
    
print("FileOrganizer.py removed...")    
os.remove("Other/FileOrganizer.py")    
input("\n PRESS ENTER TO EXIT")
