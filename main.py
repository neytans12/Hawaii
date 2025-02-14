# Importando bibliotecas/funcões de bibliotecas
from requests import get
import os
import matplotlib.pyplot as plt
import time
from datetime import date
import menu
import pandas as pd
import json

if not os.path.exists("dados"):
    os.mkdir("dados")

caminho_csv = os.path.join("dados", "perguntas.csv")

if not os.path.exists(caminho_csv):
    os.system("python3 perguntas.py")
    os.remove("perguntas.py")


# A principio, sei que faria sentido criptografar tanto o arquivo perguntas.py quanto o perguntas.csv, haja vista que esses arquivos contem as respostas de todas as questões, mas não o fiz para facilitar a analse do codigo. Poderia implementar essa função em um momento futuro.


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
    else:
        print("Seu notebook está vazio.")

def delete_notebook(caminho_notebook):
    if os.path.exists(caminho_notebook):
        os.remove(caminho_notebook)
        print("Feito")
    else:
        print("Seu notebook não existe existe...")
    

def gerar_quiz_diario(caminho_perguntas, caminho_acertos): # GEra as funções que serão usadas no Quiz
    # Carregar o CSV
    df = pd.read_csv(caminho_perguntas)
    df = df.drop(columns=['Unnamed: 0'])
    gramatica = df[df["categoria"] == "Gramatica e Significado"].sample(n=3, random_state=None) # Selecionar 3 perguntas aleatórias
    vocab = df[df["categoria"] == "Vocabulario"].sample(n=3, random_state=None)
    compr = df[df["categoria"] == "Compreensao de texto"].sample(n=3, random_state=None)

    # Converter as perguntas selecionadas em uma lista de dicionários
    perguntas_selec = []

    for i in range(3):
        for o in [gramatica, vocab, compr]:
            dict_pergunta = {"Pergunta": o["pergunta"].values[i],
                            "A": o["A"].values[i],
                            "B": o["B"].values[i],
                            "C": o["C"].values[i],
                            "D": o["D"].values[i],
                            "Categoria": o["categoria"].values[i],
                            "Correta": o["correta"].values[i]}
            perguntas_selec.append(dict_pergunta)
    
    # Remover as perguntas selecionadas do DataFrame original
    df = df.drop(gramatica.index)
    df = df.drop(compr.index)
    df = df.drop(vocab.index)
    df = df.reset_index(drop=True)
    # Salvar o DataFrame atualizado de volta ao CSV
    df.to_csv(caminho_perguntas)

    play_quiz(perguntas_selec, caminho_acertos)
    

def play_quiz(perguntas_select, caminho_acertos):
    questoes_acertadas = {"Vocabulario": 0,
                          "Gramatica e Significado": 0,
                          "Compreensao de texto": 0}
    for i, o in enumerate(perguntas_select):
        menu_pergunta = f'''
{i+1}) {o["Pergunta"]}
    A){o["A"]}
    B){o["B"]}
    C){o["C"]}
    D){o["D"]}
        '''
        
        print(menu_pergunta)
        user_resp = input("Sua resposta --> ").strip().capitalize()
        if user_resp != o["Correta"]:
            print("RESPOSTA INCORRETA...")
        else:
            questoes_acertadas[o["Categoria"]] += 1
            print("RESPOSTA CORRETA...")
            
                


    print("Fim do quiz. Volte amanhã :)")

    caminho_log = os.path.join("dados", "log.csv")

    if os.path.exists(caminho_log):
        df_log = pd.read_csv(caminho_log)
        
        df_log = pd.concat([df_log, pd.DataFrame({"Logs": [hoje]})], ignore_index=True, join="inner")
        
        df_log.to_csv(caminho_log)
    else:
        df_log = pd.DataFrame({"Logs": [hoje]})
        df_log.to_csv(caminho_log)



    if os.path.exists(caminho_acertos):
        with open(caminho_acertos, 'r') as file:
            acertos = json.load(file)
        for i, o in acertos.items():
            acertos[i] += questoes_acertadas[i]
        with open(caminho_acertos, 'w') as file:
            json.dump(acertos,file)
    else:
        with open(caminho_acertos, 'w') as file:
            json.dump(questoes_acertadas,file)


def gerar_estatisticas(caminho_acertos):
    if os.path.exists(caminho_acertos):
        with open(caminho_acertos, 'r') as file:
            acertos = json.load(file)
        
        categorias = list(acertos.keys())
        valores = list(acertos.values())
        plt.rcParams['figure.figsize'] = (8.0, 6.0)
        plt.rcParams['figure.dpi'] = 150
        plt.title('Desempenho durante os quizes diarios', fontsize=10)
        plt.xlabel('Categorias')
        plt.ylabel('Acertos')
        plt.bar(categorias, valores, color='red', edgecolor='black',width=0.3)
        plt.show()
    else:
        print("Parece que você ainda não comcluiu nenhum quiz diario...")

        


caminho_notebook = os.path.join("dados", "notebook.csv") # Criando um caminho_notebook valido tanto para windows quanto para linux
caminho_perguntas = os.path.join("dados", "perguntas.csv")

caminho_acertos = os.path.join("dados", "acertos.json")

caminho_log = os.path.join("dados", "log.csv")

hoje = date.today().strftime("%b-%d-%Y")



while True:
    print(menu.logo)
    user_act = int(input(menu.opcoes))
    match user_act:
        case 1:
            palavra = input("Digite a palavra: ")
            req_mostrar_palavra(palavra, caminho_notebook)
            print("Voltando ao menu...")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
        case 2:
            acessar_notebook(caminho_notebook)
            print("Voltando ao menu...")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
        case 3:
            delete_notebook(caminho_notebook)
            print("Voltando ao menu...")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
        case 4:
            
            if os.path.exists(caminho_log):
                df_log = pd.read_csv(caminho_log)
                if hoje in df_log["Logs"].values:
                    print("Você ja fez o quiz diario. Volte amanhã :)")
                else:
                    gerar_quiz_diario(caminho_perguntas, caminho_acertos)
            else:
                gerar_quiz_diario(caminho_perguntas, caminho_acertos)
            print("Voltando ao menu...")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
        case 5:
            gerar_estatisticas(caminho_acertos)
            print("Voltando ao menu...")
            time.sleep(3)

            os.system('cls' if os.name == 'nt' else 'clear')
        case 6:
            print("Até a proxima :)")
            time.sleep(3)
            break
        case _:
            print("Opção invaida...")
            print("Voltando ao menu...")
            time.sleep(3)