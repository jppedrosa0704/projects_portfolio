import json
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

    
########################################
    '''CLASSE LIVRO'''
########################################

class Livro:
    def __init__(self, nome):
        self._nome = nome
    @property
    def nome(self):
        return self._nome
    
########################################
        '''CLASSE EDITORA'''
########################################
class Editora:
    def __init__(self, nome):
        self._nome = nome
    @property
    def nome(self):
        return self._nome


########################################
        '''CLASSE AUTOR'''
########################################
class Autor:
    def __init__(self, nome):
        self._nome = nome
        self.editora = None
        self._livros = []

    @property
    def nome(self):
        return self._nome
    
    #--------------------------------------
        #   ADICIONAR LIVRO   #
    #--------------------------------------
    def adicionar_livro(self, livro):

        # if any(l.nome == livro.nome for l in self._livros):
        #     print('Este livro já se encontra cadastrado.')
        #     return False
        for l in self._livros:
            if l.nome.lower() == livro.nome.lower():
                print('Este livro já se encontra cadastrado.')
                input('\nPressione qualquer tecla para continuar...')
                return False
        
        self._livros.append(livro)
        print(f"✅  {livro.nome} cadastrado com sucesso!")
        input('\nPressione qualquer tecla para continuar...')
        return True
    #--------------------------------------
            #   LISTAR LIVROS   #
    #--------------------------------------
    def listar_livros(self):
        if not self._livros:
            print('Não há livros cadastrados.')

        else:
            print("----LISTA DE LIVROS-----")
            edit = self.editora.nome if self.editora else "não tem editora"
            for l in self._livros:
                print(
                    f"Autor: {self._nome}\n"
                    f"Livro: {l._nome}\n"
                    f"Editora: {edit}\n"
                )
        input('\nPressione qualquer tecla para continuar...')

    #--------------------------------------#
    #           REMOVE LIVRO               #
    #--------------------------------------#
    def remove_livro(self):
        limpar_tela()

        ordenado = sorted(self._livros, key=lambda l: l.nome) #guarda na variável a lista ordenada por livro
        for i, livro in enumerate(ordenado, start=1):#enumera os livros por índice
            print(f"[{i}]  {livro.nome}")
        while True:
            try:
                indice = int(input("Digite o códito do  livro para remover:"))
                if indice < 1 or indice > len(self._livros): #Validação para evitar uma opção inválida
                    print('opção inválida')
                    input('\nPressione qualquer tecla para continuar...')
                    continue
                else:
                    removido = self._livros.pop(indice - 1) #remove pelo índice o livro
                    print(f"🔥  {removido.nome} removido com sucesso.")
                    autor.salvar_json()
                    input('\nPressione qualquer tecla para continuar...')
                    break
            except ValueError:
                print('opção inválida')
        
    #--------------------------------------#
    #         SALVA LISTA EM JSON          #
    #--------------------------------------#
    def salvar_json(self):
        dados = {
            'autor': self._nome,
            'livro': [l._nome for l in self._livros],
            'editora': self.editora.nome
            }
        with open('biblioteca_POO.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    #--------------------------------------#
    #         CARREGA LISTA EM JSON        #
    #--------------------------------------#
    def carregar_json(self):
        try:
            with open('biblioteca_POO.json', 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                self._livros = []
                for l in dados.get('livro', []):
                    self._livros.append(Livro(l))

        except (FileNotFoundError, json.JSONDecodeError):
            #caso não tenha aqruivo ou ocorra algma falha no json
            pass


########################################
        '''PROGRAMA PRINCIPAL'''
########################################
autor = Autor('Machado de Assis') # cria o objeto autor
autor.carregar_json() # carrega os dados da lista em json
editora = Editora('Abril') #cria objeto editora
autor.editora = editora #ligação entre a classe autor com a classe editora

#--------------------------------------
        #   MENU DO SISTEMA   #
#--------------------------------------
while True:
    limpar_tela()
    print('--------------------------------------')
    print('           MENU DO SISTEMA            ')
    print('--------------------------------------')
    print("[1] Adicionar livro")
    print("[2] Listar livros")
    print("[3] Remover livro")
    print("[4] Sair")
    print('--------------------------------------')
    try:
        opc = int(input('Escolha sua opção: '))
        if opc < 1 or opc > 4:
            print('Opção inválida')
            continue
    except ValueError:
        print('Opção inválida')
        continue
    match opc:
        case 1:
            livro = Livro(input('Digite o nome do livro: '))
            autor.adicionar_livro(livro)
            autor.salvar_json()
            
        case 2:
            autor.listar_livros()
        case 3:
            # for i, livro in enumerate(autor.livros.nome):
            #     print(f"{i}")
            # input('\nPressione qualquer tecla para continuar...')
            autor.remove_livro()
        case 4:
            break


