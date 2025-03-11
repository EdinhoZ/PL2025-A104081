import json
import ply.lex as lex

# Carregar o stock inicial
def carregar_stock():
    try:
        with open("stock.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_stock(stock):
    with open("stock.json", "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4, ensure_ascii=False)

# Tokens do analisador léxico
tokens = (
    'LISTAR', 'MOEDA', 'SELECIONAR', 'SAIR',
    'CODIGO', 'VALOR', 'PONTO'
)

t_LISTAR = r'LISTAR'
t_MOEDA = r'MOEDA'
t_SELECIONAR = r'SELECIONAR'
t_SAIR = r'SAIR'
t_CODIGO = r'[A-Z][0-9]+'
t_VALOR = r'(2e|1e|50c|20c|10c|5c|2c|1c)'
t_PONTO = r'\.'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Função principal da máquina
def vending_machine():
    stock = carregar_stock()
    saldo = 0
    moedas = {'2e': 200, '1e': 100, '50c': 50, '20c': 20, '10c': 10, '5c': 5, '2c': 2, '1c': 1}

    print("maq: Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    while True:
        entrada = input(">> ")
        lexer.input(entrada)
        tokens_list = list(lexer)
        if not tokens_list:
            continue

        comando = tokens_list[0].type
        
        if comando == 'LISTAR':
            print("maq:")
            print(f"{'cod'.ljust(6)} | {'nome'.ljust(20)} | {'quantidade'.ljust(10)} | {'preço'}")
            print("-" * 50)
            for item in stock:
                print(f"{item['cod'].ljust(6)} | {item['nome'].ljust(20)} | {str(item['quant']).ljust(10)} | {item['preco']}e")
        
        elif comando == 'MOEDA':
            for token in tokens_list[1:]:
                if token.type == 'VALOR':
                    saldo += moedas[token.value]
            print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c")
        
        elif comando == 'SELECIONAR':
            if len(tokens_list) < 2 or tokens_list[1].type != 'CODIGO':
                print("maq: Código inválido.")
                continue
            codigo = tokens_list[1].value
            produto = next((item for item in stock if item['cod'] == codigo), None)
            
            if not produto:
                print("maq: Produto inexistente.")
            elif produto['quant'] == 0:
                print("maq: Produto esgotado.")
            elif saldo < produto['preco'] * 100:
                print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c; Pedido = {int(produto['preco'] * 100)}c")
            else:
                saldo -= int(produto['preco'] * 100)
                produto['quant'] -= 1
                print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
                print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c")
        
        elif comando == 'SAIR':
            troco = saldo
            troco_devolvido = {}
            for moeda, valor in sorted(moedas.items(), key=lambda x: -x[1]):
                while troco >= valor:
                    troco -= valor
                    if moeda in troco_devolvido:
                        troco_devolvido[moeda] += 1
                    else:
                        troco_devolvido[moeda] = 1
            
            print("maq: Pode retirar o troco:", ", ".join([f"{v}x {k}" for k, v in troco_devolvido.items()]))
            print("maq: Até à próxima")
            salvar_stock(stock)
            break

if __name__ == "__main__":
    vending_machine()