def validacao_email(email):
    return email[-8:] == "@puc.com"
print (validacao_email("oliveiradev@puc.com"))

def validacao_senha(senha):
    check_tamanho = len(senha) >= 8
    check_maiuscula = possuiMaiuscula(senha)
    check_minuscula = possuiMinuscula(senha)
    check_numero = possuiNumero(senha)

def possuiMaiuscula(palavra):
    for letra in palavra:
        if 'A' <= letra <= 'Z':
            return True
    return False ### Porque eu preciso verificar todo o for até o final da palavra

def possuiMinuscula(palavra):
    for letra in palavra:
        if 'a' <= letra <= 'z':
            return True
    return False ### Porque eu preciso verificar todo o for até o final da palavra

def possuiNumero(palavra):
    for caracter in palavra:
       if '0' <= caracter <= '9':
          return True
    return False ### Porque eu preciso verificar todo o for até o final da palavra

print (validacao_senha("oliveira123"))