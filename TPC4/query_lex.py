import ply.lex as lex
import os

# Lista de tokens reconhecidos
tokens = (
    'SELECT',
    'WHERE',
    'LIMIT',
    'VAR',
    'IDENTIFIER',
    'DOT',
    'STRING',
    'LBRACE',
    'RBRACE',
    'NUMBER'
)

t_SELECT = r'SELECT'
t_WHERE = r'WHERE'
t_LIMIT = r'LIMIT'
t_VAR = r'\?[a-zA-Z_]\w*'
t_IDENTIFIER = r'(?!SELECT|WHERE|LIMIT)[a-zA-Z_:][a-zA-Z0-9_:]*'
t_DOT = r'\.'
t_STRING = r'"[^"]*"'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_NUMBER = r'\d+'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f'Caractere ilegal: {t.value[0]}')
    t.lexer.skip(1)

# Criar o analisador léxico
lexer = lex.lex()

# Exemplo de uso
query = """
SELECT ?nome ?desc WHERE {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
"""

output_location = "outputs"
os.makedirs(output_location, exist_ok=True)
output_file = f"{output_location}/output.txt"
with open(output_file, "w") as file:
    lexer.input(query)
    while (r := lexer.token()):
        print(r)
        file.write(str(r) + "\n")