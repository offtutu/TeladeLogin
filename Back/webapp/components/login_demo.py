from django_unicorn.components import UnicornView

from Conta import Verificacao


class LoginDemoView(UnicornView):
    usuario = ""
    senha = ""
    mensagem = ""

    def entrar(self):
        if Verificacao(self.usuario, self.senha):
            self.mensagem = "Login realizado com sucesso."
        else:
            self.mensagem = "Usuario ou senha incorretos."
