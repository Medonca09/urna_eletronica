import sqlite3

conexao = sqlite3.connect('urna_eletronica.db')
cursor = conexao.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()
print("Tabelas disponíveis:", tabelas)

cursor.execute("SELECT * FROM votos;")
dados = cursor.fetchall()

for linha in dados:
    print(linha)

conexao.close()
