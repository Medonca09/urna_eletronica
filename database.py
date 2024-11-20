import sqlite3

def conectar_banco():
    return sqlite3.connect("urna_eletronica.db")

def tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        numero INTEGER UNIQUE NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS votos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        candidato_id INTEGER NOT NULL,
        FOREIGN KEY (candidato_id) REFERENCES candidatos (id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS eleitores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        eleitor_id TEXT UNIQUE NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()