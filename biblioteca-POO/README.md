📚 Biblioteca POO (Associação de Classes)
Este projeto é uma demonstração prática de como gerir relações entre diferentes entidades num sistema utilizando Programação Orientada a Objetos (POO) em Python. O sistema simula o catálogo de livros de um autor vinculado a uma editora.

🚀 Funcionalidades Principais
Associação entre Classes: O sistema conecta as classes Autor, Livro e Editora, demonstrando como objetos se relacionam na memória.

CRUD de Livros: Permite adicionar, listar e remover livros de forma dinâmica.

Validação de Duplicados: O sistema verifica se um livro já existe (case-insensitive) antes de permitir o novo registo.

Ordenação Inteligente: A listagem para remoção é apresentada de forma ordenada alfabeticamente para facilitar a experiência do utilizador.

Persistência em JSON: Gravação e carregamento automático do acervo em ficheiro .json.

🛠️ Pilares de POO Demonstrados
Neste código, foquei-me na aplicação de conceitos estruturais:

Encapsulamento: Uso de @property para aceder a atributos protegidos (como o nome do autor).

Composição e Associação: A classe Autor possui uma lista de objetos Livro e uma instância da classe Editora.

Lógica de Coleções: Manipulação de listas com métodos como pop(), append() e funções lambda para ordenação personalizada.

📂 Como Executar
Certifique-se de que o Python 3.10+ está instalado.

Execute o ficheiro:

Bash
python biblioteca_POO.py
Os dados serão guardados automaticamente em biblioteca_POO.json.
