dic={"l":[123,24,56] ,3.4:["uy","jh"]}
print("dic-   ",dic)
print()
print(dic.items())
print()
ff = {form: keys
				for keys, values in dic.items() 
				for form in values
      } 
print("ff-  ",ff)
print()


print(ff.keys())



for keys, values in dic.items():
    print("keys- ",keys)
    print("values- ",values)













