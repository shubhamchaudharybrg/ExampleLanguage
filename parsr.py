# This is a parser file.
import lexr as lx

#Function for addition.
def ADD(*args):
	t = 0
	for ii in args:
		t += ii
	return t

#Function for subtraction.
def SUB(*args):
	t = args[0]
	for ii in args[1:]:
		t -= ii
	return t

#Function for division.
def DIV(*args):
	t = args[0]
	for ii in args[1:]:
		t /= ii
	return t

#Function for multiplication.
def MUL(*args):
	t = 1
	for ii in args:
		t *= ii
	return t

#Function for defining integer.
def INT(args):
	op = args.replace(' ','')
	equal_sign = op.find('=')
	aftr_equal = int(op[equal_sign+1:])
	op[0:equal_sign] = aftr_equal

#This is Parser.
func_vars = ["INT","STR","ADD","SUB","MUL","DIV","PRINT"]
t_list = []
#tempVar = [0,1,2,3,4,5,6,7,8,9]
def parser(args):
	tokens = lx.lexer(args)
#	print(values)
	if tokens[0] in func_vars:
		if tokens[0] == 'PRINT':
			print(tokens[1])
		elif tokens[0] != 'PRINT':
			for ii in tokens[1]:
				if ii in [str(i) for i in range(0,10)]:
					operand = int(ii)
					#t_list = []
					t_list.append(operand)
#			print(t_list)
			if tokens[0] == 'ADD':
				print(ADD(*t_list))
				t_list.clear()
			if tokens[0] == 'SUB':
				print(SUB(*t_list))
				t_list.clear()
			if tokens[0] == 'MUL':
				print(MUL(*t_list))
				t_list.clear()
			if tokens[0] == 'DIV':
				print(DIV(*t_list))
				t_list.clear()
	else:
		print('CommandError : Invalid command.')

