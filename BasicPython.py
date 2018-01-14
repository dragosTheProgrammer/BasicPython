#!/usr/bin/python3 ##this is shebang and it tells the compiler where is the path for the unix like system (Mac, Linux)
"""
# conditionals
#if-elif-else
a, b = 5, 5

if a < b:
    print('a ({}) is less than b ({})'.format(a, b))  #curly braces for showing inside the values using .format method
elif a==b:
 print("a({}) is the same as b({})".format(a,b)) #it is working with only one space indentation but 
 												# usually it is tab used for indent
else:
    print('a ({}) is not less than b ({})'.format(a, b))

#ternary operator ~similar from c (a<b? TRUE:FALSE)
print("TRUE" if a<b else "FALSE") 
"""
#####################################################################################################################

# loops
"""
#for loop
for x in range(0,4):
	print("number ({}) is x".format(x))

#for else
for x in range(0,10):
	print (x)
else:
	print("The x is not in range anymore")

#Strings as iterable This will print each char on separate line
stringToBePrinted  = "Hello Github!"
for s in stringToBePrinted:
	print (s)

# Lists as an iterable
#colection is an iterable
colection = ['this', 'is', 'a', 'colection', 1,2,3]

for c in colection:
	print (c)

#Loop over Lists of lists
list_of_lists = [[1,2,3],[4,5,6],[7,8,9],[10,11,12,13,14,15]] #the list can have diffrent dimesions
for list in list_of_lists:
	for x in list:
		print (x)

#while loop
Index = 0

while Index <= 100:
	Index+=1
	print((Index))
	if Index == 89:
		print('Break the Index is 89')
		break
print('the loop is done')

"""



#####################################################################################################################
#functions aka methods
"""
def isNumberOdd_b(n):
	if n%2 == 0:
		return True
	else:
		return False

for n in range(0, 100):
	print ( "the number {}".format(n), "is odd is", isNumberOdd_b(n))

"""
#####################################################################################################################
#Generators are creating an iterator using yield
# they are iterators but you can only iterate over them once. It's because they do not store all the values in memory
# they gen the values on the fly
"""
def CreateAGen(rangeNo =3):
	Mylist = range(rangeNo)
	for index in Mylist:
		yield index

# Yield is a keyword that is used like return, except the function will return a generator.
mygenerator= CreateAGen(100)
mygenerator2 = (x for x in range(300))

for i in mygenerator:
	print(i)

for i in mygenerator2:
	print(i)
"""
#####################################################################################################################
#class and polymorphism
"""
class ThisIsAClass_c():

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def Sum(self):
		return self.x+self.y 



class ThisIsDerivedClass(ThisIsAClass_c): #this class inherits ThisIsAClass
	def Subtraction(self):
		return self.x - self.y



c = ThisIsAClass_c(5,9)
print(c.Sum())

d = ThisIsDerivedClass(6,1)
print(d.Subtraction())

"""
#####################################################################################################################
"""
#Exceptions try except

#div with 0
# IOError
# If the file cannot be opened.

# ImportError
# If python cannot find the module

# ValueError
# Raised when a built-in operation or function receives an argument that has the
# right type but an inappropriate value

# KeyboardInterrupt
# Raised when the user hits the interrupt key (normally Control-C or Delete)

# EOFError
# Raised when one of the built-in functions (input() or raw_input()) hits an
# end-of-file condition (EOF) without reading any data


#error opening file
try:
	fh = open('textFile.txt')
except IOError as e:
	print("An error has encounter {}".format(e))

#div by 0
a, b = 0,5

try:
	c = b/a
except ZeroDivisionError as z:
	print("The error is {}".format(z))
""" 
 #####################################################################################################################

#creating a main script it is used when you have diffenrt functions and you want that those fucntions to be seen
""""
def main():
	print("This is main")
	ThisIsAnotherMethod()

print("this will be called first")

def ThisIsAnotherMethod():
	print("Now ThisIsAnotherMethod it is called")
	pass


if __name__ == "__main__": main() #basiclly main is called of EOF

"""
#####################################################################################################################
# x = 5
# id is unique and it is a large number 
# type(x) -> <class 'int'>
# if I change the x = 6 it will have a different id because it points to a different object 
# x = 6 id(x) = 50000008 if i change it back to 5 > id(x) = 50000004
# basically the object is imutable and i only changed the reference to the object 
# #####################################################################################################################
#basic operations
"""
num = 12/ 5 
print (type(num), num) #<class 'float'> 2.4

num = 12// 5 
print (type(num), num) #<class 'int'> 2

num = 12%8 
print (type(num), num) #<class 'int'> 4

num = int(9.5) #calling the constructor of int object
print (type(num), num) #<class 'int'> 9


"""
# print(divmod(5,3)) #this is showing div and modulo res in tuple (1, 2)

#bitwise operations
#let's make a method for converting a number in binary
def DecToBin(no): print('{:08b}'.format(no)) 

# DecToBin(10)

# & | ^ << >> ~
#####################################################################################################################
#compare objects is/is not to know if it is the same object
x,y= 5, 6
print(id(x)) #1584387184
print(id(y)) #1584387200
# is used when youa re comparing objects
print(x is y) #False

y = 5
x = 5
print(id(x)) #1584387184
print(id(y)) #1584387184
print(x is y) #True

# if w have separate lists they have diffrent ids

