from Back.Conta import Conta_de_usuario, Verificacao


while True:
    try:
        Usuario = input("Digite seu nome de usuario: ")
        Senha = input("Digite sua senha: ")

        Verificacao(Usuario, Senha)

    except KeyboardInterrupt:
        print("Operação cancelada pelo usuario")
        break
    except:
        print("Ocorreu um erro, tente novamente")

input("Pressione Enter para fechar...")