Flow Control
	
	Boolean > True or False
	Boolean Comparisons > ==, !=, <, >, <=, >=
	Boolean Operators > and, or, not
		and > True, True > True (Only if 2 are True in the same Operation is everything True)
			  True, False > False
			  False, True > False
			  False, False > False

		or > True, True > True (If 1 is True the whole Operation is True)
			 True False > True
			 False True > True
			 False False > False

		not > not True > False
			  not False > True

	Mixing Boolean and Comparison Operators (It goes from Left side, refreshes and calculates right side or next side)
		(4 < 5) and (5 < 6)
		True

	Elements of Flow Control (Conditions > more specific in Flow Control == Expressions)

		Conditions (statements/functions) (if, else, elif, for, range(), break/continue, pass)

		Blocks ( Indentation in a statement)

		if max = "max"
			> 	print('ree') | block Indentation
		elif max = "ray"
			>	print('ray stfu') | block Indentation
		else 			 
			>	print('gay') | block Indentation

	Flow Statements (always : at end)

		if statement: (example above)

		else statement: (example above)

		elif statement: (example above)	

		while loop statement:

			while spam < 5:
			print('Hi')
			spam = spam +1

		break statement: (while loop statements automatically stops when reached 'break')

			while True:
				print('Name? ')
				name = input()
				if name == 'your name':
				>	break | when reached it will stop the while loop
			print('Thanks')

		continue statement: (while loop statements automatically continues when reached 'continue')

			while True:
				print('Name? ')
				name = input()
				if name != 'Joe':
					continue
				print('Hello Joe, whats the pass homie ')
				password = input()
				if password == 'swordfish':
					break
			print('Access granted')	

		for loops and range() Function: (requires: for keyword, a var, in keyword, 
										 a call to range() = up to 3 digits)

			for i in range(5):
				print('Jerry %s' %i)

		An Equivalent while loop (same as a for loop)

			print('My name is')
			i = 0
			while i < 5:
				print('Jimmy Five Times (' + str(i) + ')')
				i = i + 1

		Starting, Stopping, Stepping Arguments in range()

			for i in range(12 ,16)
			> 12
			> 13
			> 14
			> 15

			for i in range(0, 10, 2)
			> 2
			> 4
			> 6
			> 8

			for i in range(5, -1, -1)
			> 5
			> 4
			> 3
			> 2
			> 1
			> 0

		importing modules ( import name, more module names)

		from import statements (from module import command)

		Ending a Program with sys.exit()

			import sys

			while True:
				print('Type exit to exit. ')
				response = input()
				if response == 'exit':
					sys.exit()
				print('You typed ' + response + '.')
		


Practice Questions

1. True or False with big F and True

2. and or not

3. and 
	True and True = True
	True and False = False
	False and True = False
	False and False = False

   or 
   True or True = True
   True or False = True
   False or True = True
   False or False = False

   not
   not True = False
   not False = True

 4.  True and False = False
     False 
     True or False = True
     not (True or False) = False
     True and False = False
     True or False = True

  5. ==, !=. <, >, <=, >=

  6. = -> is used to assign a var
  	 == is to compare in a comparison or statement

  7. A condition is more specific in Flow Control, to evaluate to a Boolean

  8. spam = 0
     if spam == 10:
     >	print('eggs')
     	if spam > 5:
     >		print('bacon')
   		else:
     >		print('Ham')
     	print('spam')
     print('spam')


    9. spam = 1 

    	if spam == 1:
    		print('Hello')
    	elif spam == 2:
    		print('Howdy')
    	else:
   			print('Greetings!')

   	10. Ctrl + C

   	11. Break = Stops the whole loop where it is 
   		Continue = Continues with the loop 

   	12. range(10) = 0 - 10
   		range(0, 10) = 0 - 10
   		range(0, 10, 1) = 0 - 10

   	13. for i in range(0, 11):
   			print(i)

   		i = 0
   		while i <= 10:
   			print(i)
   			i = i + 1
   	14. import spam

   		def bacon():
    		print('hey')

		spam.bacon()















