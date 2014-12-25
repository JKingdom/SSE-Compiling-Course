from ply import *


tokens = (
    'H1',
    'H2',
    'H3',
    'CR',
    'TEXT',
    'DOUBLESTAR',
    'HR',
    'POINT',
    'LEMI','RIMI',
    'LESM','RISM',
    'LEST', 'RIST',
    'LI', 'SELI', 'TRLI',
    'STAR',
    'NLI', 'SENLI', 'TRNLI',
    'NUMBER',
    'T'
    )

# Tokens
t_H1 = r'\#'
t_H2 = r'\#\#'
t_H3 = r'\#\#\#'
t_DOUBLESTAR = r'[\*\_]{2}'
t_HR = r'([-=\*]\ *){3,}(?=\n)'
t_LI = r'(?m)^[\*\-\+](?=\ +[^\*\-]+$)'
t_SELI = r'(?m)^\t[\*\-\+](?=\ +[^\*\-]+$)'
t_TRLI = r'(?m)^\t{2}[\*\-\+](?=\ +[^\*\-]+$)'
t_STAR = r'[\*\_](?!\ *[\*\_])'
t_POINT = r'`(?!\ *`)'
t_LEMI = r'\[(?=.*\]\(.*\))'
t_RIMI = r'\](?=\(.*\))'
t_LESM = r'\((?=.*\))'
t_RISM = r'\)'
t_LEST = r'<(?=.*>)'
t_RIST = r'>'
t_NLI = r'(?m)^\d\.(?=\ +[^\*\-]+$)'
t_SENLI = r'(?m)^\t\d\.(?=\ +[^\*\-]+$)'
t_TRNLI = r'(?m)^\t{2}\d\.(?=\ +[^\*\-]+$)'
t_NUMBER = r'\d+(?!\.\ )'
t_T = r'\t(?![\*\d])'

def t_TEXT(t):
    r'[^\t\d=`\+\n\_\*\#\[\]\(\)<>-]+'
    t.value = str(t.value)
    return t

t_ignore = ""


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