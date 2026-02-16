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
    
    user_to_update = None

    for user in user_list:

        if user_id == user['id']:
            user_to_update = user
            break
        
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
    
    for user in user_list:
        if user['id'] == id_remover:
            del user_list[user_list.index(user)]
            print(f'Usuário com id {id_remover} removido.')
            return

   

def main():
    quit_program = False
    user_list = []
    next_user_id = 1
    while not quit_program:
        
        show_menu()
        answer = read_option()
    
        if answer == 1:
           create_user(user_list, next_user_id)
           next_user_id+=1

        elif answer == 2:
            read_users(user_list)
            time.sleep(5)
        
        elif answer == 3:
            update_user(user_list)
            time.sleep(5)

        elif answer == 4:
            delete_user(user_list)

        elif answer == 5:
            quit_program = True
        
        else:
            print('Opção inválida.')

    print('\nPrograma finalizado.')

main()  