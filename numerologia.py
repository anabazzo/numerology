from re import sub

def remove_caract_espec(nome):
  novo_nome = sub(r'[ãáàâä]', 'a', nome)
  novo_nome = sub(r'[õóòôö]', 'o', novo_nome)
  return novo_nome

def calcula_nome(nome):
  alfabeto = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 1,
    'k': 2,
    'l': 3,
    'm': 4,
    'n': 5,
    'o': 6,
    'p': 7,
    'q': 8,
    'r': 9,
    's': 1,
    't': 2,
    'u': 3,
    'v': 4,
    'w': 5,
    'x': 6,
    'y': 7,
    'z': 8
  }

  nome_valido = remove_caract_espec(nome)

  nome_completo = list(nome_valido)

  soma = 0

  for letra in nome_completo: 
    soma = soma + alfabeto.get(letra, 0)


  return soma
