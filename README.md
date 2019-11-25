# ExampleLanguage
This repo contains an example language built using Python.

The lexr.py file contains the lexer to extract tokens.

The parsr.py contains the parser to parse the tokens.

The interpreter.py contains the actual interpreter of the example language.

###########################################################################

USE........................................................................

python interpreter.py                                                      

Example program to implement functions of BASIC Language.

BASIC >> ADD 2,2
4

BASIC >> SUB 7,5
2

BASIC >> MUL 3,4
12

BASIC >> PRINT Hello World!
Hello World!

BASIC >> print hello world!
SyntaxError : Commands must be in upper case.
CommandError : Invalid command.                                              

BASIC >> PRINTT hello
CommandError : Invalid command.

BASIC >>
