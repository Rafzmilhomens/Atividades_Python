peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))

IMC = peso/(altura**2)

print(f'Seu IMC é igual a {IMC}')

if(IMC >= 18.5 and IMC <=25):
    print('Peso normal.')
elif(IMC < 18.5):
    print('Você está abaixo do peso')
elif(IMC > 25):
    print('Você está acima do peso')