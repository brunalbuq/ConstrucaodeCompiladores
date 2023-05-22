def analisador_caracteres():
  entrada = input("Entrada: ")

  #Desmembrando uma string em múltiplas strings através de um separador passando no parâmetro, retornando todas em uma lista.
  nova_entrada = entrada.split(' ')

  contador_caracteres = 0
  contador_espaco = 0

  #Contagem dos caracteres e espaços em branco
  for i in range(len(entrada)):
    if entrada[i] != ' ':
      contador_caracteres += 1
    else:
      contador_espaco += 1

  print("1. - Total de caracteres encontrados:", contador_caracteres)
  print("2. - Total de espaços em branco encontrados:", contador_espaco)
  print("3. - Total de caracteres com espaços em branco encontrados:", contador_caracteres + contador_espaco)
  
  #Printando a lista da entrada sem nenhum espaço
  print("4. - Saída na tela sem os espaços em branco: ", ''.join(nova_entrada) )
  
analisador_caracteres()