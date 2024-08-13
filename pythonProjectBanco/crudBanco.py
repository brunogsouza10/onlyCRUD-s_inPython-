import sqlite3

def get_db_connection():
    return sqlite3.connect('database.db')

def create_register(name, address, age, gender, investment):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO cadastroBanco(nome, endereco, idade, sexo, investimento) VALUES(?,?,?,?,?)',
                   (name, address, age, gender, investment))
    conn.commit()
    conn.close()

def read_registers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cadastroBanco')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def update_registers(id, name, address, age, gender, investment):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE cadastroBanco SET nome = ?, endereco = ?, idade = ?, sexo = ?, investimento = ? WHERE id = ?',
                   (name, address, age, gender, investment, id))
    conn.commit()
    conn.close()

def delete_registers(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cadastroBanco WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS cadastroBanco (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL,
        idade INTEGER,
        sexo TEXT NOT NULL,
        investimento INTEGER)
        '''
    )
    conn.commit()
    conn.close()

def menu():
    while True:
        print("\n====MENU DE CADASTRO BANCO TAXAHADDAD====")
        print("1. Criar Cadastro ")
        print("2. Ler Cadastros ")
        print("3. Atualizar Cadastro ")
        print("4. Excluir Cadastro ")
        print("5. Sair")
        print("============================================")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Nome do cliente: ")
            address = input("Endereço: ")
            age = input("Idade: ")
            gender = input("Sexo: ")
            investment = input("Investimento: ")
            create_register(name, address, int(age), gender, int(investment))

        elif choice == '2':
            read_registers()

        elif choice == '3':
            id = int(input("ID do cadastro a ser atualizado: "))
            name = input("Novo nome: ")
            address = input("Novo endereço: ")
            age = input("Nova idade: ")
            gender = input("Novo sexo: ")
            investment = input("Novo investimento: ")
            update_registers(id, name, address, int(age), gender, int(investment))

        elif choice == '4':
            id = int(input("ID do cadastro a ser excluído: "))
            delete_registers(id)

        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    create_table()
    menu()
