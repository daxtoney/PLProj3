from grover_parse import *

while True:
    ln = input("Grover>> ")
    root = parse(ln)
    res = root.eval()
