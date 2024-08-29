def build_message(**info) : 
    parts = []
    iterator = 0;
    for key, message in info.items() :
        parts.append(str(key.capitalize()) + ": " + str(message))
    return ", ".join(parts)
    
message = build_message(name="Alice", age=30, city="New York")
print(message)
