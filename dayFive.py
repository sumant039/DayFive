#!/usr/bin/python
import re
#Decorators
#Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class

#A Fucntion can return another function

def is_called():
    def is_returned():
        print("Hello")
       
    return is_returned

new = is_called()


#Outputs "Hello"
new()

#def test()"
#    a
#Def te
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")


#ordinary()

pretty = make_pretty(ordinary)
pretty()



#example 2

def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner
#decorating divide function
@smart_divide
def divide(a,b):
    return a/b

val=divide(2.0,5.0)

print("value of divide is",val)

val1=divide(2,0)

print("val of divide by 0 is",val1)




#Chaining Decorators

def star(func):
    def inner(*args, **kwargs):
        print(" outer star") 
        print("*" * 30) #1
        func(*args, **kwargs)
        print("dollar")
        print("$" * 30)
    return inner

def percent(func):               
    def inner(*args, **kwargs):
        print("percent")#2
        print("%" * 30)
        func(*args, **kwargs)
        print("rate")
        print("@" * 30)
    return inner

#Defining 2 decorators
@star
@percent
def printer(msg):
    print("In Printer")
    print(msg)#3
printer("Hello")




#outer star
#******************************
#percent
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#In Printer
#Hello
#rate
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#dollar
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#iterators 

#generators Yield
#def 
#
listEven=[1,2,3,4,5,6,7,8,9,10]
def evenNums(listEven):
    for num in listEven:
        if num%2==0:
            yield num
#we cant itertate on singl element,we should have multiple elements
#if we will use return insted of  yield we will get only one value because control will come out of the function
for eN in evenNums(listEven):
    print("eN is",eN)



import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(30, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

print("Elements in lottery")
Str=list(lottery())
print((Str[0]))
Str1=list(lottery())
print((Str1[1]))
#for random_number in lottery():
#       print("And the next number is... %d!" %(random_number))



#
# fill in this function
def fib():
    yield 2
    pass #this is a null statement which does nothing when executed, useful as a placeholder.

# testing code
import types


if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
for fi in fib():
	print("Hello Fib")

def getNum(a):
	return a+1

val=getNum(2)
print val
#getNum is not a generator hence we cant iterate over it.
#for ge in getNum():
#	print("Hello")

if type(getNum(3)) == types.GeneratorType:
    print("Good, The fib function is a generator.")
else:
    print ("Not a generator function")

#re is a library in python for regular expression ,it has few functions like match ,find ,search etc   



pattern = r"Cool"
sequence = "Cookie"

#use match wherever we use conditional statements

if re.match(pattern, sequence):
  print("Match!")
else: print("Not a match!")



print (re.match(pattern, sequence))
#Cookie match upto pattern defined 
#regular expression has wild cards * . + \w \s a* ajay aman  , a. ae af ag + a+ a ak 
print(re.search(r'Co\wk\w', 'Cookie').group())

#\w - Lowercase w. Matches any single letter, digit or underscore.

print(re.search(r'Co.k.e', 'Cookie').group())

#\w - Lowercase w. Matches any single letter, digit or underscore.

re.search(r'Co\wk\we', 'Cookie').group()

#\W - Uppercase w. Matches any character not part of \w (lowercase w). @ is not a aprt of \w hence it is a part of \W

print(re.search(r'C\Wke', 'C@ke').group())

#\s - Lowercase s. Matches a single whitespace character like: space, newline, tab, return.

print(re.search(r'Eat\scake', 'Eat cake').group())

#\S - Uppercase s. Matches any character not part of \s (lowercase s).


re.search(r'Cook\Se', 'Cookie').group()
#\t - Lowercase t. Matches tab.

#re.search(r'Eat\tcake', 'Eat    cake').group()

#'Eat\tcake'

re.search(r'c\d\dkie', 'c00kie').group()

#\n - Lowercase n. Matches newline.

#\r - Lowercase r. Matches return.

#\d - Lowercase d. Matches decimal digit 0-9.

re.search(r'c\d\dkie', 'c00kie').group()

#^ - Caret. Matches a pattern at the start of the string.

re.search(r'^Eat', 'Eat cake').group()

#$ - Matches a pattern at the end of string.

re.search(r'cake$', 'Eat cake').group()

re.search(r'Number: [0-6]', 'Number: 5').group()

#\A - Uppercase a. Matches only at the start of the string. Works across multiple lines as well.

re.search(r'\A[A-E]ookie', 'Cookie').group()

#\b - Lowercase b. Matches only the beginning or end of the word

re.search(r'\b[A-E]ookie', 'Cookie').group()


# This checks for '\' in the string instead of '\t' due to the '\' used
re.search(r'Back\\stail', 'Back\stail').group()

#{x} - Repeat exactly x number of times.

#{x,} - Repeat at least x times or more.

#{x, y} - Repeat at least x times but no more than y times.

re.search(r'\d{9,10}', '0987654321').group()

pattern = "cookie"
sequence = "Cake and cookie"

heading  = r'<h1>TITLE</h1>'
re.match(r'<.*>', heading).group()

#search(pattern, string, flags=0)

pattern = "cookie"
sequence = "Cake and cookie"

re.search(pattern, sequence).group()

#match(pattern, string, flags=0)
pattern = "C"
sequence1 = "IceCream"

# No match since "C" is not at the start of "IceCream"
re.match(pattern, sequence1)


#search() versus match()
#The match() function checks for a match only at the beginning of the string (by default) whereas the search() function checks for a match anywhere in the string.


#findall(pattern, string, flags=0)
email_address="test@gmail.com  test1@gmail.com"
#'addresses' is a list that stores all the possible match
addresses = re.findall(r'[\w\.-]+@[\w\.-]+', email_address)
for address in addresses:
    print(address)



print(re.search(r'Spokes Person:\w*\s\w*\s\w*', 'Spokes Person:fsjhhfjhajhjshajhjfj ewhfjhhwh hewfkjhhw').group())
#In a file there is some ip address and server name extract ip address and server name separately and print 
#using generators find all prime numbers between 1-100 
#In a file there are word containing special characters ,print those words
#validate an email id with help of regular expression.
#Validate ipv6 address using python regular expression 
#Match all MAC addresses in file and print all those. 


