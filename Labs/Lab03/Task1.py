with open(r'text.txt') as fileobj:

    string = fileobj.read()
    print(f"Number of characters in file is: {len(string)}")
