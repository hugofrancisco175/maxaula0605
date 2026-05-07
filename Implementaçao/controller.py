class SessaoController:

    def __init__(self, service):
        self.service = service

    def registrar_publico(self, id_sessao, publico):

        return self.service.registrar_publico(
            id_sessao,
            publico
        )
