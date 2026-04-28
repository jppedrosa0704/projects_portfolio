# 💰 Financial System (Python CLI)

Este é um sistema de gestão financeira pessoal desenvolvido em **Python**, que permite o controlo de receitas, despesas e cálculo de saldo em tempo real para múltiplos utilizadores.

## 🚀 Funcionalidades Principais
* **Gestão de Utilizadores:** Registo único por e-mail com validação de formato e nome.
* **Controlo Transacional:** Registo detalhado de Entradas (`income`) e Saídas (`expense`).
* **Relatórios Financeiros:** Geração de sumários com total de ganhos, gastos e balanço final.
* **Persistência em JSON:** Armazenamento automático de dados para garantir que as informações não se percam ao fechar o programa.
* **Interface Limpa:** Navegação via terminal com menus intuitivos e limpeza automática de ecrã.

## 🛠️ Competências Técnicas Demonstradas
Neste projeto, apliquei conceitos fundamentais de engenharia de software:
* **Estruturas de Dados:** Uso de dicionários para acesso rápido aos dados do utilizador via e-mail.
* **Data Validation:** Implementação de filtros para impedir nomes com números, e-mails inválidos ou valores negativos.
* **Modularidade:** Código organizado em funções específicas, facilitando a manutenção e escalabilidade.
* **Persistência de Dados:** Serialização e desserialização de objetos Python para o formato JSON.

## 📂 Como Utilizar
1. Execute o script:
   ```bash
   python financial_system.py

Registe um utilizador com um e-mail válido.

Adicione as suas transações e consulte o relatório financeiro a qualquer momento.
