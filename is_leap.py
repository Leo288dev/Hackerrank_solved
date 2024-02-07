
def is_leap(ano):

    if ano < 2000 and (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
        return True
    elif ano >= 2000 and ano % 400 == 0:
        return True
    else:
        return False



ano = int(input('ano'))
print(is_leap(ano))


# ANO BISSEXTO - se o ano for dividido igualmente por 4 é bissexto
# se o ano pode ser dividido igualmente por 100 e por 400 então é bissexto
# caso contrário não é bissexto
