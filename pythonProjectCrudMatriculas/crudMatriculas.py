import sqlite3
#Criando conexão com banco de dados
def get_db_connection():
    return sqlite3.connect('database.db')

def create_matriculate(name, course):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO matriculas (nome, curso) VALUES (?, ?)', (name, course))
    conn.commit()
    conn.close()
#ler matriculas
def read_matriculates():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM matriculas')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
#atualizar matriculas
def update_matriculates(id, name, course):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE matriculas SET nome = ?, curso = ? WHERE id = ?', (name, course, id))
    conn.commit()
    conn.close()
#deletar matriculas
def delete_matriculates(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM matriculas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
#criar tabela no database
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matriculas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            curso TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
#create menu com estrutura de repeticao enquanto true
def menu():
    while True:
        print("\n====Menu de Matrículas====")
        print("1. Criar Matrícula")
        print("2. Ler Matrículas")
        print("3. Atualizar Matrícula")
        print("4. Excluir Matrícula")
        print("5. Sair")
        print("============================")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Nome do aluno: ")
            course = input("Curso: ")
            create_matriculate(name, course)
        elif choice == '2':
            read_matriculates()
        elif choice == '3':
            id = int(input("ID da matrícula a ser atualizada: "))
            name = input("Novo nome: ")
            course = input("Novo curso: ")
            update_matriculates(id, name, course)
        elif choice == '4':
            id = int(input("ID da matrícula a ser excluída: "))
            delete_matriculates(id)
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    create_table()
    menu()
