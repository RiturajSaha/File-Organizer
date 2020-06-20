files ={"java":100, "python":112, "c":11}} 

key_list = list(files.keys())
val_list = list(files.values())

print(files.values())
for ele in val_list:
  if '.dvf' in ele:
      print(key_list[val_list.index(ele)])
