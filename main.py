# Importando bibliotecas/funcões de bibliotecas
from requests import get
import os
import pandas as pd
import random
from datetime import date
import menu


if not os.path.exists("dados"):
    os.mkdir("dados")

freeDictionaryAPI = "https://api.dictionaryapi.dev/api/v2/entries/en/" # Link usado para emtrar em contato com API

# Requisitar e mostrar definição de palavra:
def req_mostrar_palavra(palavra, caminho_notebook):
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
                    salvar_palavra_notebook(palavra.capitalize(), caminho_notebook)
                    break
                case "N":
                    break
                case _:
                    print("Opção invalida.")
    

        enter = input("Pressione enter para sair do dicionario ")
        os.system('cls' if os.name == 'nt' else 'clear')
# Salvar palavra em notebook
def salvar_palavra_notebook(palavra, caminho_notebook):
    if os.path.exists(caminho_notebook):
        # Se o caminho_notebook já existe, significa que o dicionario ja foi criado
        # Nesse caso, podemos apenas ler o arquivo CSV e fazer as devidas operações
        df_notebook = pd.read_csv(caminho_notebook) # Lendo o arquivo
        nova_palavra= pd.DataFrame({"Palavras": [palavra]}) # Criando daatframo com nova palavra

        df_notebook = pd.concat([df_notebook, nova_palavra], ignore_index=True, join="inner")# Unindo os dois dataframes
        df_notebook.to_csv(caminho_notebook) # Escrevendo arquivo
    else:
        # No segundo caso, teremos que criar o arquivo
        df_notebook = pd.DataFrame({"Palavras": [palavra]})
        df_notebook.to_csv(caminho_notebook)
        
def acessar_notebook(caminho_notebook):

    if os.path.exists(caminho_notebook):
        df_notebook = pd.read_csv(caminho_notebook)
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

def delete_notebook(caminho_notebook):
    if os.path.exists(caminho_notebook):
        os.remove(caminho_notebook)
        print("Feito")
    else:
        print("Seu notebook não existe existe...")
    

def gerar_quiz_diario(caminho_perguntas): # GEra as funções que serão usadas no Quiz
    # Carregar o CSV
    df = pd.read_csv(caminho_perguntas)
    df = df.drop(columns=['Unnamed: 0'])

    # Selecionar 3 perguntas aleatórias
    perguntas_selecionadas = df.sample(n=3, random_state=None)

    # Converter as perguntas selecionadas em uma lista de dicionários
    quiz = perguntas_selecionadas.to_dict(orient='records')

    # Remover as perguntas selecionadas do DataFrame original
    df = df.drop(perguntas_selecionadas.index)
    df = df.reset_index(drop=True)
    # Salvar o DataFrame atualizado de volta ao CSV
    df.to_csv(caminho_perguntas)

    print(quiz)

def play_quiz(perguntas_select):

    for i, o in enumerate(perguntas_select):
        menu_pergunta = f'''
{i+1}) {o["Pergunta"]}
    A){o["Alternativa A"]}
    B){o["Alternativa B"]}
    C){o["Alternativa C"]}
    D){o["Alternativa D"]}
        '''
        
        print(menu_pergunta)
        user_resp = input("Sua resposta --> ").strip().capitalize()
        if user_resp != o["Correta"]:
            print("RESPOSTA INCORRETA...")
        else:
            print("RESPOSTA CORRETA...")
    print("Fim do quiz. Volte amanhã :)")
    global fez_quiz_diario
    fez_quiz_diario = True


caminho_notebook = os.path.join("dados", "notebook.csv") # Criando um caminho_notebook valido tanto para windows quanto para linux
caminho_perguntas = os.path.join("dados", "perguntas.csv")


hoje = date.today().strftime("%b-%d-%Y")


print(menu.logo)

fez_quiz_diario = False

while True:
    user_act = int(input(menu.opcoes))
    match user_act:
        case 1:
            palavra = input("Digite a palavra: ")
            req_mostrar_palavra(palavra, caminho_notebook)
        case 2:
            acessar_notebook(caminho_notebook)
        case 3:
            delete_notebook(caminho_notebook)
        case 4:
            if fez_quiz_diario:
                print("Você ja fez o quiz diario. Volte amanhã :)")
            else:
                gerar_quiz_diario(caminho_perguntas)
                fez_quiz_diario = True
        case 5:
            print("Até a proxima :)")
            break
