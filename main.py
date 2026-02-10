import time

def main():
    quit_program = False
    user_list = []
    while not quit_program:
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
        answer = int(input('\nOpção: '))
        
       
        if answer == 5:
            quit_program = True
        
        elif answer == 1:
            user_name = input('Digite o nome do usuário: ')
            user_email = input('Digite o email do usuário: ')
            user_age = int(input('Digite a idade do usuário: '))
            
            user = {'name': user_name, 
                    'email': user_email,
                    'age': user_age}

            user_list.append(user)
            
            print('Usuário cadastrado com sucesso.')

        elif answer == 2:
            if len(user_list) == 0:
                print('Nenhum usuário encontrado.')
                continue
            
            for user in user_list:
                print(f"\nId: {user['id']}\nNome: {user['name']}\nEmail: {user['email']}\nIdade: {user['age']}\n\n")

            time.sleep(10)
        elif answer in range(3,5):
            print('\nOpção não implementada. Tente novamente em breve.')
        else:
            print('Opção inválida.')

    print('\nPrograma finalizado.')

main()  