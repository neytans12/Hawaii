import pandas as pd


lista_perguntas = [
    {
        "pergunta": "Qual é o significado de 'dog' em português?",
        "alternativas": {
            "A": "Gato",
            "B": "Cachorro",
            "C": "Pássaro",
            "D": "Peixe",
        },
        "correta": "B"
    },
    {
        "pergunta": "Qual palavra é um sinônimo de 'happy'?",
        "alternativas": {
            "A": "Sad",
            "B": "Angry",
            "C": "Tired",
            "D": "Joyful",
        },
        "correta": "D"
    },
    {
        "pergunta": "O que significa 'blue' em português?",
        "alternativas": {
            "A": "Vermelho",
            "B": "Amarelo",
            "C": "Verde",
            "D": "Azul",
        },
        "correta": "D   "
    },
    {
        "pergunta": "Qual é a tradução correta da palavra "overwhelming" para o português?"
        "alternativas": {
            "A": "Tranquilo",
            "B": " Impressionante",
            "C": "Irrelevante",
            "D": "Insignificante",
         }
         "correta": "B"
    },
    {
        "pergunta": "Qual das seguintes palavras pode substituir "happy" sem mudar o significado da frase?"
        "alternativas": {
            "A": "Miserable",
            "B": "Cheerful",
            "C": "Furious",
            "D": "Anxious",
         }
         "correta": "B"
    },
    { 
        "pergunta": "Qual palavras completa corretamente a frase "She was feeling very ___ after working for ten hours straight"?" 
        "alternativas": {
            "A": "Exhausted",
            "B": "Delighted",
            "C": "Confused",
            "D": "Excited",
        }
        "correta": "A"
    },
    { 
        "pergunta": "Qual é o antônimo da palavra generous?"
        "alternativas": {
            "A": "Selfish",
            "B": "Kind",
            "C": Friendly",
            "D": "Thoughtful",
        }
        "correta": "A"
    },
    { 
        "pergunta": "O que significa a expressão break the ice?"
         "alternativas": {
             "A": "Iniciar uma conversa para aliviar o clima tenso",
             "B": "Terminar um relacionamento",
             "C": "Destruir algo frágil",
             "D": "Ficar nervoso"
       }
       "correta": "A"
    },
    {
        "pergunta": "Qual dessas palavras é um substantivo?",
        "alternativas": {
            "A": "Run",
            "B": "Beautiful",
            "C": "Table",
            "D": "Quickly",
        },
        "correta": "C"
    },
    {
        "pergunta": "Qual palavra melhor completa a frase: 'She ____ to school every day.'?",
        "alternativas": {
            "A": "Go",
            "B": "Going",
            "C": "Goes",
            "D": "Gone",
        },
        "correta": "C"
    },
    {
        "pergunta": "O que significa 'chair' em português?",
        "alternativas": {
            "A": "Cadeira",
            "B": "Mesa",
            "C": "Sofá",
            "D": "Janela",
        },
        "correta": "A"
    },
    {
        "pergunta": "Qual é o antônimo de 'fast'?",
        "alternativas": {
            "A": "Slow",
            "B": "Quick",
            "C": "Speed",
            "D": "Move",
        },
        "correta": "A"
    },
    {
        "pergunta": "O que significa 'book' em português?",
        "alternativas": {
            "A": "Caderno",
            "B": "Revista",
            "C": "Livro",
            "D": "Papel",
        },
        "correta": "C"
    },
    {
        "pergunta": "Qual das palavras abaixo é um adjetivo?",
        "alternativas": {
            "A": "Jump",
            "B": "Beautiful",
            "C": "Table",
            "D": "Run",
        },
        "correta": "B"
    },
    {
        "pergunta": "Qual é o significado de 'big' em português?",
        "alternativas": {
            "A": "Pequeno",
            "B": "Grande",
            "C": "Médio",
            "D": "Largo",
        },
        "correta": "B"
    },
    {
        "pergunta": "Qual dessas palavras é um verbo?",
        "alternativas": {
            "A": "House",
            "B": "Car",
            "C": "Blue",
            "D": "Sing",
        },
        "correta": "D"
    },
    {
        "pergunta": "Qual é o plural de 'mouse' em inglês?",
        "alternativas": {
            "A": "Mouses",
            "B": "Mices",
            "C": "Mice",
            "D": "Mousees",
        },
        "correta": "C"
    },
    {
        "pergunta": "Qual palavra completa a frase: 'I have a ____ idea.'?",
        "alternativas": {
            "A": "Good",
            "B": "Well",
            "C": "Nicely",
            "D": "Better",
        },
        "correta": "A"
    },
    {
        "pergunta": "Qual dessas palavras é um pronome pessoal?",
        "alternativas": {
            "A": "He",
            "B": "House",
            "C": "Green",
            "D": "Run",
        },
        "correta": "A"
    },
    {
        "pergunta": "Qual dessas palavras é um advérbio?",
        "alternativas": {
            "A": "Quickly",
            "B": "Quick",
            "C": "Quicker",
            "D": "Fast",
        },
        "correta": "A"
    },
    {
        "pergunta": "Qual é o significado de 'cold' em português?",
        "alternativas": {
            "A": "Quente",
            "B": "Frio",
            "C": "Gelado",
            "D": "Morno",
        },
        "correta": "B"
    },
    {
        "pergunta": "Qual é a forma correta para completar a frase: 'She ____ to school every day.'?",
        "alternativas": {
            "A": "go",
            "B": "goes",
            "C": "going",
            "D": "gone",
        },
        "correta": "B"
    },
    {
        "pergunta": "Qual das frases abaixo está gramaticalmente correta?",
        "alternativas": {
            "A": "She don’t like apples.",
            "B": "She didn't like apples.",
            "C": "She not like apples.",
            "D": "She doesn’t like apples.",
        },
        "correta": "D"
    },
    {
        "pergunta": "Qual palavra é um pronome possessivo?",
        "alternativas": {
            "A": "He",
            "B": "His",
            "C": "Him",
            "D": "Her",
        },
        "correta": "B"
    },
    {
        "pergunta": "Qual das opções completa corretamente a frase: 'If I ____ you, I would apologize.'?",
        "alternativas": {
            "A": "was",
            "B": "were",
            "C": "am",
            "D": "is",
        },
        "correta": "B"
    },
    {
        "pergunta": "Qual dessas palavras é um verbo modal?",
        "alternativas": {
            "A": "Can",
            "B": "Is",
            "C": "Has",
            "D": "Will be",
        },
        "correta": "A"
    },
    {
        "pergunta": "Qual das frases está no tempo verbal Present Perfect?",
        "alternativas": {
            "A": "She has visited Paris.",
            "B": "She visits Paris.",
            "C": "She will visit Paris.",
            "D": "She is visiting Paris.",
        },
        "correta": "A"
    },
    {
        "pergunta": "Qual a função de 'quickly' na frase: 'She runs quickly.'?",
        "alternativas": {
            "A": "Verbo",
            "B": "Substantivo",
            "C": "Adjetivo",
            "D": "Advérbio",
        },
        "correta": "D"
    },
    {
        "pergunta": "Qual opção completa corretamente a frase: 'By the time we arrived, they ____ already left.'?",
        "alternativas": {
            "A": "have",
            "B": "had",
            "C": "has",
            "D": "were",
        },
        "correta": "B"
    },
    {
        "pergunta": "Qual é a forma correta do passado simples do verbo 'to eat'?",
        "alternativas": {
            "A": "Eaten",
            "B": "Ate",
            "C": "Eating",
            "D": "Eats",
        },
        "correta": "B"
    },
    {
        "pergunta": "Qual das frases está na voz passiva?",
        "alternativas": {
            "A": "She wrote the book.",
            "B": "The book was written by her.",
            "C": "She writes a book.",
            "D": "She is writing a book.",
        },
        "correta": "B"
    },
    {
        "pergunta": "Qual é o erro na frase: 'She didn’t went to school yesterday.'?",
        "alternativas": {
            "A": "O verbo 'went' está incorreto; deveria ser 'go'.",
            "B": "O verbo 'went' está incorreto; deveria ser 'gone'.",
            "C": "O verbo 'went' está incorreto; deveria ser 'goes'.",
            "D": "O verbo 'went' está incorreto; deveria ser 'go'.",
        },
        "correta": "A"
    },
    {
        "pergunta": "Qual das frases está na forma interrogativa?",
        "alternativas": {
            "A": "She is reading a book.",
            "B": "She read a book.",
            "C": "Is she reading a book?",
            "D": "She was reading a book.",
        },
        "correta": "C"
    },
    {
        "pergunta": "Qual das frases está correta no futuro simples?",
        "alternativas": {
            "A": "She will go to the party.",
            "B": "She goes to the party tomorrow.",
            "C": "She went to the party next week.",
            "D": "She go to the party next week.",
        },
        "correta": "A"
    },
    {
        "pergunta": "Qual das frases usa a estrutura correta do condicional tipo 1?",
        "alternativas": {
            "A": "If it rains, we would stay home.",
            "B": "If it rains, we will stay home.",
            "C": "If it rained, we will stay home.",
            "D": "If it rain, we will stay home.",
        },
        "correta": "B"
    },
    {
        "pergunta": "Qual palavra completa corretamente a frase: 'She is interested ____ learning new languages.'?",
        "alternativas": {
            "A": "on",
            "B": "at",
            "C": "in",
            "D": "with",
        },
        "correta": "C"
    },
    {
        "pergunta": "Qual das frases está na forma negativa do Present Simple?",
        "alternativas": {
            "A": "She don’t like coffee.",
            "B": "She doesn’t like coffee.",
            "C": "She didn’t like coffee.",
            "D": "She not like coffee.",
        },
        "correta": "B"
    },
        {
        "pergunta": "Qual é a ideia principal do seguinte trecho? 'Many people believe that reading books is the best way to gain knowledge. However, others argue that practical experience is more valuable than theoretical learning.'",
        "alternativas": {
            "A": "A importância da prática sobre a teoria.",
            "B": "A leitura é a única forma de aprender.",
            "C": "A experiência prática não é útil.",
            "D": "Livros são inúteis para adquirir conhecimento.",
        },
        "correta": "A"
    },
    {
        "pergunta": "Qual título seria mais apropriado para um texto que discute os benefícios da tecnologia na educação?",
        "alternativas": {
            "A": "Os desafios da agricultura moderna",
            "B": "O impacto da tecnologia na aprendizagem",
            "C": "A evolução dos esportes olímpicos",
            "D": "Como cozinhar massas perfeitamente",
        },
        "correta": "B"
    },
    {
        "pergunta": "Após ler o seguinte parágrafo, qual alternativa representa a conclusão mais lógica? 'John trained hard for months, waking up early every day and following a strict diet. On the day of the competition, he performed exceptionally well and won first place.'",
        "alternativas": {
            "A": "John se arrependeu de ter treinado tanto.",
            "B": "John perdeu a competição.",
            "C": "O treinamento de John valeu a pena.",
            "D": "John decidiu parar de competir.",
        },
        "correta": "C"
    },
    {
        "pergunta": "No trecho: 'Despite the rain, they decided to go for a walk.' O que a palavra 'Despite' indica?",
        "alternativas": {
            "A": "Causa",
            "B": "Condição",
            "C": "Contraste",
            "D": "Tempo",
        },
        "correta": "C"
    },
    {
        "pergunta": "Qual a melhor opção para substituir a expressão 'very tired' no trecho: 'After the marathon, he was very tired'?",
        "alternativas": {
            "A": "Exhausted",
            "B": "Sleepy",
            "C": "Energetic",
            "D": "Hungry",
        },
        "correta": "A"
    },
    {
        "pergunta": "Qual das frases melhor resume a seguinte passagem? 'The internet has changed the way people communicate, making it easier to stay in touch, share ideas, and access information.'",
        "alternativas": {
            "A": "A internet tornou a comunicação mais difícil.",
            "B": "A internet facilitou a comunicação e o acesso à informação.",
            "C": "A internet impede as pessoas de se comunicarem corretamente.",
            "D": "A internet é uma ferramenta inútil para a comunicação.",
        },
        "correta": "B"
    },
    {
        "pergunta": "Qual alternativa indica o tom do seguinte trecho? 'The author strongly criticizes the government's decision to cut education funding, arguing that it will have negative consequences for future generations.'",
        "alternativas": {
            "A": "Neutro",
            "B": "Crítico",
            "C": "Otimista",
            "D": "Humorístico",
        },
        "correta": "B"
    },
    {
        "pergunta": "O que pode ser inferido a partir da seguinte frase? 'By the time we arrived at the theater, the movie had already started.'",
        "alternativas": {
            "A": "Eles chegaram antes do filme começar.",
            "B": "O filme já estava em andamento quando chegaram.",
            "C": "Eles perderam apenas o final do filme.",
            "D": "O filme ainda não havia começado quando chegaram.",
        },
        "correta": "B"
    },
    {
        "pergunta": "Qual das palavras a seguir melhor descreve o sentimento expresso na frase: 'She was thrilled when she received the good news'?",
        "alternativas": {
            "A": "Angry",
            "B": "Excited",
            "C": "Confused",
            "D": "Sad",
        },
        "correta": "B"
    },
    {
        "pergunta": "Qual das alternativas abaixo melhor resume a ideia do trecho? 'Eating a balanced diet and exercising regularly are essential for maintaining good health.'",
        "alternativas": {
            "A": "Uma dieta balanceada e exercícios são importantes para a saúde.",
            "B": "Evitar exercícios pode melhorar a saúde.",
            "C": "Comer qualquer tipo de comida é suficiente para ser saudável.",
            "D": "Exercícios físicos são prejudiciais à saúde.",
        },
        "correta": "A"
    },
    {
        "pergunta": "Qual é a mensagem principal do seguinte trecho? 'The rapid advancement of technology has led to many changes in the workplace, making tasks more efficient but also reducing the number of available jobs.'",
        "alternativas": {
            "A": "A tecnologia não afeta o mercado de trabalho.",
            "B": "A tecnologia traz mais empregos para todos.",
            "C": "A tecnologia melhora a eficiência, mas reduz empregos.",
            "D": "A tecnologia faz as tarefas mais difíceis e lentas.",
        },
        "correta": "C"
    },
    {
        "pergunta": "Qual título seria mais apropriado para um texto que discute o impacto do aquecimento global na biodiversidade?",
        "alternativas": {
            "A": "Mudanças no clima e suas consequências ecológicas",
            "B": "A ascensão das novas tecnologias",
            "C": "O crescimento das populações urbanas",
            "D": "A preservação dos ecossistemas marinhos",
        },
        "correta": "A"
    },
    {
        "pergunta": "Após ler o seguinte parágrafo, qual alternativa representa a conclusão mais lógica? 'Maria estudou intensamente para o exame, revisando suas anotações e resolvendo exercícios. Quando chegou o dia da prova, ela se sentiu confiante e preparada.'",
        "alternativas": {
            "A": "Maria ficou nervosa durante o exame.",
            "B": "Maria não estudou o suficiente para o exame.",
            "C": "O estudo de Maria a ajudou a se sentir pronta para o exame.",
            "D": "Maria não conseguiu completar a prova.",
        },
        "correta": "C"
    },
    {
        "pergunta": "No trecho: 'Although he was tired, he continued to work late into the night.' O que a palavra 'Although' indica?",
        "alternativas": {
            "A": "Causa",
            "B": "Condição",
            "C": "Contraste",
            "D": "Tempo",
        },
        "correta": "C"
    },
    {
        "pergunta": "Qual a melhor opção para substituir a expressão 'really hungry' no trecho: 'After the long hike, they were really hungry'?",
        "alternativas": {
            "A": "Ravenous",
            "B": "Full",
            "C": "Energetic",
            "D": "Thirsty",
        },
        "correta": "A"
    },
    {
        "pergunta": "Qual das frases melhor resume a seguinte passagem? 'Social media platforms have become a powerful tool for individuals and businesses alike, enabling faster communication and access to a global audience.'",
        "alternativas": {
            "A": "As mídias sociais dificultam a comunicação.",
            "B": "As mídias sociais permitem uma comunicação mais rápida e global.",
            "C": "As mídias sociais são ineficazes para negócios.",
            "D": "As mídias sociais não têm impacto no comércio.",
        },
        "correta": "B"
    },
    { 
        "pergunta": "Choose the correct verb tense to complete the sentence: By the time we arrived, they ___ dinner"
        "alternativas": {
            "A": "Eat",
            "B": "Were eating",
            "C": "Had eaten",
            "D": "Will eat",
        } 
        "correta": "C"
    },
    {
       "pergunta": "Choose the correct verb tense to complete the sentence: While she ____ a book, her brother was watching TV"
       "alternativas": {
           "A": "Read",
           "B": "Reads",
           "C": "Was reading",
           "D": "Was read",
       }
       "correta": "C"
   },
   {
      "pergunta": "Identifique o verbo na frase: The dog barked loudly at the stranger"
      "alternativas": {
          "A": "The",
          "B": "Dog" 
          "C": "Barked",
          "D": "Loudly",
      }
      "correta": "C"
  },
  { 
      "pergunta": "Qual palavra é um advérbio na frase: She quickly finished her homework and went outside"
       "alternativas": {
           "A": "She",
           "B": "Quickly",
           "C": "Finished",
           "D": "Homework",
      
      }
      "correta": "C"
  },
  { 
      "pergunta": "Escolha a preposição correta para completar a frase: She is very good ___ playing piano"
       "alternativas": {
           "A": "In",
           "B": "At",
           "C": "On",
           "D": "With",
     
     }
     "correta": "B"
 },
 {    
     "pergunta": "A partir do texto a seguir, o que Sarah estava fazendo no pôr do sol?" 'The sun was setting, and the sky turned a deep shade of orange. Sarah walked along the beach, enjoying the peaceful moment. She felt grateful for the quiet and the beauty of nature around her.'
     "alternativas": {
         "A": "Taking a walk in the park",
         "B": "Sitting in her house",
         "C": "Walking along the beach",
         "D": "Watching the sunset from her window",

    }
    "correta": "C"
 },
 {
     "pergunta": "A partir do texto a seguir, como James se sentiu ao encontrar a moeda?" 'James couldn't believe his luck when he found an old coin in the garden. He had been digging for hours, and suddenly, something shiny appeared in the soil.'
     "alternativas": {
         "A": "Angry",
         "B": "Surprised",
         "C": "Sad",
         "D": "Nervous",

     }
     "correta": "B"
 },
 {
    "pergunta": "A partir do texto a seguir, o que aconteceu na livraria?"'The library was quiet except for the soft sound of pages turning. Students were scattered around, reading or studying, while the librarian moved silently between the rows of books.'
    "alternativas": {
        "A": "There was a loud noise",
        "B": "People were reading or studying",
        "C": "The librarian was talking to everyone",
        "D": "The students were playing games",

    }
    "correta": "B"
 },
 { 
    "pergunta": "A partir do texto a seguir, qual a atmosfera mais provável do restaurante? 'The restaurant was packed with people, and the air smelled of delicious food. The waiter greeted us with a warm smile and led us to our table by the window.'
    "alternativa": {
       "A": "Quiet and empty",
       "B": "Packed and lively",
       "C": "Dark and cold",
       "D": "Messy and disorganized",
  
   }
   "correta": "B"
},
{ 
    "pergunta": "A partir do texto a seguir, qual a atitude da equipe em relação à chuva?" 'Despite the heavy rain, the team decided to continue playing. They were determined to finish the match, even though the field was becoming slippery.'
    "alternativas": {
        "A": "They want to stop playing",
        "B": "They are determined to keep playing.",
        "C": "They are afraid of getting wet.",
        "D": "They think the rain is not important.",
    }
    "correta": "B"
},
]

for index, dic in enumerate(lista_perguntas[0:17]):
    dic.update({"categoria": "Vocabulario"})

for index, dic in enumerate(lista_perguntas[16:33]):
    dic.update({"categoria": "Gramatica e Significado"})

for index, dic in enumerate(lista_perguntas[32::]):
    dic.update({"categoria": "Compreensão de texto"})


perguntas_normalizadas = []
for pergunta in lista_perguntas:
    row = {
        'pergunta': pergunta['pergunta'],
        'A': pergunta['alternativas']['A'],
        'B': pergunta['alternativas']['B'],
        'C': pergunta['alternativas']['C'],
        'D': pergunta['alternativas']['D'],
        'categoria': pergunta['categoria'],
        'correta': pergunta['correta']
    }
    perguntas_normalizadas.append(row)

df = pd.DataFrame(perguntas_normalizadas)

# Salvar como CSV
df.to_csv('perguntas.csv')



print(len(lista_perguntas))