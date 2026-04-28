📚 Advanced Library Management (V3 - POO & JSON)
Este é um sistema robusto de gestão bibliográfica desenvolvido em Python, que utiliza Programação Orientada a Objetos (POO) para modelar relações complexas entre Autores, Livros e Editoras, com persistência de dados em múltiplos ficheiros.

🚀 Funcionalidades Principais
Arquitetura Multi-Classe: Implementação de classes independentes para Autor, Livro e Editora com associações dinâmicas.

Persistência Dupla (JSON): Separação de dados em autores.json e editoras.json, garantindo a integridade e organização da informação.

Sistema de Índices: Navegação intuitiva onde o utilizador escolhe autores e livros através de índices numéricos, minimizando erros de digitação.

Validação de Existência: Impede o registo duplicado de autores e editoras (case-insensitive).

Listagem Estruturada: Visualização organizada com alinhamento de texto e separadores visuais para facilitar a leitura.

🛠️ Competências Técnicas Demonstradas
Este projeto eleva o nível técnico ao aplicar:

Serialização de Objetos Complexos: Transformação de instâncias de classes em dicionários aninhados para armazenamento em JSON e a subsequente reidratação (conversão de JSON de volta para objetos Python).

List Comprehension & Lambdas: Uso de técnicas avançadas para filtragem e mapeamento de dados.

Gestão de Exceções: Tratamento de erros de ficheiro (FileNotFoundError) e de entrada de dados (ValueError).

Encapsulamento: Uso de atributos protegidos (_nome) e decoradores @property.

📂 Como Utilizar
Garanta que tem o Python instalado.

Execute o ficheiro:

Bash
python biblioteca_v3.py
O sistema criará automaticamente os ficheiros JSON necessários ao realizar o primeiro registo.
