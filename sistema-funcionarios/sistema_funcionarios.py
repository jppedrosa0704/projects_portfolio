import json  # Biblioteca para manipulação de arquivos JSON

# Classe que representa a Empresa
class Empresa:
    def __init__(self, nome):
        self._nome = nome                 # Nome da empresa (protegido)
        self._departamento = None         # Departamento da empresa (protegido)
        self._funcionarios = []           # Lista de funcionários

    # Cadastro de funcionários
    def cadastrar_funcionario(self, funcionario):
        if not isinstance(funcionario, Funcionario):  # Validação de tipo
            raise TypeError('Aceita apenas objeto do tipo Funcionario.')
        self._funcionarios.append(funcionario)        # Adiciona funcionário à lista
        print(f"✅  {funcionario.nome} salvo com sucesso.")  # Mensagem de sucesso
        input('\nPressione Enter para continuar...')        # Pausa para o usuário

    # Getter para o nome da empresa
    @property
    def nome(self):
        return self._nome

    # Salvar funcionários em arquivo JSON
    def salvar_json(self):
        try:
            dados = {
                "empresa": self._nome,
                "funcionarios": [f._nome for f in self._funcionarios]  # Lista de nomes
            }
            with open('empresa.json', 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)  # Salva de forma legível
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    # Carregar funcionários do JSON
    def carregar_json(self):
        try:
            with open('empresa.json', 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)  # Carrega dados do arquivo
                self._funcionarios = []     # Limpa lista atual
                for nome in dados.get('funcionarios', []):  # Pega a lista de nomes
                    self._funcionarios.append(Funcionario(nome))  # Cria objetos Funcionario
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # Arquivo ainda não existe ou está vazio

    # Remover funcionário pelo nome
    def remover_funcionario(self, funcionario):
        for f in self._funcionarios:
            if f.nome == funcionario:          # Verifica se o nome coincide
                self._funcionarios.remove(f)   # Remove funcionário
                print(f"❌ {funcionario} removido com sucesso.")
                input('\nPressione Enter para continuar...')
                return True
        print(f"⚠️ Funcionário {funcionario} não encontrado.")  # Caso não exista
        input('\nPressione Enter para continuar...')
        return False

    # Listar funcionários cadastrados
    def listar_funcionarios(self):
        if not self._funcionarios:  # Verifica se lista está vazia
            print('Não há funcionários cadastrados.')
        else:
            print("=-"*15)
            print(f"{'LISTA DE FUNCIONÁRIOS':>25}")
            print("=-"*15)
            # Verifica se empresa tem departamento
            dept_nome = self._departamento.nome if self._departamento else 'sem departamento'
            for f in self._funcionarios:
                print(
                    f"Empresa: {self.nome}\n"
                    f"Nome do funcionário: {f.nome}\n"
                    f"Departamento: {dept_nome}"
                )
                print("=-"*15)
        input('\nPressione Enter para continuar...')

# Classe que representa o funcionário
class Funcionario:
    def __init__(self, nome):
        self._nome = nome  # Nome protegido do funcionário

    @property
    def nome(self):
        return self._nome   # Acesso seguro ao nome

# Classe que representa o departamento
class Departamento:
    def __init__(self, nome):
        self._nome = nome  # Nome protegido do departamento

    @property
    def nome(self):
        return self._nome  # Getter para nome do departamento

# Criação da empresa e departamento
empresa = Empresa('DEV Consulting')
departamento = Departamento('RH')
empresa._departamento = departamento  # Atribui departamento à empresa
empresa.carregar_json()               # Carrega funcionários salvos anteriormente

# Menu do sistema
print('[1] Adicionar funcionários')
print('[2] Listar funcionários')
print('[3] Remover funcionário')
print('[4] Sair')

while True:
    try:
        opc = int(input('Escolha a opção desejada: '))
        if opc < 1 or opc > 4:
            print('Opção inválida.')
    except ValueError:
        print('Opção inválida.')

    match opc:
        case 1:
            nome = input('Digite o nome do funcionário: ')
            nome_funcionario = Funcionario(nome)
            empresa.cadastrar_funcionario(nome_funcionario)
            empresa.salvar_json()  # Atualiza JSON
        case 2:
            empresa.listar_funcionarios()  # Mostra funcionários
        case 3:
            funcionario = input('Digite o nome do funcionário: ')
            if empresa.remover_funcionario(funcionario):
                empresa.salvar_json()  # Atualiza JSON
        case 4:
            break  # Sai do loop