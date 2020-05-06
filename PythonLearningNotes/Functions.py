#Functions are like a mini program in the program



#def = beginning of functions followed up with name of the function with () and colon


	# Def Statements with Parameters

		print(argument)

		#You can assign a Parameter to a function and when calling it you can type out an argument

		def Hello(name): # Parameter in the ()
			print('Hello %s' %name)


		Hello('Alice') # Argument in the ()
		Hello('Bob') # Argument in the ()

		#Once the function returns the value in the Parameter is lost

		hello('Bob')
		print(name) # It will give an error because name has already return in the Function, 
					# it referees to a var that doesn't exist



	# Return Value and return Statements

		# The value that a function call evaluates to is called the return value of the function

		import random


		def getAnswer(answerNumber):
    		if answerNumber == 1:
       			 return 'no'
    		elif answerNumber == 2:
        		 return 'right'


		r = random.randint(1, 9)
		fortune = getAnswer(r)
		print(fortune)



	# The None Value

		# None represents the absence of a value.
		# None is the only value of the NoneType data type.
		# None in other languages = null, nil, or undefined.

		# Unlike input() or len() that return something print() doesn't, which makes print() return None.

		spam = print('Hello')

		None = spam

		>>> True

		# Python automatically adds no return to every function that doesn't return anything.
		# While or for loops implicitly end with a continue statement.
		# If you use return statement with no value, None is returned.



	# Keyword Arguments and print()

		# Most arguments are identified by their position in the function call.
		# Keyword arguments are identified by the keyword put before them in the function call.
		# Keyword arguments are often used for optional parameters.
		# Example: print() has optional parameters called end and sep to specify what should be printed
		# end - Whats printed at the end, sep - Whats printed between the arguments (separating them)

		# end example

		print('Hello', end='') # You can disable the new line with end=''
		print('World')

		>>> HelloWorld


		# sep example

		print('cats', 'dogs' 'mice', sep=',') # It separates the names with a comma 

		>>> cats,dogs,mice



	# Local and Global Scope

		# Parameters and Arguments that are assigned to a call function are said to exist in that
		# functions "Local Scope".
		# Variable that exists in the "Local Scope" is called the "Local Variable".

		# Variables that are assigned outside all functions are said to exist in the "Global Scope".
		# Variable that exists in the "Global Scope" is called the "Global Variable".

		# A Variable must be one or the other, it can't be both.

		# Scope is like a container for variables. Scope gets destroyed, all the variables are forgotten.
		# There is only one Global Scope, and its created when the program begins. When Program 
		# terminates, so does the Scope.
		# Local Scope is only created when a function is called.
		# Any vars assigned in this function exist within the local scope. When the function returns,
		# the local scope is destroyed, and the vars are forgotten.

		# Why Scopes matter:

			# Code in the Global scope cannot use any Local vars.
			# Local Scope can access Global vars.
			# Code in a functions Local Scope cannot use vars in any other Local Scope.
			# You can use same name for var if they are in different Scopes. That is, var Spam can exist in
			# Local and Global Scopes.

		# The Reason why Python has different Scopes is so vars can be modified by the code in a
		# particular call to a function, the function interacts with the rest of the program
		# only through its parameters an the return value.

		# If the program contained nothing but Global vars, if theres a bug, it will be hard to find, if your
		# program is thousands of lines.
		# If the program had a bug in a local var, you'd know which function it is.

		# Running global vars in small programs is fine, but its a bad habit relying on global vars,
		# when your programs become larger and larger.
	


	# Local Variables Cannot Be Used in the Global Scopes

		def spam():
			eggs = 1329371

		spam()
		print(eggs)

		# This will give out an error, because print() is trying to access an argument in the Global Scope,
		# when the argument in reality in a Local Scope is, in a function.



	# Local Scopes Cannot Use Variables in Other Local Scopes

		def spam():
			eggs = 99
			bacon()
			print(eggs)

		def bacon():
			ham = 101
			eggs = 0

		spam()

		# When the program stars spam() is called, it sets eggs to 99, calls bacon, which does its job
		# but when it tries to return, the vars from that call are destroyed, and the spam() continues
		# where it left off.

	# Global Variables Can be Read from a Local Scope

		def spam():
			print(eggs)
		eggs = 42
		spam()
		print(eggs)		


		# Because eggs was assigned outside of the Local Scope, eggs becomes global, and spam() can access
		# vars from Global.



	# Local and Global Variables with the Same Name

		# To make life easier avoid using Local Vars with the same name as a Global Var or another Local Var
		# But technically, its possible.


		def spam():
			eggs = 'spam local'
			print(eggs)  # prints 'spam local'

		def bacon():
			eggs = 'bacon local'
			prints(eggs) # prints 'bacon local'
			spam() 
			print(eggs) # prints 'bacon local'	

		eggs = 'global'
		bacon()
		print(eggs) 

		# They are 3 different Vars in the program, but because of the Global and the 2 Local Scopes, 
		# they never interact with each other.



	# The Global Statement

	def spam():
    	global eggs
    	eggs = 'spam'

	eggs = 'global'
	spam()
	print(eggs)

	>>> spam

		# Because global eggs was at the beginning of spam(), it changed the global Var eggs from 'global'
		# to 'spam'. No local 'spam' Var was created.

			# There are 4 rules to tell if a Var is Local or Global:

				# 1. If a Var is being used outside of any Function, then its always a Global Var.

				# 2. If there is a Global statement in a Function for that Var, its a Global Var.

				# 3. If a Var is used in an assignment statement in the Functions, its a Local Var.

				# 4. If the Var is not used in an assignment statement, its not a Global Var.

		# Examples:

	def ham():
		print(eggs) # GLOBAL

	

	eggs = 42 # GLOBAL
	myFunction()
	print(eggs)



	def bacon():
		eggs = 'bacon' # LOCAL



	def spam():
		global eggs # LOCAL
		eggs = 'spam'


		# You can't use a Local Var in a Function before you assign it.

	def spam():
    	print(eggs)
    	eggs = 'spam local' # < Has to go above print()

	eggs = 'global'
	spam()

		# It puts out an error!



