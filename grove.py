"""
Is your Grove interpreter using a static or dynamic type system? 
Briefly explain what aspects of the interpreter make it so.

Our interpriter is using a dynamic type system. 
We know this is the case because we don't require users to 
declare a type when they make a new variable. We also have to check 
on our end to make sure the types match up when doing addition since 
the user doesn't have to declare what types they are adding. 

Users can also do the following 

Grove>> set x = "Hello"
Grove>> x
Hello
Grove>> set x = 420
Grove>> x
420

"""

from grove_parse import *

if __name__ == "__main__": 
	# loop 
	while True:
		# read
		ln = input("Grove>> ")

		try:
			root = parse(ln)
			# eval
			res = root.eval()
			# print 
			if not res is None:
				print(res)
		except GroveError as e:
			print(e)
