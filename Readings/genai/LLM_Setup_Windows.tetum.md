'# Konfigurasaun Modelu Lian Open-Source iha Ita-nia Laptop Windows

## Introdusaun

Hospeda modelu lian open-source iha ita-nia komputador lokál bele sai projetu intersante ba entusiasta teknolojia no solusaun prátiku ba sira-ne'ebé preokupa kona-ba privasidade dadus ka hakarak experimenta ho AI la depende ba servisu cloud. Gía ida ne'e sei orienta ita liuhusi prosesu konfigurasaun no operasaun modelu lian open-source iha ita-nia laptop Windows, sem uza Conda.

## Benefísiu Husi Hospedajen LLM Lokál

1. Esperiénsia aprendizajen prátika ho teknolojia AI
2. Opção atu afinar modelu sira bazeia ba dadus ita-nia rasik
3. Privasidade no kontrolu dadus ne'ebé aas
4. La iha custu rekurrente husi servisu cloud
5. Aksesibilidade offline
6. Flexibilidade atu experimenta ho modelu sira-ne'ebé diferente

## Pré-rekizitu

- Windows 10 ka 11
- Python 3.10 ka foun liu instaladu ona
- Git instaladu ona
- Espasu disk sufisiente (pelo menus 20GB livre)
- CPU modernu (no GPU ba desempeñu di'ak liu, maski la presiza)

## Gía Konfigurasaun Pasu Husi Pasu

### 1. Kria Ambiente Virtuál

Loke komandu prompt no navega ba diretóriu projetu ne'ebé ita hakarak. Depois kria no ativa ambiente virtuál:

```
python -m venv llm_env
llm_env\Scripts\activate
```

### 2. Klon Repositóriu WebUI

Ho ita-nia ambiente virtuál ne'ebé ativadu ona, klon repositóriu text-generation-webui:

```
git clone https://github.com/oobabooga/text-generation-webui.git
cd text-generation-webui
```

### 3. Instala Dependénsia

Instala pakote Python sira ne'ebé presiza:

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
pip install -r requirements.txt
```

Nota: Se ita la uza GPU, bele ignora pasu instalasaun torch no corre `pip install -r requirements.txt` de'it.

### 4. Download Modelu Lian

Ita iha opção balu atu download modelu:

a. Uza interface WebUI (ita sei kobre iha pasu tuir mai)
b. Uza linha komandu:
   ```
   python download-model.py pankajmathur/orca_mini_13b
   ```
c. Download manualmente ficheiru sira husi Hugging Face no coloka iha pasta `models`

Ba gía ida ne'e, ita sei uza interface WebUI atu download modelu.

### 5. Hahú Server WebUI

Corre komandu tuir mai atu hahú server:

```
python server.py
```

Terminal sei hatudu URL lokál (jeralmente `http://localhost:7860`). Abre URL ne'e iha ita-nia web browser.

### 6. Download no Karga Modelu

Iha interface WebUI :

1. Bá ba aba "Models"
2. Iha sesaun "Download custom model or LoRA", koloka ligasaun modelu Hugging Face tuir mai:
   ```
   pankajmathur/orca_mini_13b
   ```
3. Klik "Download"
4. Hafoin download, hili modelu husi menu dropdown iha sesaun "Model"
5. Klik "Load" atu ativa modelu

### 7. Konfigura Definisaun

Iha aba "Parameters", ajusta definisaun bazeia ba ita-nia hardware:

- Se uza CPU, ativa opção "cpu"
- Ajusta parámetru sira seluk hanesan presiza ba desempeñu

### 8. Hahú Konversa!

Navega ba aba "Chat" no hahú interasaun ho ita-nia modelu lian ne'ebé ita hospeda lokálmente.

## Tips