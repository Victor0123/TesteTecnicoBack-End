inicio = int(input('Digite um numero: '))
fim = int(input('Digite um numero: '))

def e_primo(numero):
    if numero == 2:
        return True

    primo = False
    if numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break
            else:
                primo = True

    return primo

for i in range(inicio, fim + 1):
    if e_primo(i):
        print(i, end = ' ')
