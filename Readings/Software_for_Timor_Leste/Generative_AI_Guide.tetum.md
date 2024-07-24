'# Guia Komprehensivu ba Uza AI Jerativa: Esplikasaun Detalladu no Ezemplu

## Tabela Husi Konteudu
1. [Konfigura Ambiente](#konfigura-ambiente)
2. [Obten API Keys](#obten-api-keys)
3. [Uza LLM lokal](#uza-llm-lokal)
4. [Uza LLM bazeia API](#uza-llm-bazeia-api)
5. [Aplikasaun no Kazu Uza](#aplikasaun-no-kazu-uza)
   - [Jerasaun Textu no Modelu Lingua](#jerasaun-textu-no-modelu-lingua)
   - [Sintese Imajen no Video](#sintese-imajen-no-video)
   - [Jerasaun Musika no Audio](#jerasaun-musika-no-audio)
   - [Jerasaun Kodigo no Kompletamentu](#jerasaun-kodigo-no-kompletamentu)
   - [Deskobrezaun Medikamentu no Dezain Molekular](#deskobrezaun-medikamentu-no-dezain-molekular)

## Konfigura Ambiente

Konfigura ambiente ne'ebé loos importante tebes atu servisu ho modelu AI jerativa. Prosesu ne'e involve kria ambiente Python ida ne'ebé dedika no instala biblioteka sira ne'ebé nesesariu. Liu husi isola ita nia ambiente projetu, ita bele evita konflitu entre projetu sira ne'ebé diferente no asegura reprosidade.

1. Kria ambiente virtual foun ida:
   ```bash
   python -m venv genai_env
   source genai_env/bin/activate  # Iha Windows, uza: genai_env\Scripts\activate
   ```

2. Instala pakote sira ne'ebé nesesariu:
   ```bash
   pip install transformers torch numpy Pillow librosa scikit-learn rdkit openai requests tensorflow tensorflow-hub magenta music21
   ```

Pakote sira ne'e fornese besik gama husi ferramenta sira ba tarefa AI jerativa sira ne'ebé variadu, husi prosesamentu lingua natural ba jerasaun imajen no kriasaun musika.

## Obten API Keys

Servisu AI jerativa barak presiza API keys atu asesu. Key sira ne'e importante tebes atu otentika ita nia pedidu sira no iha tempu balun atu jere uzu no faturamentu. Iha ne'e mak oinsa atu hetan keys ba servisu sira ne'ebé popular:

### OpenAI API Key
1. Bá ba https://openai.com/api/ no rejista hodi hetan konta ida.
2. Ha'u bainhira loga on, bá ba seksaun API Keys iha ita nia painel konta.
3. Klik iha "Kria segredu foun" atu jera API key foun ida.
4. Kopia key no rai nia ho seguransa. Ita la bele haree fila fali.

### Hugging Face API Key
1. Bá ba https://huggingface.co/ no rejista hodi hetan konta ida.
2. Ha'u bainhira loga on, bá ba ita nia konfigurasaun perfil.
3. Iha seksaun "Tokens Aksesu", klik iha "Token foun" atu kria API key ida foun.
4. Fó naran ba ita nia token no hili permissaun sira ne'ebé nesesariu.
5. Kopia token no rai nia ho seguransa.

### Replicate API Key (ba Diffusion Estavel)
1. Bá ba https://replicate.com/ no rejista hodi hetan konta ida.
2. Ha'u bainhira loga on, bá ba ita nia konfigurasaun konta.
3. Iha seksaun "API tokens", ita sei hetan ita nia API key.
4. Kopia key no rai nia ho seguransa.

Lembra atu rai ita nia API keys ho sigilu no la fahe sira publikamente. Servisu barak oferese dalan atu jere no troka key sira ba seguransa ne'eb

Uza Hugging Face Transformers biblioteka:

```python
husi transformers import pipeline

# Inisia pipeline jerasaun textu
generator = pipeline('text-generation', model='gpt2')

# Jera textu
prompt = "Artificial Intelligence is"
output = generator(prompt, max_length=50, num_return_sequences=1)

print(output[0]['generated_text'])
```

Ezemplu output:
```
Artificial Intelligence is becoming increasingly important in our daily lives. From self-driving cars to virtual assistants, AI is transforming the way we interact with technology and each other.
```

Kódigu ida ne'e uza modelu GPT-2 hodi jera textu bazeia ba prompt ne'ebé fó. Parameter `max_length` kontrola númeru máximu token sira iha output, no `num_return_sequences` hatudu hira mak kumpletu diferente hodi jera. LLM lokál oferese laténsia ki'ik liu no privasidade liu, maibé bele iha kapasidade limitadu kompara ho modelu sira baseia iha cloud.

## Uza LLM bazeia API

Modelu Língua bazeia API, hanesan OpenAI's GPT-3, oferese kapasidade boot sira la presiza rekursu komputasionál lokál. Modelu sira ne'e normalmente avansadu liu no regularmente atualiza. Iha ne'e mak ezemplu ida uza OpenAI API:

```python
import openai
import os

# Hafó ita-nia API key
openai.api_key = 'your-openai-api-key-here'

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Translate the following English text to French: 'Hello, how are you?'",
  max_tokens=60
)

print(response.choices[0].text.strip())
```

Ezemplu output:
```
Bonjour, comment allez-vous?
```

Kódigu ida ne'e uza OpenAI API hodi asesu modelu GPT-3 hodi jera textu. Parameter `engine` hatudu modelu ne'ebé uza, `prompt` mak textu input, no `max_tokens` limita kompridu output nian. Modelu sira bazeia API oferese desempeñu estadu-da-arte no kapasidade boot sira, maibé presiza ligasaun internet no bele hetan kustu uzu.

## Aplikasaun no Kazu Uzu

### Jerasaun Textu no Modelu Língua

Jerasaun textu no modelu língua iha linha frente husi AI jerativu. Modelu sira ne'e, treinadu ho dadus textu boot, bele komprende no jera textu hanesan umanu. Sira kapás hodi halo servisu husi kumpletu textu simples to komprensaun no jerasaun língua kompleksu. Modelu língua hanesan GPT-3 hatudu kapasidade espesial iha aplikasaun sira oioin, inklui asisténsia hakerek, chatbots, no hakerek kriativu.

Ezemplu ida uza modelu pre-treinadu ba análize sentimentu:

```python
husi transformers import pipeline

classifier = pipeline("sentiment-analysis")

textu = "Hau gosta uza modelu AI jerativu. Sira versátil tebes no poderozu!"
rezultadu = classifier(textu)

print(f"Textu: {textu}")
print(f"Sentimentu: {rezultadu[0]['label']}")
print(f"Konfiansa: {rezultadu[0]['score']:.4f}")
```

Ezemplu output:
```
Textu: Hau gosta uza modelu AI jerativu. Sira versátil tebes no poderozu!
Sentimentu: POSITIVE
Konfiansa: 0.9998
```

Ezemplu ida ne'e demonstra oinsa modelu pre-treinadu bele análiza sentimentu textu nian. Kapasidade ida ne'e importante tebes iha aplikasaun sira hanesan monitorizasaun média sosial, análize feedback kliente, no peskiza merkadu.

### Síntese Imajen no Vídeu

Síntese imajen no vídeo mak área ida interensante husi AI

'1024 , nn . LeakyReLU(0.2) , nn . Linear(1024, 3 * 64 * 64) , nn . Tanh() 
def forward(self, z):
    img = self.model(z)
    img = img.view(img.size(0), 3, 64, 64)
    return img

# Karga ida generator ne'ebé treina ona (ita presiza treina primeiru)
generator = Generator(latent_dim=100)
generator.load_state_dict(torch.load('path_to_pretrained_generator.pth'))
generator.eval()

# Jera rosto
latent_vector = torch.randn(1, 100)
with torch.no_grad():
    generated_image = generator(latent_vector)

save_image(generated_image, "generated_face.png", normalize=True)
print("Rosto ne'ebé jera ona salva ona hanesan generated_face.png")

Kódigu snippet ne'e hatudu oinsá atu uza GAN ne'ebé treina ona hodi jera imajen rosto ne'ebé realista. Generator simu input hosi random noise vector no prodús imajen hanesan output.

### Jerasaun Musika no Audio

Jerasaun musika no audio mak aplikasaun interesante hosi AI generativa, kombina elementus hosi prosesamentu sinal, teoria musika, no aprendizajen mákina. Modelu sira ne'e bele kria kompozisaun original, transforma musika ezistente, ka até konverte audio ba partitura.

1. Toca partitura ho Music21:

Music21 mak kit ferramenta ba musicologia ho suporta komputadór. Nia bele uza hodi analiza, kria, no manipula musika iha forma simbólika (hanesan partitura).

```python
from music21 import converter, instrument, note, chord, stream

def play_sheet_music(file_path):
    # Karga partitura
    score = converter.parse(file_path)
    
    # Hasai parte piano (se iha)
    piano_part = None
    for part in score.parts:
        if 'Piano' in part.partName:
            piano_part = part
            break
    
    if piano_part is None:
        print("La iha parte piano iha partitura.")
        return
    
    # Kria stream foun ba playback
    playback_stream = stream.Stream()
    
    # Hatama nota no akorde ba playback stream
    for element in piano_part.recurse():
        if isinstance(element, note.Note):
            playback_stream.append(note.Note(element.pitch, quarterLength=element.duration.quarterLength))
        elif isinstance(element, chord.Chord):
            playback_stream.append(chord.Chord(element.pitches, quarterLength=element.duration.quarterLength))
    
    # Toca musika
    sp = midi.realtime.StreamPlayer(playback_stream)
    sp.play()

# Uza
play_sheet_music('path_to_sheet_music.xml')
```

Kódigu ne'e karga partitura, hasai piano parte, no toka. Hatudu oinsá partitura dijitál bele manipula no toka ho programa.

```python
from music21 import converter, instrument, note, chord, stream
import os

def play_sheet_music(file_path):
    # Determina estensaun file
    _, file_extension = os.path.splitext(file_path)
    
    # Karga partitura
    if file_extension.lower() == '.pdf':
        score = converter.parse(file_path, format='musicxml', forceSource=True)
    else:
        score = converter.parse(file_path)
    
    # Hasai parte piano (se iha)
    piano_part = None
    for part in score.parts:
        if 'Piano' in part.partName:
            piano_part = part
            break
    
    if piano_part is None:
        print("La iha parte piano iha partitura.")
        return
    
    # Kria stream foun ba playback
    playback_stream = stream.Stream()
    
    # Hatama nota no akorde ba playback stream
    for element in piano_part.recurse():
        if isinstance(element, note.Note):
            playback_stream.append(note.Note(element.pitch, quarterLength=element.duration.quarterLength))
        elif isinstance(element, chord.Chord):
            playback_stream.append(chord.Chord(element.pitches, quarterLength=element.duration.quarterLength))
    
    # Toca musika
    sp = midi.realtime.StreamPlayer(playback_stream)
    sp.play()

# Uza
play_sheet_music('path_to_sheet_music.pdf')  # ou .xml, .mxl, etc.
```
Kódigu ne'e konverte musika husi formato pdf.

"""
Websites atu hetan partitura:

1. IMSLP (

'Ne'e ba melodias ne'ebé naruk/liu ki'ik
    temperatura = 1.0  # Ajusta ne'e atu kontrola randomidade

    generator_options = generator_pb2.GeneratorOptions()
    generator_options.args['temperature'].float_value = temperatura
    generate_section = generator_options.generate_sections.add(start_time=0, end_time=num_steps)

    sekuensia = melody_rnn.generate(music_pb2.NoteSequence(), generator_options)

    # Konverte ba MIDI
    magenta.music.sequence_proto_to_midi_file(sekuensia, 'generated_melody.mid')
    print("Melodia jera no salva ona iha 'generated_melody.mid'")

# Uzu
generate_melody()
```

Kódigu ne'e uza modelu pre-treinadu husi Attention RNN husi Magenta atu jera melodia foun. Melodia ne'ebé jera depois salva ona iha arkivu MIDI. Parametru 'temperatura' kontrola randomidade husi jerasaun - valor boot liu produs rezultadu ne'ebé la espera, enkuantu valor ki'ik liu halo output ne'ebé previsivel liu.

4. Jerasaun Progressaun Akoorden ho Markov Chains:

Maski la direitamente abordajen ne'ebé uza rede neural, Markov Chains bele efetivu atu jera sekvensia hanesan musika, hanesan progressaun akoorden. Iha ne'e ezemplu ida:

```python
import random

klase MarkovChain:
    def __init__(self):
        self.chain = {}

    def add_sequence(self, sekvensia):
        ba i iha range(len(sekvensia) - 1):
            atual = sekvensia[i]
            next_chord = sekvensia[i + 1]
            if atual la iha self.chain:
                self.chain[atual] = {}
            if next_chord la iha self.chain[atual]:
                self.chain[atual][next_chord] = 0
            self.chain[atual][next_chord] += 1

    def jera(self, hahu, naruk):
        atual = hahu
        rezultadu = [atual]
        ba _ iha range(naruk - 1):
            if atual la iha self.chain:
                break
            opsaun = list(self.chain[atual].keys())
            pesos = list(self.chain[atual].values())
            atual = random.choices(opsaun, weights=pesos)[0]
            rezultadu.append(atual)
        return rezultadu

# Dadus treinamentu (progressaun akoorden)
dadus_treinamentu = [
    ['C', 'Am', 'F', 'G'],
    ['C', 'F', 'G', 'C'],
    ['Am', 'F', 'C', 'G'],
    ['C', 'G', 'Am', 'F']
]

# Kria no treina Markov chain
markov = MarkovChain()
ba progressaun iha dadus_treinamentu:
    markov.add_sequence(progressaun)

# Jera progressaun akoorden foun
progressaun_foun = markov.jera('C', 8)
print("Progressaun Akoorden Jera:", ' - '.join(progressaun_foun))
```

Kódigu ne'e demonstra oinsá uza Markov Chain simples atu jera progressaun akoorden. Nia aprende husi ezemplu progressaun no bele jera foun ne'ebé tuir padraun hanesan. Metodu ne'e bele uza atu kria trilhas atras ou inspira kompositores ho sekvensia akoorden foun.

### Jerasaun no Kompletamentu Kódigu

Jerasaun no kompletamentu kódigu sai aplikasaun importante liu husi AI jenerativu iha dezenvolvimentu software. Modelu sira bele ajuda programador sira liu husi sugestaun ba kompletamentu kódigu, jera funsaun tomak bazeia ba deskrisaun, ou mós tradus entre lingua programasaun.

Ba jerasaun kódigu, ami sei uza modelu Codex liu husi OpenAI API:

```python
import openai

openai.api_key = 'sira-nia-openai-api-key-iha-ne’e'

prompt = """
# Funsaun Python atu kalkula faktorial husi numeru
def faktorial(n):
"""