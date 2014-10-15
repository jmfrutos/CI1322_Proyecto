import ply.lex as lex
tokens = ('IF', 'ELSE', 'NUM', 'LPAREN', 'RPAREN', 'VAR', 'PRINT')
reserved = {
	'if' : 'IF'
	'else' : 'ELSE'
	'int' : 'INT'
	'print' : 'PRINT'
}
t_LPAREN = r'\('
t_RPAREN = r'\)'
def t_NUM(t):
    r'd+'
    try:
        t.value = int(t.value)
    except ValueError:
        print "Line %d: Number %s is too large!" % (t.lineno,t.value)
        t.value = 0
    return t
def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'VAR')    # Check for reserved words
    return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
t_ignore  = ' \t'
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)
lex.lex()
lex.runmain()



