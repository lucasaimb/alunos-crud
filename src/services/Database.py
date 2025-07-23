import sqlite3
from ctypes import memset

DB = r'C:\PythonProjects\APIS\alunos-crud\src\alunos.db'
def adicionar_aluno(matricula: int, nome: str, data_nascimento: str = None, curso: str = None):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO alunos (matricula, nome, data_nascimento, curso)
            VALUES (?, ?, ?, ?)
        """, (matricula, nome, data_nascimento, curso))
        conn.commit()
        return f"Aluno {nome} adicionado com sucesso."
    except sqlite3.IntegrityError as e:
        return f"Erro ao adicionar aluno: {e}"
    finally:
        conn.close()


def buscar_aluno(matricula: int):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos WHERE matricula = ?", (matricula,))
    aluno = cursor.fetchone()

    conn.close()
    if aluno:
        return {
            "matricula": aluno[0],
            "nome": aluno[1],
            "data_nascimento": aluno[2],
            "curso": aluno[3]
        }
    else:
        print(f"Nenhum aluno encontrado com matrícula {matricula}.")
        return None


def listar_alunos():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    conn.close()

    # Transforma em uma lista de dicionários
    lista = [
        {
            "matricula": aluno[0],
            "nome": aluno[1],
            "data_nascimento": aluno[2],
            "curso": aluno[3]
        }
        for aluno in alunos
    ]

    return lista


def deletar_aluno(matricula: int):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM alunos WHERE matricula = ?", (matricula,))
    conn.commit()
    if cursor.rowcount > 0:
        mensagem = f"Aluno com matrícula {matricula} deletado com sucesso."
    else:
        mensagem = f"Nenhum aluno encontrado com matrícula {matricula}."
    conn.close()
    return mensagem
