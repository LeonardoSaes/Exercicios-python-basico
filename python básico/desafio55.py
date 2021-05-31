# pergunta o sexo da pessoa e válida
sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmF':
    sexo = str(input('Dados inválidos, Por favor, informe o seu sexo [M/F]:')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
print('FIM')
