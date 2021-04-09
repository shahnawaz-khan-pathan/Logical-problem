str = "Hello <<UserName>>, How are you?"
name= input("Enter your name here ")
if len(name) < 3:
    print('min three characters')
else:
    str = str.replace("<<UserName>>",name)
    print(str)