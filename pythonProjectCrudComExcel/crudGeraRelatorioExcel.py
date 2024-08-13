import sqlite3
import pandas as pd

def connect_db():
    conn = sqlite3.connect('my_database.db')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL
        )
        '''
    )
    conn.commit()
    conn.close()

# Função para criar um cliente
def add_customer():
    name = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    age = int(input("Digite a idade do cliente: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO customers (name, email, age) VALUES (?, ?, ?)', (name, email, age))
    conn.commit()
    conn.close()
    print("Cliente adicionado com sucesso!")

# Função para listar clientes
def list_customers():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print("Lista de Clientes:")
        for row in rows:
            print(row)
    else:
        print("Nenhum cliente cadastrado.")

# Função para atualizar cliente
def update_customer():
    customer_id = int(input("Digite o ID do cliente a ser atualizado: "))
    name = input("Digite o novo nome do cliente: ")
    email = input("Digite o novo email do cliente: ")
    age = int(input("Digite a nova idade do cliente: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE customers SET name = ?, email = ?, age = ? WHERE id = ?', (name, email, age, customer_id))
    conn.commit()
    conn.close()
    print("Cliente atualizado com sucesso!")

# Função para deletar cliente
def delete_customer():
    customer_id = int(input("Digite o ID do cliente a ser excluído: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM customers WHERE id = ?', (customer_id,))
    conn.commit()
    conn.close()
    print("Cliente excluído com sucesso!")

# Função para gerar relatório
def generate_report():
    try:
        # Conexão com o banco de dados
        conn = connect_db()

        # Realiza a consulta para obter todos os dados da tabela customers
        query = 'SELECT * FROM customers'
        df = pd.read_sql_query(query, conn)

        # Pede ao usuário o nome do arquivo com a extensão .xlsx
        filename = input("Digite o nome do arquivo Excel (ex: report.xlsx): ")

        # Salva os dados no arquivo Excel
        df.to_excel(filename, index=False)
        print(f'Relatório gerado: {filename}')
    except Exception as e:
        print(f"Ocorreu um erro ao gerar o relatório: {e}")
    finally:
        conn.close()

# Função para exibir o menu
def show_menu():
    while True:
        print("\n=====CADASTRO DE CLIENTES=====")
        print("1. Adicionar cliente")
        print("2. Listar clientes")
        print("3. Atualizar cliente")
        print("4. Excluir cliente")
        print("5. Gerar relatório Excel")
        print("6. Sair")
        print("================================")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            add_customer()
        elif choice == '2':
            list_customers()
        elif choice == '3':
            update_customer()
        elif choice == '4':
            delete_customer()
        elif choice == '5':
            generate_report()
        elif choice == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente!")



if __name__ == '__main__':
    create_table()
    show_menu()
