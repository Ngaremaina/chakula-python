# function to display output
#print('hello world') #string
#print (2 + 3)#numbers
#print(True, False)#boolean

#Variables
x = 2.26
y = True
print(type(x))
print(type(y))

#Data types
#string, int, float, double, bool
string = "hello"
int = 2
float = 3.14
double = 3.14
bool = True
# dict
# print(dict)
# print(string, int, float, double, bool, dict)

#Loops
# while loop and for loop
x = 1
# for x in range(10):# 0 - 9
#     print(x)

while x < 3:
    # print(x)
    x = x + 1

#if statements
a = 56
b = 33
print(a * b)
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
   print("Default")

#Function
def Sum():
    print(7 + 9)

Sum()

#Comment => #

#Arrays
i = [10, 5 , 8 , 9 , 85]
# print(i)
# print(len(i))
# for j in i:
#    print(j * 2)
# j = 0
# while j < len(i):
   
#    j = j + 1

#classes
class Dog:
   global sound
   sound = "bark"
   def bark():
      print(sound)

Dog.bark()
# print(Dog.sound)