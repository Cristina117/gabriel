import json

ARQUIVO_CADASTROS = "cadastros.json"

def exibir_menu():
    print("_____________ MENU CADASTRO ____________")
    print("1. Cadastrar pessoa")
    print("2. Ver cadastros")
    print("3. Sair")
    print("___________________________________________")

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
    cadastros = carregar_cadastros() # type: ignore
    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            cadastrar_pessoa(cadastros)
        elif opcao == "2":
            ver_cadastros(cadastros)
        elif opcao == "3":
            print("Obrigado por utilizar o sistema de cadastro!")
            break
        else:
            print("Opcao invalida! Tente novamente.")

if __name__ == "__main__":
    main()
