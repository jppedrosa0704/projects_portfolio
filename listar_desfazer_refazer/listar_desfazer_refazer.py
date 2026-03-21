import os  # Importa o módulo para interagir com o sistema operacional (limpar tela)

def limpar_tela():
    # Limpa a tela do terminal dependendo do sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')


# Lista que mantém as tarefas ativas
tarefas = []

# Lista que armazena temporariamente as tarefas desfeitas, permitindo "refazer"
desfeitas = []

while True:
    limpar_tela()  # Limpa a tela antes de cada interação com o usuário

    # Mostra comandos disponíveis
    print('comandos: listar, desfazer, refazer, sair: ')
    
    # Recebe a entrada do usuário e converte para minúsculo
    opcao = input('Digite uma tarefa ou comando: ').lower()

    if opcao == 'listar':
        # Mostra todas as tarefas ativas
        if not tarefas:
            print('não tem tarefas.')
        else:
            for t in tarefas:
                print(t)
        input('\nPress any key to exitt...')  # Pausa para o usuário ver as tarefas

    elif opcao == 'desfazer':
        # Remove a última tarefa adicionada e guarda para refazer
        if tarefas:
            desfazer_ultima_tarefa = tarefas.pop()  # Remove o último item
            desfeitas.append(desfazer_ultima_tarefa)  # Armazena na lista de desfeitas
            print(f'tarefa desfeita: {desfazer_ultima_tarefa}\n')
            print('TAREFAS: ')
            for t in tarefas:
                print(t)
            input('\nPress any key to exit...')
        else:
            print('nada para desfazer.')
            input('\nPress any key to exit...')

    elif opcao == 'refazer':
        # Restaura a última tarefa desfeita
        if desfeitas:
            refazer = desfeitas.pop()  # Remove da lista de desfeitas
            tarefas.append(refazer)    # Adiciona de volta às tarefas
            print(f'Tarefa refeita: {refazer}\n')
            print('TAREFAS: ')
            for t in tarefas:
                print(t)
            input('\nPress any key to exit...')
        else:
            print('Nada para refazer.')
            input('\nPress any key to exit...')

    elif opcao == 'sair':
        # Encerra o loop principal
        break
    else:
        # Adiciona uma nova tarefa
        tarefas.append(opcao)
        print(f'Tarefa adicionada: {opcao}')
        input('\nPress any key to exit...')

# Exibe a lista final de tarefas ao sair
print(tarefas)
