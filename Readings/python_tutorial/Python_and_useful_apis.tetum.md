'# Guia Kompletu ba Uza API Gratuitu ho Python

Guia ne'e fornese ezemplu konaba oinsá uza API gratuitu sira ho Python. Seksaun ida-idak inklui deskrisaun badak konaba API no esemplu kódigu nian ne'ebé demonstra nia uzu.

## Tabela Husi Konteúdu
1. Google Search API
2. Telize API
3. IP Geolocation API
4. Free Geo IP API
5. COVID-19 API
6. Translo API
7. NLP Translation API
8. Shazam Core API
9. Article Data Extraction no Text Mining API
10. ReCaptcha Solver API

## 1. Google Search API

Google Search API fornese rezultadu buka ne'ebé efikaz iha tempu real, rekupera dadus husi Google web no image search.

```python
import requests

def google_search(query, api_key, cx):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'key': api_key,
        'cx': cx
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Uzu
api_key = "YOUR_API_KEY"
cx = "YOUR_CUSTOM_SEARCH_ENGINE_ID"
query = "Python programming"

results = google_search(query, api_key, cx)

if results:
    for item in results.get('items', []):
        print(f"Títulu: {item['title']}")
        print(f"Ligasaun: {item['link']}")
        print(f"Fragmentu: {item['snippet']}")
        print("---")
else:
    print("La hetan rezultadu ka akontese erru.")
```

## 2. Telize API

Telize mak API REST nian ne'ebé permite programador sira buka informasaun lokal husi IP moris ida no rekupera IP husi vizitante.

```python
import requests

def get_ip_info(ip_address=None):
    if ip_address:
        url = f"https://api.telize.com/geoip/{ip_address}"
    else:
        url = "https://api.telize.com/ip"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Uzu
# Hetan informasaun kona-ba IP ida espesifiku
ip_info = get_ip_info("8.8.8.8")
if ip_info:
    print(f"IP: {ip_info['ip']}")
    print(f"Nasaun: {ip_info['country']}")
    print(f"Rejiaun: {ip_info['region']}")
    print(f"Sidade: {ip_info['city']}")
    print(f"Latitude: {ip_info['latitude']}")
    print(f"Longitude: {ip_info['longitude']}")
else:
    print("Lae hetan informasaun IP.")

# Hetan ita nia IP rasik
my_ip = get_ip_info()
if my_ip:
    print(f"Ha'u nia IP: {my_ip['ip']}")
else:
    print("Lae hetan ita nia IP.")
```

## 3. IP Geolocation API

IP Geolocation API fornese informasaun detallu konaba lokal IP husi vizitante sira, inklui nasaun, sidade, latitude, longitude, timezone, no tan.

```python
import requests

def get_ip_geolocation(ip_address=None):
    url = "https://api.ipgeolocation.io/ipgeo"
    params = {
        'apiKey': 'YOUR_API_KEY',
        'ip': ip_address
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Uzu
# Hetan informasaun kona-ba IP ida espesifiku
ip_info = get_ip_geolocation("8.8.8.8")
if ip_info:
    print(f"IP: {ip_info['ip']}")
    print(f"Nasaun: {ip_info['country_name']}")
    print(f"Sidade: {ip_info['city']}")
    print(f"Latitude: {ip_info['latitude']}")
    print(f"Longitude: {ip_info['longitude']}")
    print(f"Zona Tempu: {ip_info['time_zone']['name']}")
    print(f"ISP: {ip_info['isp']}")
else:
    print("Lae hetan informasaun IP.")

# Hetan

```python
import requests

def translate_content(konteudu, target_lang, source_lang=None, is_html=False):
    url = "https://nlp-translation.p.rapidapi.com/v1/translate"
    headers = {
        "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",
        "X-RapidAPI-Host": "nlp-translation.p.rapidapi.com"
    }
    payload = {
        "text": konteudu,
        "to": target_lang,
        "from": source_lang,
        "html": is_html
    }

    resposta = requests.post(url, json=payload, headers=headers)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

# Modu atu uza ba tradusaun testu
text_to_translate = "Hello, how are you?"
target_language = "fr"  # Frances

resultadu = translate_content(text_to_translate, target_language)

if resultadu:
    print(f"Testu orijinal: {text_to_translate}")
    print(f"Testu nebe'e tradus: {resultadu['translated_text']}")
    print(f"Lian kona ba fonte nebe'e deteta: {resultadu['from']}")
else:
    print("Tradusaun la konsege.")

# Modu atu uza ba tradusaun HTML
html_to_translate = "<p>Bemvindo ba ita nia <strong>website</strong>!</p>"
target_language = "de"  # Alemaun

html_resultadu = translate_content(html_to_translate, target_language, is_html=True)

if html_resultadu:
    print(f"\nHTML orijinal: {html_to_translate}")
    print(f"HTML nebe'e tradus: {html_resultadu['translated_text']}")
else:
    print("Tradusaun HTML la konsege.")
```

## 8. Shazam Core API

API Shazam Core oferese ba dezenvolvedores atu asesu ba kapasidade rekonhesimentu musika Shazam nian. Nia bele uza atu identifika hanesan musica, hetan detallu kona ba musica no hetan informasaun relevante.

```python
import requests

