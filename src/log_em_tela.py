from src.manipulador_de_log import ManipuladorDeLog


class LogEmTela(ManipuladorDeLog):
    def log(self, mensagem):
        print(mensagem)
