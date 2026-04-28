🛒 Market Management System (Python POO)
Este é um sistema completo de gestão de supermercado desenvolvido em Python, focado na aplicação prática de Programação Orientada a Objetos e persistência de dados. O projeto simula o fluxo real de um estabelecimento, desde o inventário até ao registo final de vendas.

🚀 Funcionalidades Principais
Gestão de Inventário: Registo de produtos com controlo de stock automático.

Sistema de Vendas: Interface interativa para associar Clientes, Funcionários (Caixas) e Produtos.

Persistência de Dados: Gravação e leitura de dados em tempo real utilizando ficheiros JSON.

Relatórios: Listagem de vendas por cliente, desempenho de funcionários e alerta de stock baixo.

Lógica de Negócio: Redução automática de stock após a confirmação da venda.

🛠️ Conceitos Técnicos Aplicados
Neste projeto, demonstrei competências em:

Herança: Utilização de uma classe base Person para derivar Customer e Employee.

Encapsulamento: Proteção de atributos sensíveis e organização de métodos de classe.

Composição: A classe Market gere coleções de objetos de outras classes.

Manipulação de Ficheiros: Implementação de um sistema de base de dados simples com o módulo json.

Tratamento de Erros: Uso de blocos try/except para garantir a estabilidade do sistema contra entradas inválidas.

📂 Estrutura do Projeto
market.py: Ficheiro principal com a lógica do menu e execução.

/data: Diretório que armazena os ficheiros JSON (products.json, customers.json, employees.json).

⚙️ Como executar
Certifique-se de ter o Python 3.x instalado.

Clone o repositório.

Execute o comando:

Bash
python market.py
