import parsr.py as pr

#Interpreter.
def interpreter():
	print('\nExample program to implement functions of BASIC Language.\n')
#Terminal of the BASIC.
	while True:
		ip = input('BASIC >> ')
		if ip == 'EXIT':
			break
		else:
			pr.parser(ip)
			#print(values)
#       elif not ip:
#               return 'VoidError : Input is None.'
if __name__ == '__main__':
	interpreter()
#       print(interpreter())
