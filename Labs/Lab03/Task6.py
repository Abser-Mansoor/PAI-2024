def insert_question(string):

    with open(r'text6.txt','r+') as fileobj:
        if string[-1] == '?':
            fileobj.write(string)
            print('Written')
            return
        
try:
    insert_question("Ist Fasih soldaten?")
except FileNotFoundError:
        print("File not Found")
except IOError:
    print("IOError Occured")
except Exception as error:
    print("Unexpected error")
