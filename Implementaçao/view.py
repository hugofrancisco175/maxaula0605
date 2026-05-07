class SessaoView:

    def __init__(self, controller):
        self.controller = controller

    def menu(self):

        print("=== Sistema Rede de Cinemas ===")

        id_sessao = int(input("Informe o ID da sessão: "))
        publico = int(input("Informe o público: "))

        resultado = self.controller.registrar_publico(
            id_sessao,
            publico
        )

        print(resultado)
