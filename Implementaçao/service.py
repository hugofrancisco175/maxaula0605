class SessaoService:

    def __init__(self, repository):
        self.repository = repository

    def registrar_publico(self, id_sessao, publico):

        sessao = self.repository.buscar_sessao(id_sessao)

        if sessao is None:
            return "Sessão não encontrada."

        capacidade = sessao[2]

        if publico > capacidade:
            return "O público não pode ultrapassar a capacidade."

        self.repository.atualizar_publico(id_sessao, publico)

        return "Público registrado com sucesso."
