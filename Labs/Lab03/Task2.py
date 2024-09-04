try:    
    with open(r'text2.txt','r') as fileobj:
        string = fileobj.read()
        print(string)
        new_string = string.replace("Abser","Ali")
    with open(r'text2.txt','w') as fileobj:
        fileobj.write(new_string)
        print(new_string)
except FileNotFoundError:
    print("File not Found")
except IOError:
    print("IOError occured")
except Exception as error:
    print("Unexpected Error Occured") 
