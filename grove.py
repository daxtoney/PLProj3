from grover_parse import *

# loop 
while True:
	# read
	ln = input("Grover>> ")
	root = parse(ln)
	# eval
	res = root.eval()
	# print 
	if not res is None:
		print(res)