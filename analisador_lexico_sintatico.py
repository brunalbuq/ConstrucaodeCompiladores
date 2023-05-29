import re

#Função para receber a expressão de inicio para análise.
def codigo_entrada():
    expressao = input("Digite o código fonte da expressão: ")
    return expressao


#Função que recebe a expressão e filtra os tokens dela.
def ver_caracter(expressao):
    tokens = re.findall(r'\b\w+\b|[+\-*/=]|[()]', expressao)
    return tokens


#Função para criar tabela de apresentação léxica da expressao recebida.
def crie_tabela_simbolos(tokens):
    tabela_simbolos = {}
    for token in tokens:
        if token not in tabela_simbolos:
            if token.isnumeric():
                tipo = "Número"
            elif re.match(r'^[a-zA-Z]+$', token):
                tipo = "Identificador"

            elif token in "+-*/=":
                if token == "+":
                    tipo = "Operador aritmético de Soma"
                elif token == "-":
                    tipo = "Operador aritmético de Subtração"
                elif token == "*":
                    tipo = "Operador aritmético de Multiplicação"
                elif token == "/":
                    tipo = "Operador aritmético de Divisão"
                else:
                    tipo = "Operador de atribuição"
                
            elif token in "()":
                tipo = "Delimitador"
            else:
                tipo = "Desconhecido"
            tabela_simbolos[token] = tipo
    return tabela_simbolos

def identifique_tokens(tabela_simbolos):
    print("Tokens encontrados:")
    for token, tipo in tabela_simbolos.items():
        print("Token:", token, "\tTipo:", tipo)


#Função para verificar erros de sintatica , retornando erros de escrita e caso tenha 4 ou mais símbolos de atribuição.
def ver_erros_sintaticos(tokens):
    for i in range(len(tokens)-1):
        if (tokens[i].isnumeric() or re.match(r'^[a-zA-Z]+$', tokens[i])) and \
                (tokens[i+1].isnumeric() or re.match(r'^[a-zA-Z]+$', tokens[i+1])):
            print(f"Erro sintático: dois operandos consecutivos sem separação. {tokens[i]} e {tokens[i+1]}")
        elif tokens[i] in "+-*/" and tokens[i+1] in "+-*/":
            print(f"Erro sintático: dois operadores consecutivos sem separação. {tokens[i]} e {tokens[i+1]}")
    if "=" in tokens:
        index = tokens.index("=")
        if len(tokens) < index + 4:
            print("Erro sintático: expressão após o símbolo de atribuição contém mais de três operandos ou operadores.")


#Função 'MAIN' puxando outros defs.
def analisador_lexico_sintatico():
    expressao = codigo_entrada()
    tokens = ver_caracter(expressao)
    tabela_simbolos = crie_tabela_simbolos(tokens)
    identifique_tokens(tabela_simbolos)
    ver_erros_sintaticos(tokens)

if __name__ == "__main__":
    analisador_lexico_sintatico()