import re

class Token:
    def _init_(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

class analisador_lexico:
    def _init_(self, expressao):
        self.expressao = expressao
        self.posicao = 0
        self.tokens = []

    def analisar(self):
        while self.posicao < len(self.expressao):
            caractere = self.expressao[self.posicao]

            if caractere.isdigit():
                token = self.analisar_numero()
                self.tokens.append(token)
            elif caractere in ['+', '-', '*', '/']:
                token = Token(caractere, ' => OPERADOR')
                self.tokens.append(token)
                self.posicao += 1
            elif caractere == '(' or caractere == ')':
                token = Token(caractere, ' => PARENTESES')
                self.tokens.append(token)
                self.posicao += 1
            elif caractere.isspace():
                self.posicao += 1
            else:
                raise ValueError(f"Caractere inválido: {caractere}")

    def analisar_numero(self):
        padrao_numero = re.compile(r'\d+(\.\d+)?')
        match = padrao_numero.match(self.expressao[self.posicao:])
        numero = match.group()
        self.posicao += len(numero)
        
        if '.' in numero:
            return Token(float(numero), ' => NUMERO_REAL')
        else:
            return Token(int(numero), ' => NUMERO_INTEIRO')


expressao = input("Digite uma expressão: ")
analisador = analisador_lexico(expressao)
analisador.analisar()

for token in analisador.tokens:
    print(token.tipo, token.valor)