# Exception Handling // error Handling

	# error > python program crashes. You dont want this in real world programs. You want the
	# to detect errors, handle them and then continue to run.


def spam(divideBy):
	return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

>>> 21.0
>>> 3.5
>>> ERROR  # Division Error: You cant divide by zero

	# Errors can be handled by try and except statements.


def spam(divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		print('Error: Invalid argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

	# If error is found it will go to the except statement, run it, and go back where it was and continue.

def spam(divideBy):
	return 42 / divideBy

try:
	print(spam(2))
	print(spam(12))
	print(spam(0))
	print(spam(1))
except ZeroDivisionError:
	print('Invalid argument.')

	# This will also do the same thing as before but instead of continuing its gonna stop and not print
	# out the spam(1)



# A short Program: Guess the Number

	# Simple Guess the Number Game

import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for guessesTaken in range(1, 7)
	print('Take a guess.')
	guess = int(input())
	if guess < secretNumber:
		print('Your guess is too low')
	elif guess > secretNumber:
		print('Your guess is too high')
	else:
		break # Correct Guess


if guess == secretNumber:
	print('Good job.')
else:
	print('Nope. The number i was thinking of %s' %str(secretNumber))



#Practice Questions

	#1. You dont have to duplicate code, which means less errors, tidier, more readable. # Correct

	#2. It executes when the function is called. With myFunction(). # Correct

	#3. MyFunction() # Kinda Correct
			# CODE

	#4. Function is where the code is contained, and the code will not be run until its been called. # Correct

	#5. There is one Global Scope, and there are as many Local Scopes as Functions that you create. # Correct

	#6. They loose their values. # Correct

	#7. A return value is the Functions expression. The Function calculates something and the return
	  # command return the end value. # Kinda Correct, More on the wrong side.

	#8. it is None. # Correct

	#9. you use 'global variable name' # Correct

	#10. Its a NoneDataType. Its the absence of a value. #Correct

	#11. the import statement, imports commands from a library. # Correct

	#12. spam.bacon() # Correct

	#13. You can use try and except. # Correct 

	#14. In the try clause, goes all the expressions. And the except clause contains the error value. # Correct

	1 Failed, 12 Correct, 1 Incomplete

