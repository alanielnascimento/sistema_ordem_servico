import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para cadastrar clientes
def cadastrar_cliente():
    nome = entry_nome.get()
    cpf_cnpj = entry_cpf_cnpj.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()

    # Conectar ao banco de dados e inserir dados do cliente
    conn = sqlite3.connect('ordem_servico.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO clientes (nome, cpf_cnpj, email, telefone, endereco)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, cpf_cnpj, email, telefone, endereco))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    entry_nome.delete(0, tk.END)
    entry_cpf_cnpj.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)

# Função para cadastrar técnicos
def cadastrar_tecnico():
    nome = entry_nome_tecnico.get()
    contato = entry_contato_tecnico.get()
    especializacao = entry_especializacao.get()

    # Conectar ao banco de dados e inserir dados do técnico
    conn = sqlite3.connect('ordem_servico.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO tecnicos (nome, contato, especializacao)
    VALUES (?, ?, ?)
    ''', (nome, contato, especializacao))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Técnico cadastrado com sucesso!")
    entry_nome_tecnico.delete(0, tk.END)
    entry_contato_tecnico.delete(0, tk.END)
    entry_especializacao.delete(0, tk.END)

# Configuração da janela principal
window = tk.Tk()
window.title("Cadastro de Clientes e Técnicos")

# Tela de cadastro de clientes
frame_cliente = tk.LabelFrame(window, text="Cadastro de Cliente", padx=10, pady=10)
frame_cliente.pack(padx=10, pady=10)

# Campos do formulário de clientes
tk.Label(frame_cliente, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(frame_cliente)
entry_nome.grid(row=0, column=1)

tk.Label(frame_cliente, text="CPF/CNPJ:").grid(row=1, column=0)
entry_cpf_cnpj = tk.Entry(frame_cliente)
entry_cpf_cnpj.grid(row=1, column=1)

tk.Label(frame_cliente, text="E-mail:").grid(row=2, column=0)
entry_email = tk.Entry(frame_cliente)
entry_email.grid(row=2, column=1)

tk.Label(frame_cliente, text="Telefone:").grid(row=3, column=0)
entry_telefone = tk.Entry(frame_cliente)
entry_telefone.grid(row=3, column=1)

tk.Label(frame_cliente, text="Endereço:").grid(row=4, column=0)
entry_endereco = tk.Entry(frame_cliente)
entry_endereco.grid(row=4, column=1)

tk.Button(frame_cliente, text="Cadastrar Cliente", command=cadastrar_cliente).grid(row=5, column=0, columnspan=2)

# Tela de cadastro de técnicos
frame_tecnico = tk.LabelFrame(window, text="Cadastro de Técnico", padx=10, pady=10)
frame_tecnico.pack(padx=10, pady=10)

# Campos do formulário de técnicos
tk.Label(frame_tecnico, text="Nome:").grid(row=0, column=0)
entry_nome_tecnico = tk.Entry(frame_tecnico)
entry_nome_tecnico.grid(row=0, column=1)

tk.Label(frame_tecnico, text="Contato:").grid(row=1, column=0)
entry_contato_tecnico = tk.Entry(frame_tecnico)
entry_contato_tecnico.grid(row=1, column=1)

tk.Label(frame_tecnico, text="Especialização:").grid(row=2, column=0)
entry_especializacao = tk.Entry(frame_tecnico)
entry_especializacao.grid(row=2, column=1)

tk.Button(frame_tecnico, text="Cadastrar Técnico", command=cadastrar_tecnico).grid(row=3, column=0, columnspan=2)

# Iniciar a interface gráfica
window.mainloop()
