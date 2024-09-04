try:    
    with open(r'text.txt') as fileobj:

        string = fileobj.read()
        count = 1
        print(f"Number of characters in file is: {len(string)}")
        print(f"Number of words in file is: {len(string.split())}")
except FileNotFoundError:
        print("File not Found")
except IOError:
    print("IOError Occured")
except Exception as error:
    print("Unexpected error")
