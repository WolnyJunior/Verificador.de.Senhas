while True:
    print('**Cadastrar novo Login e Senha**\n')
    criar = int(input('Criar novo Login e Senha.\n(1)SIM \n(2)NÃO\n'))
    if criar == 1:
        login = input('Digite o Login de Usuário:\n')
        print('Usuário Válido\n')
        print('Para criar uma senha forte, deve se utilizar ao menos:\n1 Caractere Especial(!,@,#,$,%,^,&,*,(,),-,+)\n1 Dígito(0 a 9)\n1 Letra MAIÚSCULA\n1 Letra minúscula\n6 Caracteres\n')

        while True:
            especial = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+')
            caractereespecial = input('Digite um caractere especial:\n!,@,#,$,%,^,&,*,(,),-,+\n')
            if caractereespecial not in (especial):
                print('Caractere Inválido\n')
                continue
            if caractereespecial in(especial):
                print('Caractere Válido\n')
                break
        while True:
            digitos1 = ('0','1','2','3','4','5','6','7','8','9')
            digito = input('Digite um Dígito: \n0 a 9.\n')
            if digito not in (digitos1):
                print('Número Inválido.\nTente um número de 0 á 9\n')
                continue
            if digito in (digitos1):
                print('Número Válido.\n')
                break
        while True:
            maiusculas = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ç')
            maiuscula = input('Digite um caractere \n"MAIÚSCULO".\n')
            if maiuscula not in (maiusculas):
                print('Caractere Inválido.\n')
                continue
            if maiuscula in (maiusculas):
                print('Caractere Válido.\n')
                break
        while True:
            minusculas = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ç')
            minuscula = input('Digite um caractere \n"minúsculo".\n')
            if minuscula not in (minusculas):
                print('Caractere Inválido.\n')
                continue
            if minuscula in (minusculas):
                print('Caractere Válido.\n')
                break
        for i in range(1):
            caracteres = input('Para fortalecer ainda mais sua senha.\nDigite um ou mais caracteres.\n')
            caracteres2 = input('Digite um ou mais caracteres para finalizar sua senha.\n')
            print(caracteres)
        digitos = str(digito)
        print('Senha forte criada com SUCESSO!\n')
        senha = (caractereespecial + digitos + (maiuscula.upper()) + (minuscula.lower()) + caracteres + caracteres2 )
        print('Login: {}\nSenha: {}\n'.format(login,senha))
    elif criar == 2:
        print('Encerrando o programa.')
        break