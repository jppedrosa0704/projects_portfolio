Este é um sistema completo de Gestão de Inventário e Vendas. Ele é particularmente impressionante para o seu portfólio porque vai além do simples cadastro: ele implementa regras de negócio, como alertas de stock baixo e relatórios de faturação.

Aqui está o README.md ideal para a pasta market-system (ou o nome que preferir):

🛒 Market Management System (Inventory & Sales)
Este é um sistema de gestão comercial completo desenvolvido em Python, projetado para automatizar o controlo de stock e o registo de vendas de um pequeno negócio.

🚀 Funcionalidades Principais
Gestão de Inventário: Registo de produtos com nome, preço e quantidade.

Controlo de Stock Inteligente: Funções dedicadas para adicionar ou remover unidades do stock atual.

Sistema de Vendas: Registo de transações com cálculo automático de total e atualização imediata do inventário.

Relatórios de Negócio: * Faturação: Relatório detalhado de todas as vendas realizadas.

Alerta de Reposição: Filtro automático que lista produtos com menos de 5 unidades em stock.

Persistência de Dados Dupla: Armazenamento independente para products.json (inventário) e sales.json (histórico de vendas).

🛠️ Competências Técnicas Demonstradas
Neste projeto, apliquei conceitos avançados de lógica e organização de dados:

Algoritmos de Ordenação: Uso de lambda functions para manter o inventário sempre organizado alfabeticamente.

Lógica de Negócio (Business Rules): Implementação de verificações de segurança para impedir vendas sem stock suficiente ou preços/quantidades negativas.

Modularidade e Reutilização: Funções utilitárias como want_to_continue() e clear_screen() para manter o código DRY (Don't Repeat Yourself).

Sanitização de Inputs: Validações rigorosas para garantir que nomes de produtos não contenham apenas números e que entradas de preço sejam numéricas.

📂 Como Utilizar
Execute o script:

Bash
python market_system.py
Utilize o menu para cadastrar produtos.

Ao realizar uma venda, o sistema descontará automaticamente do stock e guardará a transação no relatório.
