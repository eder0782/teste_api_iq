from api_iq.app import api_iq as api_iq




while True:
    valor = int(input('digite 1 para conectar, 2 para pegar balanco, 3 mudar conta, 4 desconectar, 5 sair:'))
    if valor==1:
        email= input('email: ')
        senha = input('senha: ')
        print('Conectado: '+ str(api.conectar(email,senha)))
        continue
    elif valor==2:
        print(api.pegar_balanco())
        continue
    elif valor==3:
        conta=input('Usar conta:')
        print('Mudou conta ==' + str(api.alterar_conta(conta.upper())))

    elif valor == 4:
        print('Deconetado ==' + str(api.desconectar()))      

    else:
        break    
        





