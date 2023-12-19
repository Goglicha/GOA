#Write a function that removes the spaces from the string, then return the resultant string.

def remove_spaces(string):
  new_string = ""
  for i in string:
    if i != " ":
      new_string += i
  return new_string
print(remove_spaces("a jhgy uhiu "))