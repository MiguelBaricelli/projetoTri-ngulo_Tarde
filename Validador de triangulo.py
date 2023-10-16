# validador do triangulo

# apresentação
# Um trabalho muito bom - Gilberto
print('            -- validador de triangulo   ')

# Entrada

a = int(input('LADO A'))
b = int(input('LADO B'))
c = int(input('LADO C'))

#Processamento e saida
if a < (b + c) and b < (a + c) and c < (a + b):
    print('\n{}, {} e {} formam um triangulo'.format(a,b,c))
else:
    print('\n{}, {} e {}, não formam triangulo'.format(a,b,c))

