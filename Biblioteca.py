user = {}

def cadastro():
    print("\nBem-vindo ao cadastro de usuários!")asda
    
    email = input("Digite o seu e-mail: ")
    senha = input("Digite uma senha: ")

    user[email] = senha    
    print("Cadastro realizado com sucesso!")

#------------------------------------------------------------------------------------------- 
def login(user):
    print("\nBem-vindo ao sistema de login!")
    
    email = input("Digite o seu e-mail: ")
    senha = input("Digite a sua senha: ")
    
    if email in user and user[email] == senha:
        print("Login realizado com sucesso!")
        return True
    
    else:
        print("login invalido")
        return False

#------------------------------------------------------------------------------------------- 
def removerUser():
    print("\nBem-vindo à seção de remoção de usuários!")

    email = input("Digite o email do usuário que deseja remover: ")

    if email in user:
        del user[email]
        print(f"Usuário com email '{email}' foi removido com sucesso!")
    else:
        print(f"Não foi encontrado usuário com esse email '{email}'")

#------------------------------------------------------------------------------------------- 
def listarUser():
    print("\nLista de usuários cadastrados:")

    if not user:
        print("Não há usuários cadastrados no sistema.")
    else:
        for email in user:
            print(f"userario = {email}")

#------------------------------------------------------------------------------------------- 
livros = {}

def cadastroLivros():

    while True:
        print("\n Menu livros:")
        print("------------------")
        print("1. Cadastrar novo livro")
        print("2. Exibir livros cadastrados")
        print("3. Escolher apenas um livro")
        print("4. Menu principal")
        
        escolha = input("Digite um numero: ")
        
        if escolha == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano de publicação do livro: ")
            
            livros[titulo] = {
                "autor": autor,
                "ano": ano
            }
            
            print(f"Livro '{titulo}' cadastrado com sucesso!")
        
        elif escolha == "2":
            if not livros:
                print("Nenhum livro cadastrado ainda.")
            else:
                print("\nLivros cadastrados:")
                for titulo, livro_info in livros.items():
                    print("-------------------")
                    print(f"Título: {titulo}")
                    print(f"Autor: {livro_info['autor']}")
                    print(f"Ano: {livro_info['ano']}")
                    print("\n")
        
        elif escolha == "3":
            if not livros:
                print("Nenhum livro cadastrado ainda.")
            else:
                titulo_livro = input("Digite o título do livro: ")
                if titulo_livro in livros:
                    livro_info = livros[titulo_livro]
                    print("-------------------")
                    print((f"\nTitulo: {titulo_livro}"))
                    print(f"Autor: {livro_info['autor']}")
                    print(f"Ano: {livro_info['ano']}")
                    print("\n")
                    
        elif escolha == "4":
            menuPrincipal()
        else:
            print("Opção inválida")
            
#------------------------------------------------------------------------------------------- 
def gerenciarColaboradores():

    while True:
        print("\nMenu Colaborador:")
        print("------------------")
        print("1. adicionar colaborador ")
        print("2. Remover colaborador")
        print("3. Listar Colaborador")
        print("4. Menu Principal")

        escolha = input("Digite um numero: ")
        if escolha == "1":
            cadastro() 
        elif escolha == "2":
            removerUser()

        elif escolha == "3":
            listarUser()
            
        elif escolha == "4":
            menuPrincipal()
        else:
            print("Opção inaválida")
#------------------------------------------------------------------------------------------- 
def menuPrincipal():
    while True:
        print("\n Menu Principal")
        print("------------------")
        print("1. Gerenciar Colaboradores")
        print("2. livros")
        print("3. Sair")

        escolha = input("Digite um numero: ")

        if escolha == "1":
            gerenciarColaboradores()

        elif escolha == "2":
            cadastroLivros()
         
        elif escolha == "3":
            break

        else:
            print("Opção inválida. Tente novamente.")
#-------------------------------------------------------------------------------------------  
def main():
    while True:
        print("\nBem vindo a Biblioteca:")
        print("------------------")
        print("1. Login")
        print("2. cadastro")

        escolha = input("Digite um numero: ")

        if escolha =="1":
            if login(user):
                menuPrincipal()

        elif escolha == "2":
            cadastro()

        else:
            print("Opção inaválida")

    

if __name__ == "__main__":
    main()

