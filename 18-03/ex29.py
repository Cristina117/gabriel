def exibir_menu():
    print("Bem vindo ao menu de cadastro")
    print("1 - Novo cadastro")
    print("2 - login")
    print("3 - sair")
def cadastro_pessoa(cadastros):
    nome=input("nome:")
    idade=input("idade:")
    turma=input("turma:")
    curso=input("curso:")
    cadastros.append({"nome:"nome,"idade:"idade,"turma:"turma,"curso:"curso})
    print("cadastro realizado com sucesso!")