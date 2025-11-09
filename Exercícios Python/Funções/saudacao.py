
def horario(atual):
    if atual < 12:
       return 'bom dia!'
    elif atual < 18:
        return 'boa tarde!'
    else:
        return 'boa noite!'

atualidade = int(input('Digite a hora atual (0-23): '))

print(horario(atualidade))