import sqlite3

# Consultar e exibir os dados inseridos
def consultar_dados():
    conn = sqlite3.connect('ordem_servico.db')
    cursor = conn.cursor()

    # Consultar clientes
    cursor.execute("SELECT * FROM clientes;")
    clientes = cursor.fetchall()
    print("Clientes cadastrados:")
    for cliente in clientes:
        print(cliente)

    # Consultar técnicos
    cursor.execute("SELECT * FROM tecnicos;")
    tecnicos = cursor.fetchall()
    print("\nTécnicos cadastrados:")
    for tecnico in tecnicos:
        print(tecnico)

    conn.close()

# Chamar a função para consultar os dados
consultar_dados()
