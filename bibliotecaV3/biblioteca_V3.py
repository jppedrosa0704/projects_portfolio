import json  # Para salvar/carregar dados em arquivos JSON
import os    # Para limpar a tela

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# ---------- CLASSES ---------- #
class Autor:
    def __init__(self, nome):
        self.nome = nome
        self.editora = None  # Editora do autor (opcional)
        self.livros = []     # Lista de livros do autor

    def __str__(self):
        return self.nome


class Livro:
    def __init__(self, nome):
        self._nome = nome
        self.editora = None  # Editora do livro (opcional)

    @property
    def nome(self):
        return self._nome


class Editora:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    def __str__(self):
        return self.nome


# ---------- FUNÇÕES DE ARQUIVOS ---------- #
def salvar_autores(autores, caminho='autores.json'):
    """Salva os autores e seus livros em um arquivo JSON"""
    autores_dict = []
    for autor in autores:
        autores_dict.append({
            'nome': autor.nome,
            'editora': autor.editora.nome if autor.editora else None,
            'livros': [
                {
                    'nome': livro.nome,
                    'editora': livro.editora.nome if livro.editora else None
                } for livro in autor.livros
            ]
        })

    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(autores_dict, arquivo, ensure_ascii=False, indent=4)

    print(f"{len(autores)} autores salvos no {caminho}")


def carregar_autores(caminho='autores.json'):
    """Carrega autores de um arquivo JSON"""
    autores = []
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            for a in dados:
                autor = Autor(a['nome'])

                # Recriar livros do autor
                autor.livros = []
                for l in a.get('livros', []):
                    livro = Livro(l['nome'])
                    if l.get('editora'):
                        livro.editora = Editora(l['editora'])
                    autor.livros.append(livro)

                # Recriar editora do autor
                if a.get('editora'):
                    autor.editora = Editora(a['editora'])

                autores.append(autor)
    except FileNotFoundError:
        return []

    return autores


def salvar_editoras(editoras, caminho='editoras.json'):
    """Salva editoras em um arquivo JSON"""
    editoras_dict = [{'nome': editora.nome} for editora in editoras]
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(editoras_dict, arquivo, ensure_ascii=False, indent=4)
    print(f"{len(editoras)} editoras salvas no {caminho}")


def carregar_editoras(caminho='editoras.json'):
    """Carrega editoras de um arquivo JSON"""
    editoras = []
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            for e in dados:
                editoras.append(Editora(e['nome']))
    except FileNotFoundError:
        return []
    return editoras


# ---------- FUNÇÕES DE LISTAGEM E REMOÇÃO ---------- #
def listar_livros():
    """Lista todos os livros cadastrados"""
    limpar_tela()
    encontrou = False

    if not autores:
        print('Nenhum autor cadastrado')
    else:
        for autor in autores:
            if autor.livros:
                encontrou = True
                print('=-'*29)
                print(f" {'':<15}Autor: {autor.nome}")
                print("=-"*29)
                for livro in autor.livros:
                    print(f"Livro: {livro.nome:<25} Editora: {livro.editora.nome if livro.editora else 'Não tem cadastro'}")
                print()
        print('=-'*29)
        if not encontrou:
            print("Nenhum livro cadastrado.")
    input('\nPressione qualquer tecla para continuar...')


def remover_livro():
    """Remove um livro de um autor"""
    limpar_tela()
    if not autores:
        print('Não existem autores cadastrados.')
        input('\nPressione qualquer tecla para continuar...')
        return

    # Lista autores
    for i, autor in enumerate(autores, start=1):
        print(f"{i}. {autor.nome}")

    # Escolher autor
    indice_autor = int(input("\nDigite o índice do autor desejado: "))
    if 1 <= indice_autor <= len(autores):
        autor_selecionado = autores[indice_autor - 1]
    else:
        print("Índice inválido")
        input('⚠️  Pressione ENTER para voltar ao menu.')
        return

    if not autor_selecionado.livros:
        print(f"\n⚠️  Não tem livros cadastrados do autor '{autor_selecionado.nome}'.")
        input('\nPressione qualquer tecla para continuar...')
        return

    # Lista livros do autor
    for i, livros in enumerate(autor_selecionado.livros, start=1):
        print(f"{i}. {livros.nome}")

    # Escolher livro
    indice_livro = int(input('Digite o índice do livro: '))
    if 1 <= indice_livro <= len(autor_selecionado.livros):
        livro_selecionado = autor_selecionado.livros[indice_livro - 1]
    else:
        print("Índice inválido")
        input("\nPressione ENTER para voltar ao menu...")
        return

    # Remover livro
    autor_selecionado.livros.remove(livro_selecionado)
    salvar_autores(autores)
    print(f"Livro '{livro_selecionado.nome}' removido do '{autor_selecionado.nome}' com sucesso.")
    input('\nPressione qualquer tecla para continuar...')


