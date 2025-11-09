## Transforma o input em string e conta seus caracteres.

def contador(numeros):
    contagem = str(numeros)
    return len(contagem)

## Input do usuário

cpf = input('Digite seu C.P.F.: ')

## Processamento e validação do dado

if not cpf.isdigit():
    print('Digite apenas números!')
elif contador(cpf) < 11:
    print('O C.P.F. precisa ter 11 dígitos!')
elif contador(cpf) > 11:
    print('O C.P.F. precisa ser 11 dígitos!')
else:
    print('C.P.F. Válido!')
    
