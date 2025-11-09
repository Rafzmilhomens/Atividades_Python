escritorio = int(input('Digite a hora atual (formato 24h): '))

if(escritorio > 18):
    print('acesso negado')
elif(escritorio < 8):
    print('acesso negado')
else:
    print('bem-vinde, trabalhadore!')