'# Um Guia Abrangente para Expressões Regulares em Python

## Introdução

Expressões regulares, muitas vezes abreviadas como regex ou regexp, são ferramentas poderosas para correspondência de padrões e manipulação de texto. Elas fornecem uma maneira concisa e flexível de pesquisar, extrair e modificar texto com base em padrões específicos. Em Python, as expressões regulares são suportadas através do módulo integrado `re`, que oferece uma ampla gama de funções para trabalhar com padrões regex.

Este guia fornece uma visão abrangente das expressões regulares em Python, cobrindo conceitos básicos, sintaxe e técnicas avançadas. Se você é novo em expressões regulares ou tem alguma experiência, este guia o ajudará a compreender e aproveitar o poder do regex em seus projetos Python.

## 1. Introdução às Expressões Regulares

Em seu núcleo, uma expressão regular é uma sequência de caracteres que define um padrão de pesquisa. Ela permite especificar um padrão de caracteres que você deseja corresponder dentro de uma string. As expressões regulares são usadas para várias tarefas, tais como:

- Procurar padrões específicos dentro de um texto maior.
- Validar a entrada do usuário para garantir que atenda a certos critérios.
- Extrair informações relevantes de texto estruturado ou não estruturado.
- Substituir ou modificar texto com base em padrões.
- Dividir strings em substrings com base em delimitadores.

As expressões regulares são suportadas em muitas linguagens de programação e editores de texto, tornando-as uma ferramenta versátil para processamento de texto em diferentes plataformas.

### Vocabulário

- **Padrão**: A sequência de caracteres que define os critérios de pesquisa em uma expressão regular.
- **Correspondência**: A substring dentro de uma string que corresponde ao padrão especificado.
- **Metacaractere**: Caracteres especiais em uma expressão regular que têm um significado predefinido e são usados para definir o padrão de pesquisa.

## 2. Sintaxe Básica de Regex

### 2.1 Caracteres Literais

A forma mais simples de uma expressão regular é uma correspondência literal. Consiste em uma sequência de caracteres que correspondem exatamente à substring desejada. Por exemplo, o padrão `"olá"` corresponderá à string exata "olá" dentro de um texto maior.

```python
import re

texto = "Olá, mundo! Olá, universo!"
correspondências = re.findall(r"olá", texto, re.IGNORECASE)
print(correspondências)  # Saída: ['Olá', 'olá']
```

Neste exemplo, a função `re.findall()` é usada para encontrar todas as ocorrências do padrão literal "olá" dentro da string `texto`. A flag `re.IGNORECASE` é usada para realizar uma pesquisa insensível a maiúsculas e minúsculas.

### 2.2 Metacaracteres

Metacaracteres são caracteres especiais em expressões regulares que têm um significado predefinido. Eles permitem definir padrões mais complexos além das correspondências literais. Aqui estão alguns metacaracteres comumente usados:

- `.` (Ponto): Corresponde a qualquer caractere único, exceto uma nova linha.
- `*` (Asterisco): Corresponde a zero ou mais ocorrências do caractere ou grupo anterior.
- `+` (Mais): Corresponde a uma ou mais ocorrências do caractere ou grupo anterior.
- `?` (Interrogação): Corresponde a zero ou uma ocorrência do caractere ou grupo anterior.
- `^` (Circunflexo): Corresponde ao início de uma string ou linha.
- `$` (Cifrão): Corresponde ao final de uma string ou linha.
- `[]` (Colchetes): Define um conjunto ou intervalo de caracteres.
- `|` (Barra vertical): Especifica alternativas (condição OU).
- `()` (Parênteses): Agrupa caracteres juntos e cria um grupo de captura.

Por exemplo, o padrão `"a.b"` corresponderia a qualquer substring de três caracteres que começa com "a", segue com qualquer caractere único (exceto nova linha) e termina com "b". Ele corresponderia a strings como "

