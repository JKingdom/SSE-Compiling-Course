from ply import *

tokens = (
    'H1','H2','H3', 'CR', 'TEXT', 'STAR', 'DOUBLESTAR', 'UL', 'DUL',  'EQL','SUB' #'BLANK', 
    )

# Tokens
t_H1 = r'\#'
t_H2 = r'\#\#'
t_H3 = r'\#\#\#'
t_STAR = r'\*'
t_DOUBLESTAR = r'\*\*'
t_UL=r'\_'
t_DUL=r'\_\_'
t_SUB=r'[-]+'   ##正则表达的改变
t_EQL=r'[=]+'

def t_TEXT(t):
    r'[a-zA-Z0-9\ \,\.\'\?]+'
    t.value = str(t.value)
    return t

t_ignore = "\t"

def t_CR(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def mklex_run(filename):
    lexer.input(open(filename).read())
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        print tok

if __name__ == '__main__':
    filename = 'test01.md'
    lexer.input(open(filename).read())
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        print tok