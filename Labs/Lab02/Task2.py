ef check(string: str) -> bool:
    return string[len(string)-1] in ['a','e','i','o','u']
    
print(check("fafafafafa"))
