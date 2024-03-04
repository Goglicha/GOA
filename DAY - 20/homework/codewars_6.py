def abbrev_name(name): #it's function name is "name"
    first_name, last_name = name.split()   #i have splitted string "name" to receive two strings
    return f"{first_name[0].upper()}.{last_name[0].upper()}" 
    
    # An f-string, or formatted string literal, is a way to embed expressions inside string literals in Python. It was introduced in Python 3.6 and provides a concise and readable way to create strings by embedding expressions inside curly braces {}. The expressions are evaluated at runtime and formatted using the format() protocol.

    