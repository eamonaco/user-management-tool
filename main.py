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

        elif answer in range(1,5):
            print('\nOpção não implementada. Tente novamente em breve.')
        else:
            print('Opção inválida.')

    print('\nPrograma finalizado.')

main()  