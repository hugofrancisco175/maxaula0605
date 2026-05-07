from database import conectar

class SessaoRepository:

    def buscar_sessao(self, id_sessao):

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM sessao WHERE id = ?",
            (id_sessao,)
        )

        sessao = cursor.fetchone()

        conexao.close()

        return sessao

    def atualizar_publico(self, id_sessao, publico):

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "UPDATE sessao SET publico = ? WHERE id = ?",
            (publico, id_sessao)
        )

        conexao.commit()
        conexao.close()