'Corresponde a qualquer dígito decimal. Equivalente a `[0-9]`.
- `\D`: Corresponde a qualquer carácter não-dígito. Equivalente a `[^0-9]`.
- `\w`: Corresponde a qualquer carácter alfanumérico ou sublinhado. Equivalente a `[a-zA-Z0-9_]`.
- `\W`: Corresponde a qualquer carácter não-alfanumérico. Equivalente a `[^a-zA-Z0-9_]`.
- `\s`: Corresponde a qualquer carácter de espaço em branco (espaço, tab, nova linha, etc.).
- `\S`: Corresponde a qualquer carácter não-espaço em branco.

```python
import re

text = "The quick brown fox jumps over the lazy dog"
matches = re.findall(r"[aeiou]", text)
print(matches)  # Output: ['u', 'i', 'o', 'o', 'u', 'o', 'e', 'e', 'a', 'o']

text = "The price is $10.50"
matches = re.findall(r"\d+\.\d+", text)
print(matches)  # Output: ['10.50']
```

No primeiro exemplo, a classe de caracteres `[aeiou]` corresponde a qualquer vogal na string `text`. No segundo exemplo, o padrão `\d+\.\d+` corresponde a um número decimal, onde `\d+` corresponde a um ou mais dígitos antes e depois do ponto decimal.

## 5. Quantificadores

Os quantificadores especificam o número de ocorrências de um carácter, grupo ou classe de carácteres num padrão. Eles permitem definir a repetição de um elemento particular numa expressão regular.

Os quantificadores mais usados são:

- `*`: Corresponde a zero ou mais ocorrências do carácter ou grupo anterior.
- `+`: Corresponde a uma ou mais ocorrências do carácter ou grupo anterior.
- `?`: Corresponde a zero ou uma ocorrência do carácter ou grupo anterior.
- `{n}`: Corresponde exatamente a n ocorrências do carácter ou grupo anterior.
- `{n,}`: Corresponde a n ou mais ocorrências do carácter ou grupo anterior.
- `{n,m}`: Corresponde entre n e m ocorrências (inclusive) do carácter ou grupo anterior.

Os quantificadores são colocados imediatamente após o carácter, grupo ou classe de carácteres que eles modificam.

```python
import re

text = "The number is 123456789"
matches = re.findall(r"\d{3}", text)
print(matches)  # Output: ['123', '456', '789']

text = "The codes are abc, abbc, abbbc, and abbbbc"
matches = re.findall(r"ab{2,4}c", text)
print(matches)  # Output: ['abbc', 'abbbc', 'abbbbc']
```

No primeiro exemplo, o padrão `\d{3}` corresponde exatamente a três dígitos consecutivos na string `text`. No segundo exemplo, o padrão `ab{2,4}c` corresponde a substrings que começam com "a", seguidas por duas a quatro ocorrências de "b", e terminam com "c".

## 6. Ancoras

As ancoras são caracteres especiais em expressões regulares que correspondem a uma posição específica dentro de uma string em vez de um carácter. Eles permitem especificar o início ou fim de uma string, ou limites de palavras.

As ancoras mais usadas são:

- `^`: Corresponde ao início de uma string ou linha.
- `$`: Corresponde ao fim de uma string ou linha.
- `\b`: Corresponde a um limite de palavra (a posição entre um carácter de palavra e um carácter não-palavra).
- `\B`: Corresponde a um não-limite de palavra.

As ancoras são frequentemente usadas em combinação com outros elementos regex para criar padrões mais precisos.

```python
import re

text = "The quick brown fox jumps over the lazy dog"
matches = re.findall(r"^The", text)
print(matches)  # Output: ['The']

text = "Hello, world!"
matches = re.findall(r"world!$", text)
print(matches)  # Output: ['world!']

text = "The fox is quick. The dog is lazy."
matches = re.findall(r"\bThe\b", text)

"ons são usados para procurar um padrão dentro de uma string. Eles retornam um objeto de correspondência se o padrão for encontrado, ou Nenhum se nenhuma correspondência for encontrada.

A função `re.search()` examina a string e retorna a primeira ocorrência do padrão, enquanto a função `re.match()` verifica se o padrão corresponde ao início da string.

```python
import re

