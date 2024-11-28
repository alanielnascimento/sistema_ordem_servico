import sqlite3

def criar_banco():
    # Conectar ao banco de dados (será criado se não existir)
    conn = sqlite3.connect('ordem_servico.db')
    cursor = conn.cursor()

    # Criar as tabelas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tecnicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        contato TEXT NOT NULL,
        especializacao TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf_cnpj TEXT NOT NULL,
        email TEXT,
        telefone TEXT,
        endereco TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tipos_servico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_servico TEXT NOT NULL,
        descricao TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ordens_servico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        tecnico_id INTEGER,
        tipo_servico_id INTEGER,
        descricao_servico TEXT,
        observacoes TEXT,
        valor_servico REAL,
        status TEXT,
        data_criacao TEXT,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id),
        FOREIGN KEY (tecnico_id) REFERENCES tecnicos(id),
        FOREIGN KEY (tipo_servico_id) REFERENCES tipos_servico(id)
    );
    ''')

    # Commit e fechar a conexão
    conn.commit()
    conn.close()

# Chamar a função para criar o banco de dados
criar_banco()
