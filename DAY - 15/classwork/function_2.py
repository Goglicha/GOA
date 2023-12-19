# def hello (name, age):
#   print("hello my name is: " + name + " i am: " + age +" years old")
# hello("nini", "25")
# hello("Ani", "26")

def str(string):
  new_str = ""
  x = len(string)

  while x > 0:
    new_str += string[x - 1]
    x -= 1
  return new_str

  
str("abcdefg")










