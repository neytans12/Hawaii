# Importando bibliotecas/funcões de bibliotecas
from requests import get
import os
import pandas as pd

if not os.path.exists("dados"):
    os.mkdir("dados")

freeDictionaryAPI = "https://api.dictionaryapi.dev/api/v2/entries/en/" # Link usado para emtrar em contato com API

# Requisitar e mostrar definição de palavra:
def req_mostrar_palavra(palavra):
    # Requisitando dados da API
    # A função get retorna um objeto (não vimos isso em aula então nao entrarei em detalhes)
    # Ao chamar o metodo text, obtemos um string com todo o texto acessado atraves da URL
    # Usei a função eval para transformar esse string em uma expressão que o python entenda (uma lista, alias)
    list_resposta = eval(get(freeDictionaryAPI+palavra).text) 
    if type(list_resposta) != list:
        # Caso o link retorne qualquer coisa que não seja uma lista, a palavra não foi encontrada
        print("Essa palavra não foi encontrada...")
    else:
        list_resposta = list_resposta[0] # O que nos interessa é o primeiro elemento dessa lista (um dicionario)
        # Navegar por esse dicionario pode ser um pouco complexo. Terei que explicar pessoalmente
        print(f"{list_resposta["word"].title()}\n--- ---\nDefinition")
        
        for i in list_resposta["meanings"]:
            print(f"{i["partOfSpeech"]}:")
            for o in i["definitions"]:
                print(f"- {o["definition"]}")
            print("\n")
        while True:
            salvar_palavra = input("Deseja salvar essa palavra em seu notebook (s/n)?").capitalize()
            # Usei o match/case para tornar o codigo mais enxuto 
            match salvar_palavra:
                case "S":
                    salvar_palavra_notebook(palavra.capitalize())
                    break
                case "N":
                    break
                case _:
                    print("Opção invalida.")
    

        enter = input("Pressione enter para sair do dicionario ")
        os.system('cls' if os.name == 'nt' else 'clear')
# Salvar palavra em notebook
def salvar_palavra_notebook(palavra):
    caminho = os.path.join("dados", "notebook.csv") # Criando um caminho valido tanto para windows quanto para linux
    if os.path.exists(caminho):
        # Se o caminho já existe, significa que o dicionario ja foi criado
        # Nesse caso, podemos apenas ler o arquivo CSV e fazer as devidas operações
        df_notebook = pd.read_csv(caminho) # Lendo o arquivo
        nova_palavra= pd.DataFrame({"Palavras": [palavra]}) # Criando daatframo com nova palavra

        df_notebook = pd.concat([df_notebook, nova_palavra], ignore_index=True, join="inner")# Unindo os dois dataframes
        df_notebook.to_csv(caminho) # Escrevendo arquivo
    else:
        # No segundo caso, teremos que criar o arquivo
        df_notebook = pd.DataFrame({"Palavras": [palavra]})
        df_notebook.to_csv(caminho)
        
def acessar_notebook():
    caminho_csv = os.path.join('dados', 'notebook.csv')

    if os.path.exists(caminho_csv):
        df_notebook = pd.read_csv(caminho_csv)
        valores = list(df_notebook["Palavras"]) # lista com as palavras
        if len(valores) == 0:
            print("Seu notebook está vazio.")
        else:
            for i in valores:
                print(f"- {i};")
        enter = input("Pressione enter para sair do dicionario ")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Seu notebook está vazio.")


print("Bem-vindo ao Hawaii.")

while True:
    user_act = int(input("Escolha uma das alternativas:\n1- Pesquisar uma palavra;\n2- Mostrar notebook;\n4- Sair\n--> "))
    match user_act:
        case 1:
            palavra = input("Digite a palavra: ")

            req_mostrar_palavra(palavra)
        case 2:
            # Em desenvolvimento, guerreiro...
            acessar_notebook()
        case 4:
            print("Até a proxima :)")
            break
