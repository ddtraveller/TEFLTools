'# Guia ba Engenharia Prompt no Afinasaun Parámetru

## Tabela husi Konteúdu
1. [Introdusaun ba Engenharia Prompt](#introdusaun-ba-engenharia-prompt)
2. [Jerasaun Augmentada husi Recuperasaun (RAG)](#gerasaun-augmentada-husi-recuperasaun-rag)
3. [Tipu Prompt no Ezemplu](#tipu-prompt-no-ezemplu)
4. [Afinasaun Parámetru](#afinasaun-parametru)
5. [Téknika Avansadu](#teknika-avansadu)

## Introdusaun ba Engenharia Prompt

Engenharia Prompt mak prátika ida husi dezaina no otimiza prompt entrada ba modelu lian atu jera rezultadu ne'ebé hakarak. Nia involve kria prompt ne'ebé efetivamente komunika tarefa, kontestu, no formatu ne'ebé hakarak ba modelu IA.

## Jerasaun Augmentada husi Recuperasaun (RAG)

RAG mak téknika ida ne'ebé kombina recuperasaun informasaun ho jerasaun testu. Nia recupera informasaun relevante husi baze konhesimentu no inkorpora nia iha prosesu jerasaun.

Ezemplu husi implementasaun RAG:

```python
import openai
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Inisializa modelu no índise
modelu = SentenceTransformer('all-MiniLM-L6-v2')
índise = faiss.IndexFlatL2(384)  # 384 mak dimensaun embedding ba modelu ida-ne'e

# Amostra baze konhesimentu
baze_konhesimentu = [
    "Kapital husi Fransa mak Paris.",
    "Torre Eiffel iha altura 324 metru.",
    "Leonardo da Vinci pinta Mona Lisa.",
    "Muralla Boot husi Xina nian naruk liu 21,000 kilometru."
]

# Kria embedding no aumenta ba índise
embeddings = modelu.encode(baze_konhesimentu)
índise.add(embeddings)

def recupera_kontestu(konsulta, k=2):
    vetor_konsulta = modelu.encode([konsulta])
    _, I = índise.search(vetor_konsulta, k)
    return [baze_konhesimentu[i] for i in I[0]]

def jera_ho_rag(prompt):
    kontestu = recupera_kontestu(prompt)
    prompt_avansadu = f"Kontestu: {' '.join(kontestu)}\n\nPergunta: {prompt}\n\nResposta:"
    
    resposta = openai.Completion.create(
        motor="text-davinci-002",
        prompt=prompt_avansadu,
        max_tokens=100
    )
    return resposta.choices[0].text.strip()

# Ezemplu uza
rezultadu = jera_ho_rag("Saida mak altura husi Torre Eiffel?")
print(rezultadu)
```

Ezemplu ida-ne'e demonstra oinsá implementa sistema RAG simples ho sentence embeddings ba recuperasaun no OpenAI's GPT-3 ba jerasaun.

## Tipu Prompt no Ezemplu

1. Zero-shot Prompts:
   Husu modelu atu halo tarefa laho ezemplu ruma.

   ```
   Klasifika fraze tuir mai hanesan pozitivu, negativu, ka neutral:
   "Filme ida ne'e di'ak, maibé ha'u hare ona ne'ebé di'ak liu."
   ```

2. Few-shot Prompts:
   Fornese ezemplu balun antes husu modelu atu halo tarefa.

   ```
   Tradús Inglés ba Françés:

   Inglés: Hello
   Françés: Bonjour

   Inglés: Goodbye
   Françés: Au revoir

   Inglés: How are you?
   Françés:
   ```

3. Chain-of-Thought Prompts:
   Gia modelu liu husi prosesu razaun pasu husi pasu.

   ```
   Rezolve problema tuir mai ho pasu husi pasu:
   
   John iha masan 5. Nia fo