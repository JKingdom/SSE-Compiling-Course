# -----------------------------------------------------------------------------
# @author globit
# This is template code of markdown generating by ply
# @update 2014-12-16
# @lience MIT
# -----------------------------------------------------------------------------
import sys

tokens = (

    'H1',
    'H2',
    'H3',
    'CR',
    'TEXT',
    'DOUBLESTAR',
    'HR',
    'POINT',
    'LEMI', 'RIMI',
    'LESM', 'RISM',
    'LEST', 'RIST',
    'LI', 'SELI', 'TRLI',
    'STAR',
    'NLI', 'SENLI', 'TRNLI',
    'NUMBER',
    'T', 'code', 'rbrace', 'codeline',
    'IMG',
    'ILEMI', 'IRIMI',
    'ILESM', 'IRISM',
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
t_ANY_NUMBER = r'\d+(?!\.\ )'
t_T = r'\t(?![\*\d])'

def t_ANY_TEXT(t):
    r'[^\t!\d=`\+\n\_\*\#\[\]\(\)<>-]+'
    t.value = str(t.value)
    return t

t_ignore = ""


def t_CR(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    return t

# Declare the state
states = (
  ('code', 'exclusive'),
  ('img', 'exclusive'),
)

# Match the first {. Enter code state.
def t_code(t):
    r'\`\`\`\n'
    t.lexer.code_start = t.lexer.lexpos        # Record the starting position
    t.lexer.level = 1                          # Initial brace level
    t.lexer.begin('code')                     # Enter 'ccode' state
    t.lexer.lineno += 1
    return t

# Rules for the code state
#def t_code_lbrace(t):     
#    r'\`\`\`\n'
#    t.value = str(t.value)
#    t.lexer.level +=1 
#    t.lexer.lineno += 1
#    return t             

def t_code_rbrace(t):
    r'\`\`\`\n+'
    t.value = str(t.value)
    t.lexer.lineno += t.value.count("\n")
    #t.lexer.lineno += 1
    t.lexer.level -=1

    # If closing brace, return the code fragment
    # if t.lexer.level == 0:
        #t.value = t.lexer.lexdata[t.lexer.code_start:t.lexer.lexpos+1]
        # t.type = "code"
        #t.lexer.lineno += t.value.count('\n')
        #t.value = "```"
    t.lexer.begin('INITIAL')           
    return t
    #else:
    #    return t

def t_code_codeline(t):
    r'.*[^`\n]*\n'
    t.value = str(t.value)
    t.lexer.lineno += t.value.count("\n")
    return t    

def t_code_error(t):
    t.lexer.skip(1)


# IMG

def t_IMG(t):
    r'\!(?=\[.+?\]\(.+?\))'
    t.lexer.begin('img')                     # Enter 'img' state
    return t


t_img_ILEMI = r'\[(?=.*\]\(.*\))'
t_img_IRIMI = r'\](?=\(.*\))'
t_img_ILESM = r'\((?=.*\))'
def t_img_IRISM(t):
    r'\)'
    t.lexer.begin('INITIAL')
    return t




def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# ------------------------------------
# definitions of parsing rules by yacc
# ------------------------------------
precedence = (
    )
names = {}

def p_body(p):
    '''body : statement'''
    print '<body>' + p[1] + '</body>'

def p_state(p):
    '''statement :  expression 
    | statement expression '''
    if (len(p)==2):
        p[0] = p[1]
    else: 
        p[0] = p[1] + p[2]

def p_exp_cr_1(p):
    '''expression : H1 factor cr'''
    p[0] = '<h1>' + str(p[2]) + '</h1>'

def p_exp_cr_2(p):
    '''expression : H2 factor cr'''
    p[0] = '<h2>' + str(p[2]) + '</h2>'

def p_exp_cr3(p):
    '''expression : H3 factor cr'''
    p[0] = '<h3>' + str(p[2]) + '</h3>'

def p_exp_cr(p):
    '''expression : lines'''
    p[0] = '<p>' + p[1] + '</p>'

def p_exp_block(p):
    '''expression : block'''
    p[0] = '<block>' + p[1] + '</block>'


# code start
def p_code_codeline(p):
    '''expression : code
    | expression codeline
    '''
    if(len(p) == 2):
        p[0] = '<code>'+'<ol>'
    else:
        p[0] = p[1] + '<li>' + p[2]+'</li>' 

def p_code_end(p):
    "expression : expression rbrace"
    p[0] = p[1] + '</ol>' + '</code>'

#code end

def p_lines_factor(p):
    '''lines : lines factor
        | lines cr
        | factor
    '''
    if(len(p) == 3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_block(p):
    '''block : block bline
    | bline
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_bline(p):
    ''' bline : RIST lines cr
    '''
    p[0] = p[2]


def p_factor_text(p):
    '''factor : text'''
    p[0] = p[1]

#def p_factor_cr(p):
#    "factor : cr"
#    p[0] = '<br/>'

def p_emfactor_text(p):
    '''factor : STAR factor STAR'''
    p[0] = '<em>' + str(p[2]) + '</em>'

def p_strongfactor_text(p):
    '''factor : DOUBLESTAR factor DOUBLESTAR'''
    p[0] = '<strong>' + str(p[2]) + '</strong>'

def p_code_text(p):
    '''factor : POINT factor POINT '''
    p[0] = '<code>' + str(p[2]) + '</code>'

def p_text_TEXT(p):
    '''text : TEXT
    | text NUMBER
    | text TEXT
    '''
    if len(p)==2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]


def p_lrsm(p):
    '''factor : LEMI factor RIMI LESM factor RISM'''
    p[0] = '<a href="' + str(p[5]) + '">' + str(p[2]) + '</a>'


def p_img_lrsm(p):
    '''factor : IMG ILEMI factor IRIMI ILESM factor IRISM'''
    p[0] = '<img src="' + p[6] + '" alt="' + p[3] + '" title="" />'


def p_lrst(p):
    '''factor : LEST factor RIST'''
    p[0] = '<a href="' + str(p[2]) + '">' + str(p[2]) + '</a>'


def p_hr(p):
    '''expression : HR cr
    '''
    p[0] = '<hr/>'


def p_ex_ul(p):
    '''expression : ul '''
    p[0] = '<ul>' + p[1] + '</ul>'


def p_ex_ol(p):
    '''expression : ol'''
    p[0] = '<ol>' + p[1] + '</ol>'



def p_ul(p):
    '''ul : ul li
        | li
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_seul(p):
    '''seul : seul seli
        | seli
    '''
    if len(p) == 3:
        p[0] = str(p[1]) + str(p[2])
    else:
        p[0] = p[1]



def p_li(p):
    '''li : LI factor cr
        | seul
    '''
    if len(p)==4:
        p[0] = '<li>' + str(p[2]) + '</li>'
    else:
        p[0] = '<ul>' + p[1] + '</ul>'



def p_seli(p):
    '''seli : SELI factor cr
        | trul
    '''
    if len(p) == 4:
        p[0] = '<li>' + str(p[2]) + '</li>'
    else:
        p[0] = '<ul>' + p[1] + '</ul>'


def p_trul(p):
    '''trul : trul trli
        | trli
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_trli(p):
    '''trli : TRLI factor cr
    '''
    p[0] = '<li>' + str(p[2]) + '</li>'


def p_ol(p):
    '''ol : ol nli
        | nli
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_nli(p):
    '''nli : NLI factor cr
    | seul'''
    if len(p)==4:
        p[0] = '<li>' + str(p[2]) + '</li>'
    else:
        p[0] = '<ul>' + str(p[1]) + '</ul>'

def p_cr_T(p):
    '''cr : CR
    | T cr
    | cr CR
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

import ply.yacc as yacc
yacc.yacc()

if __name__ == '__main__':
    #filename = 'test03.md'
    if len(sys.argv) != 2:
        print "usage : run.py inputfilename"
        raise SystemExit 
    if len(sys.argv) == 2:
        yacc.parse(open(sys.argv[1]).read())
