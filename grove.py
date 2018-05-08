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
