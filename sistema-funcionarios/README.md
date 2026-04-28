🏢 Corporate HR System (POO Relationship Model)
Este sistema simula o núcleo de gestão de funcionários de uma empresa, focando-se na organização estrutural entre departamentos e colaboradores utilizando Python.

🚀 Funcionalidades Principais
Modelagem Organizacional: Uso de classes para separar as entidades Empresa, Departamento e Funcionario, simulando um ambiente corporativo real.

Persistência de Dados: Gravação e leitura automática da base de dados de funcionários em ficheiro empresa.json.

Validação de Tipos (isinstance): O sistema garante a integridade dos dados, aceitando apenas objetos da classe Funcionario no método de cadastro.

Gestão Dinâmica (CRUD): Possibilidade de adicionar, listar e remover colaboradores com atualização em tempo real do ficheiro de dados.

Encapsulamento: Proteção de atributos sensíveis utilizando prefixos _ e acesso via decoradores @property.

🛠️ Pilares de POO Demonstrados
Este código é uma excelente vitrine de boas práticas de engenharia de software:

Agregação: A classe Empresa agrega objetos Funcionario. Se a empresa fechar, os funcionários continuam a existir como objetos independentes.

Composição Simples: A relação com o Departamento demonstra como uma empresa se estrutura internamente.

Tratamento de Exceções: Implementação de blocos try/except para lidar com erros de ficheiro e entradas de utilizador inválidas no menu.

📂 Como Executar
Execute o script:

Bash
python hr_system.py
Utilize o menu numérico para gerir a sua equipa.

Os dados serão persistidos no ficheiro empresa.json.