def listar_autores():
    """Lista todos os autores cadastrados"""
    limpar_tela()
    if not autores:
        print("Não tem autores cadastrados.")
    else:
        print("=-"*12)
        print(f"{'':<7}Autores")
        print("=-"*12)
        for autor in autores:
            print(f"{autor.nome}")
        print("=-"*12)
    input('\nPressione qualquer tecla para continuar...')


def listar_editoras():
    """Lista todas as editoras cadastradas"""
    for i, editora in enumerate(editoras, start=1):
        print(f"{i} {editora.nome}")
    input('\nPressione qualquer tecla para continuar...')


# ---------- LISTAS GLOBAIS ---------- #
autores = carregar_autores()
editoras = carregar_editoras()


# ---------- MENU PRINCIPAL ---------- #
while True:
    limpar_tela()
    print('--------------------------------------')
    print('           MENU DO SISTEMA            ')
    print('--------------------------------------')
    print('[1] Cadastrar Autor')
    print('[2] Cadastrar Editora')
    print('[3] Adicionar livro a um autor')
    print('[4] Listar livros')
    print('[5] Remover livro de um autor')
    print('[6] Listar autores')
    print('[7] Listar editoras')
    print('[8] Sair')
    print('--------------------------------------')

    try:
        opc = int(input('Escolha sua opção: '))
    except ValueError:
        print('Opção inválida.')
        input('\nPressione qualquer tecla para continuar...')
        continue

    match opc:
        case 1:
            # Cadastrar Autor
            nome_autor = input("Digite o nome do autor: ").strip()
            autor_existente = next((a for a in autores if a.nome.lower() == nome_autor.lower()), None)

            if autor_existente:
                print(f"⚠️ O autor '{nome_autor}' já existe! Adicione livros a ele ou escolha outro nome.")
                input("\nPressione Enter para continuar...")
            else:
                autor = Autor(nome_autor)
                autores.append(autor)
                salvar_autores(autores)
                print(f"{nome_autor} Salvo com sucesso!")
                input("\nPressione Enter para continuar...")

        case 2:
            # Cadastrar Editora
            nome_editora = input("Digite o nome da editora: ").strip()
            editora_existente = next((e for e in editoras if e.nome.lower() == nome_editora.lower()), None)
            if not editora_existente:
                editora = Editora(nome_editora)
                editoras.append(editora)
                salvar_editoras(editoras)
                print(f"{nome_editora} Salvo com sucesso!")
                input("\nPressione Enter para continuar...")
            else:
                print(f"⚠️ A editora '{nome_editora}' já está cadastrada.")
                input("\nPressione Enter para voltar ao menu...")

        case 3:
            # Adicionar livro a um autor
            limpar_tela()
            if not autores:
                print("Nenhum autor cadastrado ainda!")
                input("\nPressione Enter para continuar...")
                continue

            # Mostrar autores
            print("Autores disponíveis:")
            for i, autor in enumerate(autores, start=1):
                print(f"{i} - {autor.nome}")

            # Escolher autor
            while True:
                try:
                    indice_autor = int(input('\nDigite o índice do autor: '))
                    if 1 <= indice_autor <= len(autores):
                        autor_selecionado = autores[indice_autor - 1]
                        print(f"\nAutor escolhido: {autor_selecionado}")
                        input("\nPressione Enter para continuar...")
                        break
                    else:
                        print('⚠️  Opção inválida')
                        input("\nPressione Enter para continuar...")
                except ValueError:
                    print("⚠️  Opção inválida.")

            limpar_tela()
            nome_livro = input('Digite o nome do livro: ')
            livro = Livro(nome_livro)
            autor_selecionado.livros.append(livro)

            # Perguntar se deseja adicionar editora
            while True:
                resp = input('Quer adicionar uma editora [S/N]? ').upper().strip()
                if resp == 'S':
                    if editoras:
                        for i, editora in enumerate(editoras, start=1):
                            print(f"{i}. {editora.nome}")
                        try:
                            indice = int(input('Escolha a editora: '))
                            if 1 <= indice <= len(editoras):
                                livro.editora = editoras[indice - 1]
                            else:
                                print("Índice inválido")
                        except ValueError:
                            print("Entrada inválida")
                    break
                elif resp == 'N':
                    break
                else:
                    print("Digite apenas S ou N.")

            # Salvar autor com novo livro
            salvar_autores(autores)
            print(f"Livro '{nome_livro}' adicionado ao autor '{autor_selecionado.nome}'!")
            input("\nPressione Enter para continuar...")

        case 4:
            listar_livros()
        case 5:
            remover_livro()
        case 6:
            listar_autores()
        case 7:
            listar_editoras()
        case 8:
            break
        case _:
            print("Opção inválida.")
            input('\nPressione qualquer tecla para continuar...')