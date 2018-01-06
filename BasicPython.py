#!/usr/bin/python3 ##this is shebang and it tells the compiler where is the path
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

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
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