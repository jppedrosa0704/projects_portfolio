📝 Task Manager (Undo/Redo Logic)
Este é um gestor de tarefas em linha de comando desenvolvido em Python que implementa a lógica clássica de "Desfazer" e "Refazer". É um exemplo prático de como manipular pilhas (stacks) para controlar o estado de uma aplicação.

🚀 Funcionalidades Principais
Gestão de Tarefas: Adição dinâmica de itens à lista de afazeres.

Sistema Desfazer (Undo): Permite reverter a última ação, movendo a tarefa para um histórico temporário.

Sistema Refazer (Redo): Permite restaurar uma tarefa que foi desfeita, recuperando-a do histórico.

Comandos Inteligentes: O sistema distingue entre a entrada de uma nova tarefa e comandos de controlo (listar, desfazer, refazer).

Interface Limpa: Uso de limpeza de terminal para manter a experiência do utilizador focada.

🛠️ Competências Técnicas Demonstradas
Neste projeto, foquei-me na manipulação avançada de listas:

Lógica de Pilha (LIFO - Last In, First Out): Utilização do método pop() para gerir a ordem das ações de desfazer e refazer.

Controlo de Fluxo: Implementação de um ciclo while True com múltiplas condições e funções modulares.

Gestão de Estado: Manutenção de duas listas paralelas (tarefas e tarefas_desfeitas) para sincronizar as ações do utilizador.

Experiência de Utilizador (UX): Mensagens de aviso (ex: "Nada para refazer") que evitam erros de execução.

📂 Como Utilizar
Execute o script:

Bash
python task_manager.py
Digite o nome de uma tarefa para adicioná-la.

Utilize os comandos especiais:

listar - Visualiza todas as tarefas.

desfazer - Remove a última tarefa.

refazer - Recupera a última tarefa removida.

sair - Encerra o programa.
