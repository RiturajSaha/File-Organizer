import os 
import pathlib 
import shutil

files = { 
	"Web": [".html5", ".html", ".htm", ".xhtml"], 
	"Pictures": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",".heif", ".psd"], 
	"Videos": [".avi", ".mkv",".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",".qt", ".mpg", ".mpeg", ".3gp"], 
	"Documents": [".oxps", ".epub", ".pages", ".docx", ".txt", ".pdf", ".doc", ".fdf", ".ods",".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt","pptx"], 
	"Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",".dmg", ".rar", ".xar", ".zip"], 
	"Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
	
} 

ff = {form: keys
				for keys, values in files.items() 
				for form in values
      }

for i in os.scandir():
  
    fname=pathlib.Path(i)
    form=fname.suffix.lower()
    src=str(fname)
    dest="Other"
    if form =="" :
        continue
    else:
      if form in ff:
         if os.path.isdir(ff[form])== False :
              os.mkdir(ff[form])
              dest=str(ff[form])
         

      else:
         if os.path.isdir("Other")== False :
              os.mkdir("Other")
              
    
    
    print(src," moved to ",dest," !")
    shutil.move(src,dest)
print("FO.py removed...")    
os.remove("Other/FO.py")    

    


