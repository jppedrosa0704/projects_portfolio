import os  # Importa o módulo para interagir com o sistema operacional (limpar tela)

def limpar_tela():
    # Limpa a tela do terminal dependendo do sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

# lista de tarefas atualizada
def listar_tarefas(tarefas):
    if not tarefas:
        print('⚠️  não tem tarefas.')
        input('\nPress any key to exitt...')
        return
    
    #Mostra a lista de tarefas atualizada
    for tarefa in tarefas:
        print('TAREFAS: ')
        print(tarefa)
    input('\nPress any key to exitt...')  # Pausa para o usuário ver as tarefas
    
#desfaz tarefa
def desfazer_tarefa(tarefas, tarefas_desfeitas):
    if not tarefas:
        print('⚠️  nada para desfazer.')
        input('\nPress any key to exit...')
        return
    
    desfazer_ultima_tarefa = tarefas.pop()  # Remove o último item
    tarefas_desfeitas.append(desfazer_ultima_tarefa)  # Armazena na lista de desfeitas
    print(f'tarefa desfeita: {desfazer_ultima_tarefa}\n') #Mostra o item desfeito
    
    #Mostra a lista de tarefas atualiada
    print('TAREFAS: ')
    for tarefa in tarefas:
        print(tarefa)
    input('\nPress any key to exit...')

#refaz tarefa
def refazer_tarefa(tarefas, tarefas_desfeitas):
    if not tarefas_desfeitas: #verifica se existe tarefa
        print('⚠️  Nada para refazer.')
        input('\nPress any key to exit...')
        return

    refazer = tarefas_desfeitas.pop()  # Remove da lista de desfeitas
    tarefas.append(refazer)    # Adiciona a tarefa desfeita a lista tarefa
    print(f'Tarefa refeita: {refazer}\n')

    #Mostra a lista de tarefas atualiada
    print('TAREFAS: ')
    for tarefa in tarefas:
        print(tarefa)
    input('\nPress any key to exit...')

#adiciona uma nova tarefa
def acidiona_tarefa(tarefas):

    tarefas.append(opcao) #adiciona uma tarefa a lista
    print(f'Tarefa adicionada: {opcao}')
    input('\nPress any key to exit...')
    return
######### 💻 MAIN PROGRAM #########

# Lista que mantém as tarefas ativas
tarefas = []

# Lista que armazena temporariamente as tarefas desfeitas, permitindo "refazer"
tarefas_desfeitas = []

while True:
    limpar_tela()  # Limpa a tela antes de cada interação com o usuário

    # Mostra comandos disponíveis
    print('comandos: listar, desfazer, refazer e sair: ')
    
    # Recebe a entrada do usuário e converte para minúsculo
    opcao = input('Digite uma tarefa ou comando: ').lower()

    if opcao == 'listar':
        # Mostra todas as tarefas ativas
        listar_tarefas(tarefas)
        continue

    elif opcao == 'desfazer':
        # Remove a última tarefa adicionada e guarda para refazer
        desfazer_tarefa(tarefas, tarefas_desfeitas)
        continue

    elif opcao == 'refazer':
        # Restaura a última tarefa desfeita
        refazer_tarefa(tarefas, tarefas_desfeitas)
        continue

    elif opcao == 'sair':
        # Encerra o loop principal
        break
    else:
        # Adiciona uma nova tarefa
        acidiona_tarefa(tarefas)
        continue

# Exibe a lista final de tarefas ao sair
print(tarefas)