texto = "A raposa marrom rápida pula sobre o cão preguiçoso"
resultado = re.search(r"raposa", texto)
if resultado:
    print("Encontrado:", resultado.group())
else:
    print("Não encontrado")
# Output: Encontrado: raposa

resultado = re.match(r"A", texto)
if resultado:
    print("Combinado:", resultado.group())
else:
    print("Não combinado")
# Output: Combinado: A
```

No primeiro exemplo, `re.search()` procura pelo padrão "raposa" em qualquer lugar dentro da string `texto` e retorna um objeto de correspondência, se encontrado. O método `group()` do objeto de correspondência recupera a substring correspondente.

No segundo exemplo, `re.match()` verifica se o padrão "A" corresponde ao início da string `texto` e retorna um objeto de correspondência, se combinado.

## 10. Usando as funções re.findall() e re.sub()

A função `re.findall()` encontra todas as ocorrências não sobrepostas de um padrão dentro de uma string e as retorna como uma lista de strings. É útil para extrair várias correspondências de uma string.

A função `re.sub()` substitui todas as ocorrências de um padrão dentro de uma string por uma string de substituição ou função especificada. É comumente usada para manipulação e substituição de texto.

```python
import re

texto = "A raposa marrom rápida pula sobre o cão preguiçoso"
correspondências = re.findall(r"\b\w{4}\b", texto)
print(correspondências)  # Output: ['rápida', 'pula', 'sobre', 'cão', 'preguiçoso']

texto = "O preço é $10.50, $20.00, e $30.00"
resultado = re.sub(r"\$(\d+\.\d+)", r"USD \1", texto)
print(resultado)  # Output: O preço é USD 10.50, USD 20.00, e USD 30.00
```

No primeiro exemplo, `re.findall()` encontra todas as palavras com exatamente quatro letras na string `texto` e as retorna como uma lista.
No segundo exemplo, re.sub() substitui todas as ocorrências de um sinal de dólar seguido por um número decimal pela string "USD" seguida pelo número decimal capturado. O \1 na string de substituição refere-se ao primeiro grupo de captura (\d+\.\d+).

## 11. Usando e Benefícios de re.compile()

A função re.compile() é usada para compilar um padrão de expressão regular em um objeto regex. O objeto regex resultante pode ser usado para operações de pesquisa, correspondência ou substituição subsequentes.

Compilar uma expressão regular com re.compile() é particularmente útil quando você precisa usar o mesmo padrão várias vezes em seu código. Ele oferece benefícios de desempenho ao evitar a necessidade de recompilar o padrão cada vez que é usado.

```python
import re

padrão = re.compile(r"\b\w{4}\b")

texto1 = "A raposa marrom rápida"
texto2 = "O cão preguiçoso"

correspondências1 = padrão.findall(texto1)
correspondências2 = padrão.findall(texto2)

print(correspondências1)  # Output: ['rápida']
print(correspondências2)  # Output: ['preguiçoso']
```

Neste exemplo, o padrão \b\w{4}\b é compilado em um objeto regex usando re.compile(). O objeto de padrão resultante é então usado para encontrar correspondências em texto1 e texto2 usando o método findall() do objeto regex.

Usar re.compile() oferece vários benefícios:

Melhoria de desempenho: Compilar uma expressão regular uma vez e reutilizar o objeto compilado várias vezes é mais eficiente do que recompilar o padrão cada vez que é usado.
Legibilidade do código: Armazenar o objeto regex compilado em uma variável com um nome descritivo pode tornar o código mais legível e fácil de entender.
Reutil