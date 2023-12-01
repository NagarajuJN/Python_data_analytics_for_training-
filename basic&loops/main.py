print("Hello Nagaraj")
# Hello Nagaraj

#---------------variables
# Integer
a = 2
print(a)
# Output: 2
# Integer
b = 9223372036854775807
print(b)
# Output: 9223372036854775807
# Floating point
pi = 3.14
print(pi)
# Output: 3.14
# String
c = 'A'
print(c)
# Output: A
# String
name = 'Nagaraj '
print(name)
# Output: Nagaraj
# Boolean
q = True
print(q)
# Output: True

# Empty value or null data type
x = None
print(x)
# Output: None
# ===========================================

#Rules for variable naming:
#1. Variables names must start with a letter or an underscore.
 x = True # valid
 _y = True # valid
 9x = False # starts with numeral
#=> SyntaxError: invalid syntax
 $y = False # starts with symbol
# SyntaxError: invalid syntax
#2.The remainder of your variable name may consist of letters, numbers and underscores.
has_0_in_it = "Still Valid"
# 3. Names are case sensitive.
x = 9
y = X*5
# =>NameError: name 'X' is not define


# =======================================
# User Input
# Interactive input
# To get input from the user, use the input function
#


name = input("What is your name? ")
# Out: What is your name?

# =====================


# Comments are used to explain code when the basic code itself isn't clear.
# Python ignores comments, and so will not execute code in there, or raise syntax errors for plain English sentences.
# Single-line comments begin with the hash character (#) and are terminated by the end of line.
# Single line comment:
# This is a single line comment in Python
# Inline comment:
print("Hello World") # This line prints "Hello World"
# Comments spanning multiple lines have """ or ''' on either end. This is the same as a multiline string, but
# they can be used as comments:
"""
This type of comment spans multiple lines.
These are mostly used for documentation of functions, classes and modules.
""""""











# =========================
# Indentation
# """Python uses indentation to define control and loop constructs. This contributes to Python's readability, however, it
# requires the programmer to pay close attention to the use of whitespace. Thus, editor miscalibration could result in
# code that behaves in unexpected ways"""

# For example:
def my_fun(): # This is a function definition.
 a = 1111 # This line belongs to the function because it's indented
 return a # This line also belongs to the same function
print(my_fun()) # This line is OUTSIDE the function bloc

a =10
b=20
if a > b: # If block starts here
 print(a) # This is part of the if block
else: # else must be at the same level as if
 print(b) # This line is part of the else bloc


# =========================

# If statement

#  if, elif, and else
# In Python you can define a series of conditionals using if for the first one, elif for the rest, up until the final
# (optional) else for anything not caught by the other conditionals.
number = 5
if number > 2:
 print("Number is bigger than 2.")
elif number < 2: # Optional clause (you can have multiple elifs)
 print("Number is smaller than 2.")
else: # Optional clause (you can only have one else)
 print("Number is 2.")
# Outputs Number is bigger than 2
# Using else if instead of elif will trigger a syntax error and is not allowed
if condition:
 body
# The if statements checks the condition. If it evaluates to True, it executes the body of the if statement. If it
# evaluates to False, it skips the body.
if True:
 print "It is true!"
 # output: It is true!
if False:
 print "This won't get printed.."
# The condition can be any valid expression:
if 2 + 2 == 4:
 print "I know python!"
# output: I know python
# ==============================

# Loops

"""for loops iterate over a collection of items, such as list or dict, and run a block of code with each element from
the collection."""
for i in [0, 1, 2, 3, 4]:
 print(i)

 #output:
 0
1
2
3
4


# range:
# is a function that returns a series of numbers under an iterable form, thus it can be used in for loops:
for i in range(5):
 print(i)

  #output:
 0
1
2
3
4
# To iterate through a list you can use for:
for x in ['one', 'two', 'three', 'four']:
 print(x)
#  out the elements of the list:
one
two
three
four



# A while loop will cause the loop statements to be executed until the loop condition is fasle. The following code will
# execute the loop statements a total of 4 times.
i = 0
while i < 4:
 #loop statements
 i = i + 1

 # =======================================


 # Break and Continue in Loops
# break statement
# When a break statement executes inside a loop, control flow "breaks" out of the loop immediately:
i = 0
while i < 7:
 print(i)
 if i == 4:
 print("Breaking from loop")
 break
 i += 1

# output:
0
1
2
3
4
Breaking from loop

# ex:

a = [1, 2, 3, 4]
for i in a:
 if type(i) is not int:
 print(i)
 break
else:
 print("no exception")

# ==================
# continue statement
# A continue statement will skip to the next iteration of the loop bypassing the rest of the current block but
# continuing the loop. As with break, continue can only appear inside loops:
for i in (0, 1, 2, 3, 4, 5):
 if i == 2 or i == 4:
 continue
 print(i)

# output:

0
1
3
5

# ==============================
#  Local Variables
# If a name is bound inside a function, it is by default accessible only within the function:
def foo():
 a = 5
 print(a) # ok
print(a) # NameError: name 'a' is not define


# ==========================

# Global Variables
# In Python, variables inside functions are considered local if and only if they appear in the left side of an assignment
# statement, or some other binding occurrence; otherwise such a binding is looked up in enclosing functions, up to
# the global scope. This is true even if the assignment statement is never executed.
x = 'Hi'
def read_x():
 print(x) # x is just referenced, therefore assumed global
read_x() # prints Hi
