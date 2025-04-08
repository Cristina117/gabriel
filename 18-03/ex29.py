def exibir_menu():
    print("Bem vindo ao menu de cadastro")
    print("1 - Novo cadastro")
    print("2 - login")
    print("3 - sair")
    print(_______________________________)
def cadastro_pessoa(cadastros):
    nome=input("nome:")
    idade=input("idade:")
    turma=input("turma:")
    curso=input("curso:")
    cadastros.append({"nome":nome,"idade":idade,"turma":turma,"curso":curso})
    print("cadastro realizado com sucesso!")
    def ver_cadastros(cadastros):
        if not cadastros:
            print(" Nenhum cadastro no sistema.")
        else:
            print("/n---------- LISTA DE CADASTROS----------")
        for i, pessoa in  enumerate (cadastros, 1):
            print (f"{i} . nome: {pessoa['nome']}, idade:
            {pessoa['idade']}, turma: {pessoa['turma']}, curso: {pessoa['curso']}")
        def main():
            cadastros = []
            while true:
                exibir_menu()
                opção = input("Escolha uma opção:")
                if opção == "1":
                    cadastrar_pessoa (cadastros)
                elif opção == "2":
                    ver_cadastros(cadastros)
                elif opção == "3":
                    print("obrigada por utilizar nosso sistema!")
if _name_=="main":
                    main()
                    
        import json

ARQUIVO_CADASTROS = "cadastros.json"

def exibir_menu():
    print("================ MENU CADASTRO ================")
    print("1. Cadastrar pessoa")
    print("2. Ver cadastros")
    print("3. Sair")
    print("==============================================")

def salvar_cadastros(cadastros):
    with open(ARQUIVO_CADASTROS, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)

def carregar_cadastros():
    try:
        with open(ARQUIVO_CADASTROS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def cadastrar_pessoa(cadastros):
    nome = input("Nome: ")
    idade = input("Idade: ")
    turma = input("Turma: ")
    curso = input("Curso: ")

    cadastros.append({"nome": nome, "idade": idade, "turma": turma, "curso": curso})
    salvar_cadastros(cadastros)
    print("Cadastro realizado com sucesso!")

def ver_cadastros(cadastros):
    if not cadastros:
        print("\nNenhum cadastro realizado.")
    else:
        print("\n================ LISTA DE CADASTROS =================")
        for pessoa in cadastros:
            print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Turma: {pessoa['turma']}, Curso: {pessoa['curso']}")
        input("\nPressione Enter para voltar ao menu...")

def main():
    cadastros = carregar_cadastros()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_pessoa(cadastros)
        elif opcao == "2":
            ver_cadastros(cadastros)
        elif opcao == "3":
            print("Obrigado por utilizar o sistema de cadastro!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

        
