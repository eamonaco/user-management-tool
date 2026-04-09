import persistence
import time


translations = {"name": "Nome",
                "email": "Email",
                "age": "Idade"
}

def show_menu():
    print(
        """
        ---------------------------------------------------------
            |Selecione uma opção:
            |1. Cadastrar usuário
            |2. Listar usuários
            |3. Atualizar usuário
            |4. Remover usuário
            |5. Sair
        ---------------------------------------------------------
        """)

def secure_input(data_type, message):
    while True:
        try:
            data = data_type(input(message))
        except ValueError:
            print("Dado inválido. Digite novamente.")
            continue
        else:
            return data

def read_option():
    return secure_input(int, '\nOpção: ')

def return_user_id(users_list, user_id):
    
    for user in users_list:
        if user_id == user['id']:
            return user
    
    return None

def create_user(users_list, next_user_id):
    user_name = secure_input(str, 'Digite o nome do usuário: ')
    user_email = secure_input(str, 'Digite o email do usuário: ')
    user_age = secure_input(int, 'Digite a idade do usuário: ')

    user = {'id': next_user_id,
            'name': user_name, 
            'email': user_email,
            'age': user_age}

    users_list.append(user)
            
    print('Usuário cadastrado com sucesso.')

def read_users(users_list):
    if len(users_list) == 0:
        print('Nenhum usuário encontrado.')
        return

    for user in users_list:
        print(f"\nId: {user['id']}\nNome: {user['name']}\nEmail: {user['email']}\nIdade: {user['age']}\n\n")

def update_user(users_list):
    if len(users_list) == 0:
        print('Nenhum usuário encontrado.')
        return
    
    read_users(users_list)
    user_id = secure_input(int, "\n\nSelecione o usuário pelo id: ")
    
    user_to_update = return_user_id(users_list, user_id)
        
    if user_to_update == None:
        print("Usuário não encontrado.")
        return

    for attribute in user_to_update:
        if attribute == "id":
            continue
        
        else:
            print(f'\n\n{translations[attribute]} atual: {user_to_update[attribute]}')

            data_type = type(user_to_update[attribute])
            
            value = secure_input(data_type, "Digite um novo valor ou pressione ENTER para manter: ")
            
            if value != "":
                user_to_update[attribute] = value
        
    
def delete_user(users_list):
    if len(users_list) == 0:
        print('Nenhum usuário encontrado.')
        return

    read_users(users_list)
    id_remover = secure_input(int, "\n\nSelecione o usuário pelo id: ")
    
    user = return_user_id(users_list, id_remover)

    if user == None:
        print("Usuário não encontrado.")
        return

    users_list.remove(user)
    print(f"Usuário com id {user['id']} deletado com sucesso.")


def main():
    
    users_list = persistence.load_data()
    
    next_user_id = 1
    quit_program = False

    actions = {
        1: "create",
        2: read_users,
        3: update_user,
        4: delete_user
    }

    while not quit_program:
        show_menu()
        answer = read_option()

        if answer == 5:
            persistence.save_data(users_list)
            quit_program = True
            continue

        if answer not in actions:
            print("Opção inválida.")
            continue

        action = actions[answer]

        if action == "create":
            create_user(users_list, next_user_id)
            next_user_id += 1
        else:
            action(users_list)

    print("\nPrograma finalizado.")

main()  