# Lexer file to extract tokens.

def lexer(arg):
	# Tokens list.
	space_pos = arg.find(' ')
	if space_pos != -1:
		cmnd = arg[0:space_pos]
		if cmnd != cmnd.upper():
			print('SyntaxError : Commands must be in upper case.')
		return [cmnd,arg[space_pos+1:]]
	else:
		print('SyntaxError : Invalid syntax.')
		return '-1'

