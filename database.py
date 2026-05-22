import sqlite3

def conectar():
    return sqlite3.connect("filmes.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS FILMES (
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   TITULO TEXT NOT NULL,
                   ANO INTEGER,
                   GENERO TEXT NOT NULL,
                   DIRETOR TEXT NOT NULL,
                   NOTA REAL
                   )
            """)
    conexao.commit()
    conexao.close()

def adicionar_filme(TITULO, ANO, GENERO, DIRETOR, NOTA):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    INSERT INTO FILMES (TITULO, ANO, GENERO, DIRETOR, NOTA)
    VALUES (?, ?, ?, ?, ?)
    """, (TITULO, ANO, GENERO, DIRETOR, NOTA))
    conexao.commit()
    conexao.close()

def listar_filmes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM FILMES")
    FILMES = cursor.fetchall()
    conexao.close()
    return FILMES

def remover_filme(ID):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM FILMES WHERE ID = ?", (ID,))
    conexao.commit()
    conexao.close()

def buscar_filme_por_titulo(TITULO):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM FILMES WHERE TITULO LIKE ?", ('%' + TITULO + '%',))
    FILMES = cursor.fetchall()
    conexao.close()
    return FILMES

def filtrar_filmes(GENERO=None, NOTA_MIN=None, DIRETOR=None):
    conexao = conectar()
    cursor = conexao.cursor()
    query = "SELECT * FROM FILMES WHERE 1=1"
    parametros = []
    
    if GENERO:
        query += " AND GENERO = ?"
        parametros.append(GENERO)
    
    if NOTA_MIN is not None:
        query += " AND NOTA >= ?"
        parametros.append(NOTA_MIN)
    
    if DIRETOR:
        query += " AND DIRETOR = ?"
        parametros.append(DIRETOR)
    
    cursor.execute(query, tuple(parametros))
    FILMES = cursor.fetchall()
    conexao.close()
    return FILMES