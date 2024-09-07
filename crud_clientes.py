import sqlite3

# Conectando ao banco de dados SQLite (cria o arquivo se não existir)
conn = sqlite3.connect('clientes_loja.db')
cursor = conn.cursor()


# Função para criar a tabela de clientes
def criar_tabela():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        idade INTEGER,
        historico_compras TEXT
    )
    ''')
    conn.commit()


# Função para adicionar um novo cliente (CREATE)
def adicionar_cliente(nome, email, idade, historico_compras):
    cursor.execute('''
    INSERT INTO clientes (nome, email, idade, historico_compras) 
    VALUES (?, ?, ?, ?)
    ''', (nome, email, idade, historico_compras))
    conn.commit()


# Função para listar todos os clientes (READ)
def listar_clientes():
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)


# Função para atualizar dados de um cliente (UPDATE)
def atualizar_cliente(id, nome, email, idade, historico_compras):
    cursor.execute('''
    UPDATE clientes SET nome = ?, email = ?, idade = ?, historico_compras = ?
    WHERE id = ?
    ''', (nome, email, idade, historico_compras, id))
    conn.commit()


# Função para deletar um cliente (DELETE)
def deletar_cliente(id):
    cursor.execute('''
    DELETE FROM clientes WHERE id = ?
    ''', (id,))
    conn.commit()


# Função para mostrar o menu
def menu():
    print("\nMenu:")
    print("1. Adicionar cliente")
    print("2. Listar clientes")
    print("3. Atualizar cliente")
    print("4. Deletar cliente")
    print("5. Sair")


# Inicialização da tabela
criar_tabela()

# Loop principal do programa
while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome = input("Nome do cliente: ")
        email = input("Email do cliente: ")
        idade = int(input("Idade do cliente: "))
        historico_compras = input("Histórico de compras: ")
        adicionar_cliente(nome, email, idade, historico_compras)
        print("Cliente adicionado com sucesso!")

    elif escolha == '2':
        listar_clientes()

    elif escolha == '3':
        id = int(input("ID do cliente a ser atualizado: "))
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        idade = int(input("Nova idade: "))
        historico_compras = input("Novo histórico de compras: ")
        atualizar_cliente(id, nome, email, idade, historico_compras)
        print("Cliente atualizado com sucesso!")

    elif escolha == '4':
        id = int(input("ID do cliente a ser deletado: "))
        deletar_cliente(id)
        print("Cliente deletado com sucesso!")

    elif escolha == '5':
        print("Saindo...")
        break

    else:
        print("Opção inválida, tente novamente.")

# Fechando a conexão com o banco de dados
conn.close()
