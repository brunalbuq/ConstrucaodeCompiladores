#Bruna de Albuquerque Medeiros RA:22009422
#Gustavo Lopes Urio Fonseca RA:22007103
#Yasmin Calixto Rodrigues RA:22008547

#Tabela de palavras reservadas
palavras_reservadas = {
    "SE": 1,
    "SENAO": 2,
    "ENQUANTO": 3,
    "+": 4,
    "-": 5,
    "/": 6,
    "*": 7,
    "(": 8,
    ")": 9,
    "E": 10,
    "OU": 11,
    "NÃO": 12,
    ">": 13,
    "<": 14,
    ">=": 15,
    "<=": 16,
    "=": 17,
    "<>": 18,
    "<-": 19,
    "->": 20,
}

#Função para verificar se um identificador é uma palavra reservada
def checar_reservadas(identificador):
    if identificador in palavras_reservadas:
        return palavras_reservadas[identificador]
    else:
        return -1

#Analisador léxico
def lexer(expressao):
    tokens = []  #Lista para armazenar os tokens
    tabela_simbolos = {}  #Tabela de símbolos
    posicao = 0  #Posição atual na entrada

    while posicao < len(expressao):
        char_atual = expressao[posicao]

        #Ignorar espaços em branco e caracteres de quebra de linha
        if char_atual.isspace():
            posicao += 1
            continue

        #Identificar números inteiros
        if char_atual.isdigit():
            num = ""
            while posicao < len(expressao) and expressao[posicao].isdigit():
                num += expressao[posicao]
                posicao += 1
            tokens.append(("INT", int(num)))
            continue
        
        #Identificar outros caracteres
        if char_atual in palavras_reservadas:
            tokens.append(("OPERATOR", char_atual, palavras_reservadas[char_atual]))
            posicao += 1
            continue


        #Identificar identificadores e palavras reservadas
        if char_atual.isalpha():
            identificador = ""
            while posicao < len(expressao) and (expressao[posicao].isalpha() or expressao[posicao].isdigit()):
                identificador += expressao[posicao]
                posicao += 1

            #Verificar se é uma palavra reservada
            cod_reservado = checar_reservadas(identificador)
            if cod_reservado != -1:
                tokens.append(("RESERVADO", cod_reservado))
            else:
                #Se não for uma palavra reservada, é um identificador
                if identificador not in tabela_simbolos:
                    tabela_simbolos[identificador] = len(tabela_simbolos) + 1
                tokens.append(("ID", tabela_simbolos[identificador]))

            continue

        #Identificar outros caracteres
        #Adicione aqui outras regras para identificação de tokens

        posicao += 1

    #Adicionar token de final de arquivo
    tokens.append(("End of File", 0))

    return (tokens, tabela_simbolos)

#Função main para testar o analisador léxico
def main():
    expressao = input("Digite a expressão: ")

    result = lexer(expressao)
    tokens = result[0]
    tabela_simbolos = result[1]

    #Exibir os tokens e suas posições na tabela
    for token in tokens:
        if token[1] in palavras_reservadas:
            print(f"Token: {token[0]} ' {token[1]} ', na Posição: {token[2]}\n")
        else:
            print("Token:", token[0], ", Valor:", token[1],"\n")


if __name__ == "__main__":
    main()