import json

print("==================")
print("SISTEMA DE ESTOQUE")
print("==================")

produtos = []
def cadastrar_produto():
        numero = True
        vazio = True
        while vazio:
            existe = False
            nome = input('nome do produto: ')
            nome = nome.strip()
            for produto in produtos:
                if nome.lower().strip() == produto["nome"].lower().strip():
                    existe = True

            if nome.strip() == "":
                 print("digite o nome do produto!")
            elif existe:
                 print("Produto já cadastrado!")
            else:
                 vazio = False
        
        while numero:
            try:
                    preco = float(input('preço: '))
                    if preco > 0:
                        numero = False
                    else:
                         print("O valor tem que ser maior que 0!")
            except:
                print("erro, digite um preço válido!")
        numero = True
        while numero:
            try:
                    quantidade = int(input('quantidade: '))
                    if quantidade <= 0:
                        numero = True
                        print("A quantidade tem que ser maior que 0!")
                    else:
                         numero = False

                    
            except:
                 print("erro, digite uma quantidade válida!")
        vazio = True
        while vazio:
            categoria = input('categoria: ')
            categoria = categoria.strip()
            if categoria.strip() == "":
                 print("digite uma categoria!")
            else:
                 vazio = False

        produto = {
                    "nome": nome,
                    "preco": preco,
                    "quantidade": quantidade,
                    "categoria": categoria
                }
        
        produtos.append(produto)

        salvar_produtos()

        print("Produto Cadastrado com Sucesso!")
        
def listar_produtos():
    if len(produtos) == 0:
         print("nenhum produto cadastrado!")
    else:
        for produto in produtos:
                    print("---------------------------------")
                    print("nome:", produto["nome"])
                    print(f"preço: R$ {produto['preco']:.2f}")
                    print("quantidade:", produto["quantidade"])
                    print("categoria:", produto["categoria"])
                    print("---------------------------------")

def registrar_compra():    
    print('qual produto está buscando?')
    nome_produto = input() 
    encontrou = False
     
    for produto in produtos:
        if nome_produto.lower().strip() == produto["nome"].lower().strip():
            print('deseja registrar esse produto? S/N')
            registro = input()
            encontrou = True
     
            if registro.lower() == "s":
                if produto["quantidade"] > 0:
                    produto["quantidade"] -= 1
                    salvar_produtos()
                    print("A Venda foi um Sucesso!")
                else:
                     print("produto sem estoque!")
            else:
                 print("compra não realizada!")
     
    if encontrou == False:
            print("produto não encontrado!")

def repor_produtos():
        print('Qual produto deseja repor?')
        repor = input()
        encontrou = False
        repondo = True
        for produto in produtos:
            if repor.lower().strip() == produto["nome"].lower().strip():
                encontrou = True
                print ("Produto encontrado: ", produto["nome"])
                print ("Quantidade: ", produto["quantidade"])
                while repondo:
                    try:
                        print("quantos produtos deseja repor?")
                        reposicao = int(input())
                        if reposicao >0 :
                             print("reposição realizada com sucesso!")
                             repondo = False
                        else:
                             print("não foi possivel realizar a reposição!")
                    except:
                         print("digite um número valido!")

                produto["quantidade"] += reposicao

                salvar_produtos()
     
        if encontrou == False:
            print("produto não encontrado")

def relatorio_produtos():
        print('========================')
        print("  RELATÓRIO DO ESTOQUE")
        print('========================')
        if len(produtos) == 0:
             print("Nenhum produto cadastrado!")
        else:
            print("total de produtos cadastrados: ", len(produtos))

            total_quantidade = 0

            for produto in produtos:
                total_quantidade += produto["quantidade"]

            print("quantida de produtos em estoque: ", total_quantidade)

            total_preco = 0

            for produto in produtos:
                total_preco += produto["quantidade"] * produto["preco"]

            print(f"valor total do estoque: R$ {total_preco:.2f}")

            maior_quantidade = 0
            nome_maior = ""

            for produto in produtos:
                if produto["quantidade"] > maior_quantidade:
                    maior_quantidade = produto["quantidade"]
                    nome_maior = produto["nome"]

            print(
                "produto com maior estoque: ",
                nome_maior,
                "(",
                maior_quantidade,
                ")"
            )

            menor_quantidade = produtos[0]["quantidade"]
            nome_menor = produtos[0]["nome"]

            for produto in produtos:
                if produto["quantidade"] < menor_quantidade:
                    menor_quantidade = produto["quantidade"]
                    nome_menor = produto["nome"]

            print(
                "produto com menor estoque: ",
                nome_menor,
                "(",
                menor_quantidade,
                ")"
            )

def salvar_produtos():
     with open("produtos.json", "w") as arquivo:
          json.dump(produtos,arquivo,indent=4)


def carregar_produtos():
     global produtos
    
     try:
        with open("produtos.json", "r") as arquivo:
            produtos = json.load(arquivo)

     except:
        print("Não há produtos cadastrados!")

carregar_produtos()   
programa_rodando = True

while programa_rodando:
    print("----------------")
    print('1 - cadastrar')
    print('2 - listar')
    print('3 - registrar')
    print('4 - repor')
    print('5 - relatório')
    print('6 - sair')
    print("----------------")

    try:
        escolha = int(input("escolha a opcao: "))
    
    except:
        print("erro!")
        continue

    if escolha == 1:
        cadastrar_produto()

    elif escolha == 2:
         listar_produtos()

    elif escolha == 3:
        registrar_compra()

    elif escolha == 4:
        repor_produtos()

    elif escolha == 5:
         relatorio_produtos()

    elif escolha == 6:
        print("Você Encerrou!")
        programa_rodando = False

    else:
        print("escolha uma opcao valida!")