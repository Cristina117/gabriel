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
                    
            #comentario?
        
