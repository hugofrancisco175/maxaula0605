import sqlite3

def conectar():
    return sqlite3.connect("cinema.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filme TEXT NOT NULL,
        capacidade INTEGER NOT NULL,
        publico INTEGER DEFAULT 0
    )
    """)

    cursor.execute("SELECT COUNT(*) FROM sessao")
    total = cursor.fetchone()[0]

    if total == 0:
        cursor.execute("""
        INSERT INTO sessao (filme, capacidade, publico)
        VALUES ('Homem-Aranha', 100, 0)
        """)

    conexao.commit()
    conexao.close()
