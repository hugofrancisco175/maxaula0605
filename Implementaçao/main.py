from database import criar_tabela
from repository import SessaoRepository
from service import SessaoService
from controller import SessaoController
from view import SessaoView

def main():

    criar_tabela()

    repository = SessaoRepository()

    service = SessaoService(repository)

    controller = SessaoController(service)

    view = SessaoView(controller)

    view.menu()

if __name__ == "__main__":
    main()
