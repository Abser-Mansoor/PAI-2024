try:
    with open(r'text7.txt','r') as fileobj:
        sentence = fileobj.read()
        original = input("Enter character to be replaced: ")
        replacement = input("Enter replacement: ")
        new_sentence = sentence.replace(original,replacement)
    with open(r'text7.txt','w') as fileobj:
        fileobj.write(new_sentence)

except FileNotFoundError:
    print("File not Found")
except IOError:
    print("IOError occured")
except Exception as error:
    print("Unexpected Error Occured") 
