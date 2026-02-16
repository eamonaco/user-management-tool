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

def read_option():
    return int(input('\nOpção: '))

def return_user_id(user_list, user_id):
    
    for user in user_list:
        if user_id == user['id']:
            return user
    
    return None

def create_user(user_list, next_user_id):
    user_name = input('Digite o nome do usuário: ')
    user_email = input('Digite o email do usuário: ')
    user_age = int(input('Digite a idade do usuário: '))
            
    user = {'id': next_user_id,
            'name': user_name, 
            'email': user_email,
            'age': user_age}

    user_list.append(user)
            
    print('Usuário cadastrado com sucesso.')

def read_users(user_list):
    if len(user_list) == 0:
        print('Nenhum usuário encontrado.')
        return

    for user in user_list:
        print(f"\nId: {user['id']}\nNome: {user['name']}\nEmail: {user['email']}\nIdade: {user['age']}\n\n")

def update_user(user_list):
    if len(user_list) == 0:
        print('Nenhum usuário encontrado.')
        return
    
    read_users(user_list)
    user_id = int(input("\n\nSelecione o usuário pelo id: "))
    
    user_to_update = return_user_id(user_list, user_id)
        
    if user_to_update == None:
        print("Usuário não encontrado.")
        return

    for attribute in user_to_update:
        if attribute == "id":
            continue
        
        else:
            print(f'\n\n{translations[attribute]} atual: {user_to_update[attribute]}')
            
            value = input("Digite um novo valor ou pressione ENTER para manter: ")
            
            if attribute == "age" and len(value) != 0:
                value = int(value)
            
            if value != "":
                user_to_update[attribute] = value
        
    
def delete_user(user_list):
    if len(user_list) == 0:
        print('Nenhum usuário encontrado.')
        return

    read_users(user_list)
    id_remover = int(input("\n\nSelecione o usuário pelo id: "))
    
    user = return_user_id(user_list, id_remover)

    if user == None:
        print("Usuário não encontrado.")
        return

    user_list.remove(user)
    print(f"Usuário com id {user["id"]} deletado com sucesso.")


def main():
    user_list = []
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
            quit_program = True
            continue

        if answer not in actions:
            print("Opção inválida.")
            continue

        action = actions[answer]

        if action == "create":
            create_user(user_list, next_user_id)
            next_user_id += 1
        else:
            action(user_list)

    print("\nPrograma finalizado.")

main()  