y = [5]
x = [5]
print(id(x)) #91626912
print(id(y)) #91625032
print(x is y) #False
print(x == y) #True
#####################################################################################################################
#and or
#difference here is that and an or are not & and | bcs these are bitwise
#eg
a = 2
b = 5
c = 7
if a<2 and b>3 or c ==7:print("condition true")
 
#####################################################################################################################
 #slice operator
lst = [9,8,7,6,5,4,3]
print(lst[0:5]) #this is a slice
for i in range(0,7): print(lst[i])
#add 50 items in the list
lst[:] = range(50)
print(lst) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
#lst[slice begin:slice end non inlcusive - without hte last element: how many elements to step over(din cat in cat sa sara)]
print(lst[10:20:3]) #[10, 13, 16, 19]
#you can replace the slice content
lst[0:5] = (5,5,5,5,5)
print(lst) #[5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12 .....49]
#####################################################################################################################
#Strings
s = "Hello \n World"
#print(s)  
# Hello 
#  World

#raw string
s = r"Hello \n World" #Hello \n World -> on a single line
#print(s) 

#triple quote strings
# it is working also with '''

s = """\ 
This is a  
new
way
of Saying 
Hello
"""
#print(s) 
#####################################################################################################################

#tuple and lists

#tuple
#I can't add change it it is imutable
x = (1,3,4)
# print(type(x), x) #<class 'tuple'> (1, 3, 4) 

#list
#Mutable
x = [1,3,4]
# print(type(x), x) #<class 'list'> [1, 3, 4]
x.insert(2, 99)#<class 'list'> [1, 3, 99, 4]
x.append(120) #<class 'list'> [1, 3, 99, 4, 120]



"""
https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples
part from tuples being immutable there is also a semantic distinction that should guide their usage. Tuples are heterogeneous data structures 
(i.e., their entries have different meanings), while lists are homogeneous sequences. Tuples have structure, lists have order.

Using this distinction makes code more explicit and understandable.

One example would be pairs of page and line number to reference locations in a book, e.g.:

my_location = (42, 11)  # page number, line number
You can then use this as a key in a dictionary to store notes on locations. A list on the other hand could be used to store multiple locations. 
Naturally one might want to add or remove locations from the list, so it makes sense that lists are mutable. 
On the other hand it doesn't make sense to add or remove items from an existing location - hence tuples are immutable.

There might be situations where you want to change items within an existing location tuple, for example when iterating 
through the lines of a page. But tuple immutability forces you to create a new location tuple for each new value. 
This seems inconvenient on the face of it, but using immutable data like this is a cornerstone of value types and functional programming techniques, which can have substantial advantages.
"""
#####################################################################################################################
#dictionaries - mutuable objects
# dic = {'one':1, 'two':2, 'three':3, 'eight':8}

# for key in dic:
# 	#print(key) 
# 	# one
# 	# two
# 	# three
# 	# eight
# 	print(dic[key])
# 	# 1
# 	# 2
# 	# 3

# for key in sorted(dic.keys()):  #this is alpahetically sorted
# 	#print(key) 
# 	# eight
# 	# one
# 	# three
# 	# two
# 	print(dic[key])
# 	# 8
# 	# 1
# 	# 3
# 	# 2

#we can use the dict class
# dic = dict(				

# 	one = 1,
# 	two =2,
# 	nn =99,
# 	three = 3,
# 	four =4

# 	)
# for key in dic:
# 	print(key, dic[key])
	# one 1
	# two 2
	# nn 99
	# three 3
	# four 4

# You can use enumarate method which is returning index and value
# str = "Hello World!"

# for index, char in enumerate(str):
# 	print(index, char)

#####################################################################################################################

#####################################################################################################################
"""
Copyright https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

To understand what yield does, you must understand what generators are. And before generators come iterables.

Iterables
When you create a list, you can read its items one by one. Reading its items one by one is called iteration:

>>> mylist = [1, 2, 3]
>>> for i in mylist:
...    print(i)
1
2
3
mylist is an iterable. When you use a list comprehension, you create a list, and so an iterable:

>>> mylist = [x*x for x in range(3)]
>>> for i in mylist:
...    print(i)
0
1
4
Everything you can use "for... in..." on is an iterable; lists, strings, files...

These iterables are handy because you can read them as much as you wish, but you store all the values in memory and this is not always what you want when you have a lot of values.

Generators
Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly:

>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)
0
1
4
It is just the same except you used () instead of []. BUT, you cannot perform for i in mygenerator a second time since generators can only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.

Yield
yield is a keyword that is used like return, except the function will return a generator.

>>> def createGenerator():
...    mylist = range(3)
...    for i in mylist:
...        yield i*i
...
>>> mygenerator = createGenerator() # create a generator
>>> print(mygenerator) # mygenerator is an object!
<generator object createGenerator at 0xb7555c34>
>>> for i in mygenerator:
...     print(i)
0
1
4
Here it's a useless example, but it's handy when you know your function will return a huge set of values that you will only need to read once.

To master yield, you must understand that when you call the function, the code you have written in the function body does not run. The function only returns the generator object, this is a bit tricky :-)

Then, your code will be run each time the for uses the generator.

Now the hard part:

The first time the for calls the generator object created from your function, it will run the code in your function from the beginning until it hits yield, 
then it'll return the first value of the loop. Then, each other call will run the loop you have written in the function one more time, and return the next value, until there is no value to return.

The generator is considered empty once the function runs but does not hit yield anymore. It can be because the loop had come to an end, or because you do not satisfy an "if/else" anymore.
"""
09