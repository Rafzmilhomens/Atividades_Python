
def idade():
   anos = atual - nascimento
   return anos

nascimento = int(input('Digite o ano de nascimento: '))
atual = int(input('Digite o ano atual: '))

print(f'A idade é igual {idade()} anos.')