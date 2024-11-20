from database import conectar_banco

def registrar_candidato(nome, cargo, numero):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
        INSERT INTO candidatos (nome, cargo, numero) 
        VALUES (?, ?, ?)
        """, (nome, cargo, numero))
        conexao.commit()
    except Exception as e:
        print(f"Erro ao registrar candidato: {e}")
    finally:
        conexao.close()

def listar_candidatos():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT id, nome, cargo, numero 
    FROM candidatos
    """)
    candidatos = cursor.fetchall()
    conexao.close()
    return candidatos

def buscar_candidato_por_numero(numero):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT id 
    FROM candidatos 
    WHERE numero = ?
    """, (numero,))
    candidato = cursor.fetchone()
    conexao.close()
    return candidato[0] if candidato else None

def registrar_eleitor(eleitor_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
        INSERT INTO eleitores (eleitor_id) 
        VALUES (?)
        """, (eleitor_id,))
        conexao.commit()
    except Exception as e:
        print(f"Erro ao registrar eleitor: {e}")
    finally:
        conexao.close()

def verificar_eleitor(eleitor_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT id 
    FROM eleitores 
    WHERE eleitor_id = ?
    """, (eleitor_id,))
    eleitor = cursor.fetchone()
    conexao.close()
    return eleitor is not None

def registrar_voto(candidato_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
        INSERT INTO votos (candidato_id) 
        VALUES (?)
        """, (candidato_id,))
        conexao.commit()
    except Exception as e:
        print(f"Erro ao registrar voto: {e}")
    finally:
        conexao.close()

def contar_votos():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT candidatos.nome, candidatos.numero, COUNT(votos.id) as total_votos
    FROM candidatos
    LEFT JOIN votos ON candidatos.id = votos.candidato_id
    GROUP BY candidatos.id
    ORDER BY total_votos DESC
    """)
    resultados = cursor.fetchall()
    conexao.close()
    return resultados
