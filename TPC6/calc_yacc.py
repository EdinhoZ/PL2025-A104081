import ply.yacc as yacc
import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN'
)

# Regras para os tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    raise SyntaxError(f"Caractere inválido: {t.value[0]}")

# Construção do analisador léxico
lexer = lex.lex()

# Regras da gramática

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    if p[3] == 0:
        raise ZeroDivisionError("Divisão por zero")
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    raise SyntaxError("Erro de sintaxe")

# Construção do analisador sintático
parser = yacc.yacc()

def evaluate(expression):
    return parser.parse(expression, lexer=lexer)

# Exemplos de uso:
print(evaluate("2+3"))  # Saída: 5
print(evaluate("67-(2+3*4)"))  # Saída: 53
print(evaluate("(9-2)*(13-4)"))  # Saída: 63