class Log:
    def __init__(self, manipuladores):
        self.__manipuladores = set(manipuladores)

    def adicionar_manipulador(self, manipulador):
        self.__manipuladores.add(manipulador)

    def info(self, mensagem):
        self.__log('info', mensagem)

    def alerta(self, mensagem):
        self.__log('alerta', mensagem)

    def erro(self, mensagem):
        self.__log('erro', mensagem)

    def debug(self, mensagem):
        self.__log('debug', mensagem)

    def __log(self, nivel, mensagem):
        for manipulador in self.__manipuladores:
            manipulador.log(self.__formatar(nivel, mensagem))

    def __formatar(self, nivel, mensagem):
        return f'[{nivel} - data]: {mensagem}'
