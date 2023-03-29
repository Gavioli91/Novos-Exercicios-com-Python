from src.manipulador_de_log import ManipuladorDeLog


class LogEmArquivo(ManipuladorDeLog):
    def log(self, mensagem):
        with open('data/log.txt', 'w') as file:
            file.write(mensagem)