def recognize_song(api_key, audio_url):
    url = "https://shazam-core.p.rapidapi.com/v1/tracks/recognize"
    
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "shazam-core.p.rapidapi.com"
    }
    
    params = {
        "url": audio_url
    }
    
    resposta = requests.get(url, headers=headers, params=params)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

# Modu atu uza
api_key = "YOUR_RAPIDAPI_KEY"
audio_url = "https://example.com/path/to/audio/file.mp3"

resultadu = recognize_song(api_key, audio_url)

if resultadu:
    print(f"Titulu Musika: {resultadu['track']['title']}")
    print(f"Artista: {resultadu['track']['subtitle']}")
    print(f"Jeneru: {resultadu['track']['genres']['primary']}")
else:
    print("La konsege atu rekonese musika.")
```

## 9. Extrasaun Dadus Artigu no API Text Mining

API extrasaun dadus artigu no Text Mining husi Ujeebu oferese ba dezenvolvedores atu estrai dadus nebe'e signifikante hanesan testu klaru husi HTML maske lian nebe'e mak uza.

```python
import requests

def extract_article_data(api_key, url):
    api_url = "https://api.ujeebu.com/article-extractor/v1/extract"
    
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "article-extractor2.p.rapidapi.com"
    }
    
    params = {
        "url": url
    }
    
    resposta = requests.get(api_url, headers=headers, params=params)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

# Modu atu uza
api_key = "YOUR_RAPIDAPI_KEY"
article_url = "https://example.com/path/to/article"

resultadu = extract_article_data(api_key, article_url)

if resultadu:
    print(f"Titulu: {resultadu['title']}")
    print(f"Autor: {resultadu['author']}")
    print(f"Data Publica: {result

'def get_trending_videos(api_key):
    url = "https://scraptik.p.rapidapi.com/trending-feed"
    
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "scraptik.p.rapidapi.com"
    }
    
    resposta = requests.get(url, headers=headers)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

# Uza
api_key = "YOUR_RAPIDAPI_KEY"

rezultadu = get_trending_videos(api_key)

if rezultadu and 'dados' in rezultadu:
    for video in rezultadu['dados'][:5]:  
        print(f"Author: {video['author']['nickname']}")
        print(f"Descrição do vídeo: {video['description']}")
        print(f"Gostos: {video['stats']['diggCount']}")
        print(f"Comentários: {video['stats']['commentCount']}")
        print(f"Shares: {video['stats']['shareCount']}")
        print(f"URL do vídeo: https://www.tiktok.com/@{video['author']['uniqueId']}/video/{video['id']}")
        print("---")
else:
    print("Falhou a recolha dos vídeos em tendência ou ocorreu um erro.")

# 14. API Tiktok video sem marca d'água

A API Tiktok video sem marca d'água permite aos desenvolvedores baixar vídeos Tiktok sem marcas d'água, para que possam ser postados noutras plataformas sociais.

import requests

def download_tiktok_video(api_key, video_url):
    url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"
    
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
    }
    
    params = {
        "url": video_url
    }
    
    resposta = requests.get(url, headers=headers, params=params)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

# Uza
api_key = "YOUR_RAPIDAPI_KEY"
video_url = "https://www.tiktok.com/@username/video/1234567890123456789"

resultado = download_tiktok_video(api_key, video_url)

if resultado and 'dados' in resultado:
    print(f"Autor: {resultado['dados']['author']['nickname']}")
    print(f"Título do vídeo: {resultado['dados']['title']}")
    print(f"URL do vídeo sem marca d'água: {resultado['dados']['play']}")
    print(f"URL do vídeo com marca d'água: {resultado['dados']['wmplay']}")
    print(f"Música: {resultado['dados']['music']}")
else:
    print("Falhou a recolha de informações do vídeo ou ocorreu um erro.")

# 15. API Rapid Translate Multi Tradução

A API Rapid Translate Multi Tradução traduz HTML, texto, palavras, frases e parágrafos em tempo real em mais de 100 idiomas.

import requests

def traduz_multi(api_key, texto, idioma_destino, idioma_origem=None):
    url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"
    
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "rapid-translate-multi-traduction.p.rapidapi.com"
    }
    
    payload = {
        "de": idioma_origem or "auto",
        "para": idioma_destino,
        "q": texto
    }
    
    resposta = requests.post(url, json=payload, headers=headers)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

# Uza
api_key = "YOUR_RAPIDAPI_KEY"
texto_para_traduzir = "Olá, como estás? Este é um teste da API de tradução."
idioma_destino = "fr"  # Francês

resultado = traduz_multi(api_key, texto_para_traduzir, idioma_destino)

if resultado:
    print(f"Texto original: {texto_para_traduzir}")
    print(f"Texto traduzido: {resultado}")
else:
    print("Falhou a tradução ou ocorreu um erro.")

# 16. API Youtube v3

A API Youtube v3 fornece dados do Youtube sem necessidade de uma chave de dados da API do Youtube.

import requests

def pesquisa_youtube(api_key, query, max_results=