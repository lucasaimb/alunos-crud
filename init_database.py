import sqlite3

# Conectar (ou criar) um banco de dados SQLite
conn = sqlite3.connect("src/alunos.db")
cursor = conn.cursor()

# Criar a tabela alunos
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    matricula INTEGER PRIMARY KEY,         -- Obrigatório e único
    nome TEXT NOT NULL,                    -- Obrigatório
    data_nascimento TEXT,                  -- Opcional (formato ISO: YYYY-MM-DD)
    curso TEXT                             -- Opcional
);
""")

# Confirmar as alterações e fechar a conexão
conn.commit()
conn.close()

print("Banco de dados e tabela 'alunos' criados com sucesso.")