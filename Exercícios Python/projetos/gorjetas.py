valorTotal = float(input('Digite o valor da conta: '))
gorgeta = float(input('Digite a porcentagem da gorgeta: '))

def porcentagemDaGorgeta (valor):
    return valor/100

def calculoDaGorgeta(pagar):
    return pagar * porcentagemDaGorgeta()

valorDaGorgeta = porcentagemDaGorgeta(gorgeta) * valorTotal

totalAPagar = valorTotal + valorDaGorgeta

print(f'Valor da Gorgeta: R$ {valorDaGorgeta}.')
print(f'Total a pagar: R$ {totalAPagar}')