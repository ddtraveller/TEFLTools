"Iha ne'e rekursu kompletu ida kona ba dokumentasaun no tutorial OpenAI nian ba Unidade 8 husi ita-nia kursu:

# Dokumentasaun no Tutorial OpenAI: Rekursu Kompletu

## 1. Introdusaun ba OpenAI

OpenAI mak laboratóriu peskiza intelijénsia artificial ne'ebé lidera, ne'ebé konsiste korpórasiun profitabel OpenAI LP no nia kompañia inan, kompañia non-profit OpenAI Inc. Sira ne'e konhesidu tanba dezenvolve model no teknolojia AI ne'ebé avansadu, ne'ebé inklui série GPT (Generative Pre-trained Transformer), DALL-E, no Codex.

## 2. Aksesu ba Rekursu OpenAI nian

- Website prinsipál: https://openai.com/
- Dokumentasaun: https://platform.openai.com/docs/introduction
- Referénsia API: https://platform.openai.com/docs/api-reference
- OpenAI Cookbook: https://github.com/openai/openai-cookbook

## 3. Model no Teknolojia OpenAI Sira-ne'ebé Importante

### 3.1 GPT (Generative Pre-trained Transformer)
- Versaun foun: GPT-4
- Kapasidade: Prosesamentu língua naturál, jerasaun textu, tradusaun, rezumu, no liu tan
- Dokumentasaun: https://platform.openai.com/docs/models/gpt-4

### 3.2 DALL-E
- Kapasidade: Jera imajen husi deskrisaun textu
- Dokumentasaun: https://platform.openai.com/docs/guides/images

### 3.3 Codex
- Kapasidade: Tradús língua naturál ba kódigu
- Dokumentasaun: https://platform.openai.com/docs/guides/code

## 4. Hahu Uza OpenAI API

### 4.1 Autentikasaun
- Regista ba konta OpenAI
- Jera xave API
- Inklui xave API iha ita-nia pedidu

### 4.2 Halo Pedidu API
- Hili endpoint ne'ebé apropriadu (exemplu, completions, chat, images)
- Kria pedidu API ho parámetru sira-ne'ebé presiza
- Haruka pedidu no prosesa resposta

### 4.3 Ezemplu Báziku (Python)
```python
import openai

openai.api_key = 'your-api-key'

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Translate the following English text to French: 'Hello, how are you?'",
  max_tokens=60
)

print(response.choices[0].text.strip())
```

## 5. Konseitu Importante iha Dokumentasaun OpenAI nian

### 5.1 Tokens
- Komprende oinsá textu divide ba tokens
- Aprende kona-ba limites token ba model diferente sira

### 5.2 Engenharia Prompt
- Téknika ba kria prompt efetivu
- Ezemplu husi prompt di'ak ba tarefa oioin

### 5.3 Fine-tuning
- Prosesu husi personaliza model ba tarefa espesífiku
- Orientasaun ba prepara dadus treinamentu

## 6. Tutorial no Gía

### 6.1 Jerasaun Textu
- Gía: https://platform.openai.com/docs/guides/completion
- Aprende oinsá jera textu uza model GPT

### 6.2 Completions Chat
- Gía: https://platform.openai.com/docs/guides/chat
- Komprende oinsá kria aplicasaun AI konversasionál

### 6.3 Jerasaun Imajen
- Gía: https://platform.openai.com/docs/guides/images
- Aprende oinsá jera no edita imajen uza DALL-E

### 6.4 Embeddings
- Gía: https://platform.openai.com/docs/guides/embeddings
- Komprende oinsá uza embeddings textu ba tarefa NLP oioin

## 7. Prátika no Orientasaun Importante

### 7.1 Limites Taxa
- Komprende no tuir