import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('ordem_servico.db')
cursor = conn.cursor()

# Consultar as tabelas no banco de dados
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

# Exibir as tabelas encontradas
print("Tabelas no banco de dados:")
for tabela in tabelas:
    print(tabela[0])

# Fechar a conexão
conn.close()
