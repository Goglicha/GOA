#Remove exclamation marks

def remove_exclamation_marks(s):
    #your code here
    new_str = ""
    for i in s:
        if i != "!":
            new_str += i
    return new_str
            