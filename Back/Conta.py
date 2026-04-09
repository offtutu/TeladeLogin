def Conta_de_usuario():
    usuario = "Kotoshi"
    senha = "Bungas"
    return usuario, senha


def Verificacao(usuario_digitado, senha_digitada):
    Usuario_correto, Senha_correta = Conta_de_usuario()
    if usuario_digitado == Usuario_correto and senha_digitada == Senha_correta:
        print("Nome de usuario correto")
        print("Senha correta")
        return True
    print("Senha ou usuario incorreto")
    return False
