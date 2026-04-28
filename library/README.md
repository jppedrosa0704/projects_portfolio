📖 Library Management System (Python CLI)
Este é um sistema de gestão de biblioteca desenvolvido em Python, focado na manipulação de dicionários e controlo de fluxo para operações de inventário e circulação de livros.

🚀 Funcionalidades Principais
Registo de Acervo: Permite o cadastro de títulos, autores e anos de publicação com validação de dados (ex: ano com 4 dígitos).

Gestão de Estados (Empréstimos): Sistema dinâmico para alternar o status de um livro entre available (disponível) e borrowed (emprestado).

Pesquisa Flexível: Motor de busca que localiza livros tanto pelo título quanto pelo nome do autor.

Interface CLI Amigável: Menu estruturado com contagem decrescente no encerramento e limpeza de ecrã para melhor legibilidade.

🛠️ Competências Técnicas Demonstradas
Neste projeto, apliquei conceitos fundamentais de programação:

Dicionários Aninhados: Armazenamento eficiente de dados estruturados onde cada chave (título) aponta para um objeto de atributos.

Algoritmos de Pesquisa: Implementação de lógica de iteração para busca parcial e correspondência de padrões (case-insensitive).

Tratamento de Exceções: Uso de blocos try/except para garantir que o programa não crash caso o utilizador introduza dados inválidos.

Formatação de Strings: Uso de f-strings com alinhamento (<60) para gerar tabelas limpas e organizadas no terminal.

📂 Como Utilizar
Execute o script principal:

Bash
python library_system.py
Utilize o menu numérico para navegar entre as funções de cadastro, listagem, busca ou empréstimo.
