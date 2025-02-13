# lista = []

# for i in range(15):
#     pergunta = input("Pergunta --> ")
#     alternativa_a = input("alternativa_a --> ")
#     alternativa_b = input("alternativa_b --> ")
#     alternativa_c = input("alternativa_c --> ")
#     alternativa_d = input("alternativa_d --> ")
#     correta = input("Letra correta --> ")
    
#     dict_pergunta = {
#         "pergunta": pergunta ,
#         "alternativas": {
#             "A": alternativa_a,
#             "B": alternativa_b,
#             "C":alternativa_c,
#             "D": alternativa_d
#         },
#         "categoria": 'Gramática e Significado',
#         "correta": correta
#     }
#     lista.append(dict_pergunta)

# print(list)

# with open('perguntas_list.txt', 'w') as file:
#     file.writelines(str(lista))

import pandas as pd
    

lista_perguntas = [
   {
      "pergunta":"Which sentence is grammatically correct?",
      "alternativas":{
         "A":"She don't like coffee.",
         "B":"She doesn't likes coffee.",
         "C":"She don't likes coffee.",
         "D":"She doesn't like coffee."
      },
      "categoria":"Gramatica e Significado",
      "correta":"D"
   },
   {
      "pergunta":"What is the correct order of adjectives in the sentence 'She bought a ___ dress'?",
      "alternativas":{
         "A":"red beautiful silk",
         "B":"silk beautiful red",
         "C":"beautiful red silk",
         "D":"beautiful silk red"
      },
      "categoria":"Gramatica e Significado",
      "correta":"C"
   },
   {
      "pergunta":"Identify the correct use of the past perfect:",
      "alternativas":{
         "A":"By the time we arrived, the movie had started.",
         "B":"By the time we arrive, the movie had started.",
         "C":"By the time we arrived, the movie has started.",
         "D":"By the time we had arrived, the movie started."
      },
      "categoria":"Gramatica e Significado",
      "correta":"A"
   },
   {
      "pergunta":"Choose the correct comparative sentence:",
      "alternativas":{
         "A":"This test is more easier than the last one.",
         "B":"This test is easier than the last one.",
         "C":"This test is much easier from the last one.",
         "D":"This test is the most easier than the last one."
      },
      "categoria":"Gramatica e Significado",
      "correta":"B"
   },
   {
      "pergunta":"Which sentence is incorrect?",
      "alternativas":{
         "A":"She suggested that he should see a doctor.",
         "B":"It's important that he be on time.",
         "C":"I wish he was here now.",
         "D":"If I were you, I wouldn't do that."
      },
      "categoria":"Gramatica e Significado",
      "correta":"C"
   },
   {
      "pergunta":"What is the correct form of the verb in the sentence 'If she ___ earlier, she wouldn't have missed the train'?.",
      "alternativas":{
         "A":"left",
         "B":"has left",
         "C":"had left",
         "D":"was leaving"
      },
      "categoria":"Gramatica e Significado",
      "correta":"C"
   },
   {
      "pergunta":"Identify the correct sentence:",
      "alternativas":{
         "A":"I look forward to hear from you.",
         "B":"I look forward to hearing from you.",
         "C":"I look forward hear from you.",
         "D":"I look forward hearing from you."
      },
      "categoria":"Gramatica e Significado",
      "correta":"B"
   },
   {
      "pergunta":"Which sentence correctly uses \"despite\"?",
      "alternativas":{
         "A":"Despite he was tired, he continued.",
         "B":"Despite of being tired, he continued.",
         "C":"Despite he is tired, he continued.",
         "D":"Despite being tired, he continued."
      },
      "categoria":"Gramatica e Significado",
      "correta":"D"
   },
   {
      "pergunta":"Choose the correct sentence:",
      "alternativas":{
         "A":"She denied to steal the money.",
         "B":"She denied stealing the money.",
         "C":"She denied that she steals the money.",
         "D":"She denied that steal the money."
      },
      "categoria":"Gramatica e Significado",
      "correta":"B"
   },
   {
      "pergunta":"What is the correct indirect question?",
      "alternativas":{
         "A":"Do you know what time is it?",
         "B":"Do you know what time it is?",
         "C":"Do you know what is the time?",
         "D":"Do you know what time does it is?"
      },
      "categoria":"Gramatica e Significado",
      "correta":"B"
   },
   {
      "pergunta":"Which sentence is grammatically correct?",
      "alternativas":{
         "A":"Neither of them have arrived yet.",
         "B":"Neither of them are arriving yet.",
         "C":"Neither of them were arrived yet.",
         "D":"Neither of them has arrived yet."
      },
      "categoria":"Gramatica e Significado",
      "correta":"D"
   },
   {
      "pergunta":"Choose the correct sentence:",
      "alternativas":{
         "A":"She suggested me to go.",
         "B":"She suggested that I go.",
         "C":"She suggested I to go.",
         "D":"She suggested that I went."
      },
      "categoria":"Gramatica e Significado",
      "correta":"B"
   },
   {
      "pergunta":"What is the correct use of \"used to\"?",
      "alternativas":{
         "A":"He used to study late.",
         "B":"He used to studying late.",
         "C":"He use to study late.",
         "D":"He used to studies late."
      },
      "categoria":"Gramatica e Significado",
      "correta":"A"
   },
   {
      "pergunta":"Which sentence is correct?",
      "alternativas":{
         "A":"It depends of the situation",
         "B":"It depends from the situation.",
         "C":"It depends on the situation.",
         "D":"It depends at the situation."
      },
      "categoria":"Gramatica e Significado",
      "correta":"C"
   },
   {
      "pergunta":"Identify the correct conditional sentence:",
      "alternativas":{
         "A":"If you study, you would pass.",
         "B":"If you studied, you will pass.",
         "C":"If you had studied, you would have passed.",
         "D":"If you studied, you pass."
      },
      "categoria":"Gramatica e Significado",
      "correta":"C"
   },
    {
        "pergunta": '''
Texto: "Alice was excited about her new job. She had spent months preparing for the interview and was finally offered the position. However, on her first day, she felt overwhelmed by all the new information and responsibilities."
Pergunta:
What can be inferred about Alice's feelings?
''',
        "alternativas": {
            "A": 'a) She regrets accepting the job.',
            "B": 'b) She was well-prepared but still found the job challenging.',
            "C": 'c) She was not interested in the job.',
            "D": 'd) She found the job easier than expected.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'B'
    },
    {
        "pergunta": '''
Texto:
"Tom looked out the window and saw dark clouds forming. He quickly grabbed his umbrella before leaving the house."
Pergunta:
Why did Tom take his umbrella?
''',
        "alternativas": {
            "A": 'a) Because it was already raining.',
            "B": 'b) Because he thought it might rain.',
            "C": 'c) Because he forgot it outside.',
            "D": 'd) Because he was cold.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'B'
    },
    {
        "pergunta": '''
Texto:
"Lena had always wanted to learn how to play the piano. She finally started lessons last month, and although it was difficult at first, she now enjoys playing simple songs."
Pergunta:
What does the passage suggest about Lena?
''',
        "alternativas": {
            "A": 'a) She found playing the piano too easy.',
            "B": 'b) She gave up after a few lessons.',
            "C": 'c) She made progress and enjoys playing now.',
            "D": 'd) She has played the piano for years.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'C'
    },
    {
        "pergunta": '''
Texto:
"David forgot to set his alarm last night. As a result, he woke up late and had to rush to get ready for work. He missed breakfast and barely caught his bus on time."
Pergunta:
What was the consequence of David forgetting to set his alarm?
''',
        "alternativas": {
            "A": 'a) He arrived at work early.',
            "B": 'b) He had a relaxing morning.',
            "C": 'c) He was late for work.',
            "D": 'd) He had to rush to get ready.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'D'
    },
    {
        "pergunta": '''
Texto:
"Maria loves to read mystery novels. She enjoys trying to figure out who the culprit is before reaching the end of the book."
Pergunta:
What does Maria enjoy most about mystery novels?
''',
        "alternativas": {
            "A": 'a) The romance in the stories.',
            "B": 'b) The challenge of solving the mystery.',
            "C": 'c) The historical settings.',
            "D": 'd) The length of the books.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'B'
    },
    {
        "pergunta": '''
Texto:
"Mark trained for months for the marathon. On the day of the race, he felt nervous but determined. After hours of running, he finally crossed the finish line, exhausted but happy."
Pergunta:
How did Mark feel after the race?
''',
        "alternativas": {
            "A": 'a) Disappointed and sad.',
            "B": 'b) Exhausted but satisfied.',
            "C": 'c) Angry at his performance.',
            "D": 'd) Uninterested in running again.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'B'
    },
    {
        "pergunta": '''
Texto:
"Lisa wanted to bake a cake for her friend’s birthday. She followed the recipe carefully, but she accidentally used salt instead of sugar."
Pergunta:
What is likely to happen to Lisa’s cake?
''',
        "alternativas": {
            "A": 'a) It will taste bad.',
            "B": 'b) It will be extra sweet.',
            "C": 'c) It will be bigger than expected.',
            "D": 'd) It will taste normal.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'A'
    },
    {
        "pergunta": '''
Texto:
"Ben was watching a movie when the power suddenly went out. He sighed, grabbed a flashlight, and started looking for candles."
Pergunta:
Why did Ben get a flashlight?
''',
        "alternativas": {
            "A": 'a) He wanted to find candles because the power went out.',
            "B": 'b) He was scared of the dark.',
            "C": 'c) He wanted to go outside.',
            "D": 'd) He was looking for his phone.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'A'
    },
    {
        "pergunta": '''
Texto:
"John had an important meeting at 9 a.m. He usually wakes up at 7 a.m., but his alarm didn't go off. When he finally woke up, it was already 8:45 a.m."
Pergunta:
What problem did John face?
''',
        "alternativas": {
            "A": 'a) He woke up too early.',
            "B": 'b) He woke up late and risked missing his meeting.',
            "C": 'c) He had too much time before his meeting.',
            "D": 'd) He forgot about his meeting.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'B'
    },
    {
        "pergunta": '''
Texto:
"Emma went to the park to relax. She brought a book and a blanket. However, after a few minutes, the wind started blowing hard, making it difficult to read."
Pergunta:
Why couldn’t Emma read comfortably?
''',
        "alternativas": {
            "A": 'a) It started raining.',
            "B": 'b) The park was too noisy.',
            "C": 'c) The wind was too strong.',
            "D": 'd) She forgot her book at home.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'C'
    },
    {
        "pergunta": '''
Texto:
"Daniel loves coffee, but he ran out of it at home. On his way to work, he stopped at his favorite café to buy a cup."
Pergunta:
Why did Daniel stop at the café?
''',
        "alternativas": {
            "A": 'a) He was meeting a friend.',
            "B": 'b) He wanted to buy coffee.',
            "C": 'c) He was looking for a new café.',
            "D": 'd) He forgot something at home.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'B'
    },
    {
        "pergunta": '''
Texto:
"Sarah’s phone battery was at 2%, and she didn’t have her charger. She had to make an urgent call before her phone died."
Pergunta:
What was Sarah’s main concern?
''',
        "alternativas": {
            "A": 'a) Finding a new phone.',
            "B": 'b) Making a call before her phone turned off.',
            "C": 'c) Watching videos on her phone.',
            "D": 'd) Taking photos with her phone.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'B'
    },
    {
        "pergunta": '''
Texto:
"Kevin’s car broke down on the way to work. He called a tow truck and waited by the side of the road."
Pergunta:
What happened to Kevin?
''',
        "alternativas": {
            "A": 'a) He arrived early at work.',
            "B": 'b) His car stopped working.',
            "C": 'c) He got a new car.',
            "D": 'd) He walked to work.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'B'
    },
    {
        "pergunta": '''
Texto:
"Lucy was at the grocery store when she realized she had left her wallet at home. She had to put back the items she wanted to buy."
Pergunta:
Why couldn’t Lucy buy the items?
''',
        "alternativas": {
            "A": 'a) The store was closed.',
            "B": 'b) She forgot her wallet at home.',
            "C": 'c) She didn’t find what she wanted.',
            "D": 'd) She decided not to buy anything.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'B'
    },
    {
        "pergunta": '''
Texto:
"James was looking forward to the soccer game, but heavy rain caused the match to be canceled."
Pergunta:
Why didn’t James watch the soccer game?
''',
        "alternativas": {
            "A": 'a) He was sick.',
            "B": 'b) He lost his ticket.',
            "C": 'c) The game was canceled due to bad weather.',
            "D": 'd) He forgot about the match.'
        },
        "categoria": 'Compreensão de texto',
        "correta": 'C'
    },
   {
        "pergunta": 'What is a synonym for reluctant?',
        "alternativas": {
            "A": 'Willing',
            "B": 'Hesitant',
            "C": 'Excited',
            "D": 'Confident'
        },
        "categoria": 'Vocabulário',
        "correta": 'B'
    },
    {
        "pergunta": 'Choose the best definition of comprehensive:',
        "alternativas": {
            "A": 'Confunsing',
            "B": 'Thorough',
            "C": 'Small',
            "D": 'Partial'
        },
        "categoria": 'Vocabulário',
        "correta": 'B'
    },
    {
        "pergunta": 'Which word means "to give up"?',
        "alternativas": {
            "A": 'Retain',
            "B": 'Relinquish',
            "C": 'Sustain',
            "D": 'Acquire'
        },
        "categoria": 'Vocabulário',
        "correta": 'B'
    },
    {
        "pergunta": 'Choose the word that fits: She was a very ___ approach to solving problems',
        "alternativas": {
            "A": 'Logical',
            "B": 'Ilogical',
            "C": 'Logic',
            "D": 'Logics'
        },
        "categoria": 'Vocabulário',
        "correta": 'A'
    },
    {
        "pergunta": 'What is the opposite of scarce?',
        "alternativas": {
            "A": 'Plantiful',
            "B": 'Rare',
            "C": 'Limited',
            "D": 'Infrequent'
        },
        "categoria": 'Vocabulário',
        "correta": 'A'
    },
    {
        "pergunta": 'What does "meticulous" mean?',
        "alternativas": {
            "A": 'Careful and precise',
            "B": 'Careless',
            "C": 'Quick and lazy',
            "D": 'Boring'
        },
        "categoria": 'Vocabulário',
        "correta": 'A'
    },
    {
        "pergunta": 'Which word means "to take something less severe"?',
        "alternativas": {
            "A": 'Aggravate',
            "B": 'Alleviate',
            "C": 'Worsen',
            "D": 'Expand'
        },
        "categoria": 'Vocabulário',
        "correta": 'B'
    },
    {
        "pergunta": 'If someone is "apathetic", they are:',
        "alternativas": {
            "A": 'Indifferent',
            "B": 'Enthusiastic',
            "C": 'Depressed',
            "D": 'Angry'
        },
        "categoria": 'Vocabulário',
        "correta": 'A'
    },
    {
        "pergunta": 'What is a synonym for "ambiguous"?',
        "alternativas": {
            "A": 'Clear',
            "B": 'Unclear',
            "C": 'Obvious',
            "D": 'Simple'
        },
        "categoria": 'Vocabulário',
        "correta": 'B'
    },
    {
        "pergunta": 'The word "ephemeral" means:',
        "alternativas": {
            "A": 'Permanent',
            "B": 'Temporary',
            "C": 'Complicated',
            "D": 'Ancient'
        },
        "categoria": 'Vocabulário',
        "correta": 'B'
    },
    {
        "pergunta": 'What is the best synonym for "elaborate":',
        "alternativas": {
            "A": 'Simplistic',
            "B": 'Detailed',
            "C": 'Boring',
            "D": 'Short'
        },
        "categoria": 'Vocabulário',
        "correta": 'B'
    },
    {
        "pergunta": 'Choose the correct sentence:',
        "alternativas": {
            "A": 'The teacher complemented my work.',
            "B": 'The teacher complimented my work.',
            "C": 'The teacher complained my work.',
            "D": 'The teacher comply my work.'
        },
        "categoria": 'Vocabulário',
        "correta": 'B'
    },
    {
        "pergunta": 'What does "feasible" mean?',
        "alternativas": {
            "A": 'Practical',
            "B": 'Impossible',
            "C": 'Imaginary',
            "D": 'Theoretical'
        },
        "categoria": 'Vocabulário',
        "correta": 'A'
    },
    {
        "pergunta": 'What is the correct meaning of "exacerbate"?',
        "alternativas": {
            "A": 'To improve',
            "B": 'To worsen',
            "C": 'To clarify',
            "D": 'To eliminate',
        },
        "categoria": 'Vocabulário',
        "correta": 'B'
    },
    {
        "pergunta": 'What is a synonym for "tedious"?',
        "alternativas": {
            "A": 'Boring',
            "B": 'Exciting',
            "C": 'Dangerous',
            "D": 'Joyful'
        },
        "categoria": 'Vocabulario',
        "correta": 'A'
    }
]

perguntas_pandas = []
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
    perguntas_pandas.append(row)

df = pd.DataFrame(perguntas_pandas)

df.to_csv("perguntas.csv")

print(len(lista_perguntas))


