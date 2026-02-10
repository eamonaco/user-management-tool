import time

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

def create_user(user_list):
    user_name = input('Digite o nome do usuário: ')
    user_email = input('Digite o email do usuário: ')
    user_age = int(input('Digite a idade do usuário: '))
            
    user = {'id': len(user_list)+1,
            'name': user_name, 
            'email': user_email,
            'age': user_age}

    user_list.append(user)
            
    print('Usuário cadastrado com sucesso.')

def list_users(user_list):
    if len(user_list) == 0:
        print('Nenhum usuário encontrado.')
        return

    for user in user_list:
        print(f"\nId: {user['id']}\nNome: {user['name']}\nEmail: {user['email']}\nIdade: {user['age']}\n\n")

     
def main():
    quit_program = False
    user_list = []
    while not quit_program:
        
        show_menu()
        answer = read_option()
    
        if answer == 5:
            quit_program = True
        
        elif answer == 1:
           create_user(user_list)

        elif answer == 2:
            list_users(user_list)
            time.sleep(10)
        
        elif answer in range(3,5):
            print('\nOpção não implementada. Tente novamente em breve.')
        else:
            print('Opção inválida.')

    print('\nPrograma finalizado.')

main()  