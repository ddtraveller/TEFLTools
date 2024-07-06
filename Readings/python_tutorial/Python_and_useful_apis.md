# Comprehensive Guide to Using Free APIs with Python

This guide provides examples of how to use various free APIs with Python. Each section includes a brief description of the API and a code sample demonstrating its usage.

## Table of Contents
1. Google Search API
2. Telize API
3. IP Geolocation API
4. Free Geo IP API
5. COVID-19 API
6. Translo API
7. NLP Translation API
8. Shazam Core API
9. Article Data Extraction and Text Mining API
10. ReCaptcha Solver API

## 1. Google Search API

The Google Search API provides powerful search results in real-time, retrieving data from both Google web and image search.

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

# Usage
api_key = "YOUR_API_KEY"
cx = "YOUR_CUSTOM_SEARCH_ENGINE_ID"
query = "Python programming"

results = google_search(query, api_key, cx)

if results:
    for item in results.get('items', []):
        print(f"Title: {item['title']}")
        print(f"Link: {item['link']}")
        print(f"Snippet: {item['snippet']}")
        print("---")
else:
    print("No results found or an error occurred.")
```

## 2. Telize API

Telize is a REST API that allows developers to query location information from any IP address and retrieve visitor's IP addresses.

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

# Usage
# Get information about a specific IP
ip_info = get_ip_info("8.8.8.8")
if ip_info:
    print(f"IP: {ip_info['ip']}")
    print(f"Country: {ip_info['country']}")
    print(f"Region: {ip_info['region']}")
    print(f"City: {ip_info['city']}")
    print(f"Latitude: {ip_info['latitude']}")
    print(f"Longitude: {ip_info['longitude']}")
else:
    print("Failed to retrieve IP information.")

# Get your own IP address
my_ip = get_ip_info()
if my_ip:
    print(f"My IP: {my_ip['ip']}")
else:
    print("Failed to retrieve your IP address.")
```

## 3. IP Geolocation API

The IP Geolocation API provides detailed information about the IP location of visitors, including country, city, latitude, longitude, timezone, and more.

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

# Usage
# Get information about a specific IP
ip_info = get_ip_geolocation("8.8.8.8")
if ip_info:
    print(f"IP: {ip_info['ip']}")
    print(f"Country: {ip_info['country_name']}")
    print(f"City: {ip_info['city']}")
    print(f"Latitude: {ip_info['latitude']}")
    print(f"Longitude: {ip_info['longitude']}")
    print(f"Timezone: {ip_info['time_zone']['name']}")
    print(f"ISP: {ip_info['isp']}")
else:
    print("Failed to retrieve IP information.")

# Get information about the visitor's IP
visitor_info = get_ip_geolocation()
if visitor_info:
    print(f"Your IP: {visitor_info['ip']}")
    print(f"Your Country: {visitor_info['country_name']}")
else:
    print("Failed to retrieve visitor information.")
```

## 4. Free Geo IP API

The FreeGeoIP.app provides a reliable and scalable IP geolocation API for developers. It uses a database of IP addresses associated with cities and other relevant information like time zone, latitude, and longitude.

```python
import requests

def get_geo_ip(ip_address=None):
    if ip_address:
        url = f"https://freegeoip.app/json/{ip_address}"
    else:
        url = "https://freegeoip.app/json/"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Usage
# Get information about a specific IP
ip_info = get_geo_ip("8.8.8.8")
if ip_info:
    print(f"IP: {ip_info['ip']}")
    print(f"Country: {ip_info['country_name']}")
    print(f"Region: {ip_info['region_name']}")
    print(f"City: {ip_info['city']}")
    print(f"Latitude: {ip_info['latitude']}")
    print(f"Longitude: {ip_info['longitude']}")
    print(f"Time Zone: {ip_info['time_zone']}")
else:
    print("Failed to retrieve IP information.")

# Get information about the visitor's IP
visitor_info = get_geo_ip()
if visitor_info:
    print(f"Your IP: {visitor_info['ip']}")
    print(f"Your Country: {visitor_info['country_name']}")
    print(f"Your City: {visitor_info['city']}")
else:
    print("Failed to retrieve visitor information.")
```

## 5. COVID-19 API

The COVID-19 API allows developers to follow the progress of the coronavirus around the world. This free API gives statistics for all countries on COVID-19.

```python
import requests

def get_covid_stats(country=None):
    if country:
        url = f"https://corona.lmao.ninja/v2/countries/{country}"
    else:
        url = "https://corona.lmao.ninja/v2/all"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Usage
# Get global COVID-19 statistics
global_stats = get_covid_stats()
if global_stats:
    print("Global COVID-19 Statistics:")
    print(f"Total Cases: {global_stats['cases']:,}")
    print(f"Total Deaths: {global_stats['deaths']:,}")
    print(f"Total Recovered: {global_stats['recovered']:,}")
    print(f"Active Cases: {global_stats['active']:,}")
else:
    print("Failed to retrieve global COVID-19 statistics.")

# Get COVID-19 statistics for a specific country
country_stats = get_covid_stats("USA")
if country_stats:
    print("\nCOVID-19 Statistics for USA:")
    print(f"Total Cases: {country_stats['cases']:,}")
    print(f"Total Deaths: {country_stats['deaths']:,}")
    print(f"Total Recovered: {country_stats['recovered']:,}")
    print(f"Active Cases: {country_stats['active']:,}")
    print(f"Cases per Million: {country_stats['casesPerOneMillion']:,}")
else:
    print("Failed to retrieve COVID-19 statistics for USA.")
```

## 6. Translo API

The Translo API is a translation service that claims to be 3 times more accurate than Google Translate. It supports over 110 languages and can translate both text and HTML content.

```python
import requests

def translate_text(text, target_lang, source_lang=None):
    url = "https://translate.netcore.in/api/v1/translate"
    headers = {
        "Authorization": "YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "to": target_lang
    }
    if source_lang:
        payload["from"] = source_lang

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Usage
text_to_translate = "Hello, how are you?"
target_language = "es"  # Spanish

result = translate_text(text_to_translate, target_language)

if result:
    print(f"Original text: {text_to_translate}")
    print(f"Translated text: {result['translated_text']}")
    print(f"Detected source language: {result['source_language']}")
else:
    print("Translation failed.")

# Translate with specified source language
source_language = "en"
result_with_source = translate_text(text_to_translate, target_language, source_language)

if result_with_source:
    print(f"\nTranslation with specified source language:")
    print(f"Translated text: {result_with_source['translated_text']}")
else:
    print("Translation with specified source language failed.")
```

## 7. NLP Translation API

The NLP Translation API is another high-quality neural machine translation service that supports over 110 languages. It can translate both text and HTML content.

```python
import requests

def translate_content(content, target_lang, source_lang=None, is_html=False):
    url = "https://nlp-translation.p.rapidapi.com/v1/translate"
    headers = {
        "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",
        "X-RapidAPI-Host": "nlp-translation.p.rapidapi.com"
    }
    payload = {
        "text": content,
        "to": target_lang,
        "from": source_lang,
        "html": is_html
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Usage for text translation
text_to_translate = "Hello, how are you?"
target_language = "fr"  # French

result = translate_content(text_to_translate, target_language)

if result:
    print(f"Original text: {text_to_translate}")
    print(f"Translated text: {result['translated_text']}")
    print(f"Detected source language: {result['from']}")
else:
    print("Translation failed.")

# Usage for HTML translation
html_to_translate = "<p>Welcome to our <strong>website</strong>!</p>"
target_language = "de"  # German

html_result = translate_content(html_to_translate, target_language, is_html=True)

if html_result:
    print(f"\nOriginal HTML: {html_to_translate}")
    print(f"Translated HTML: {html_result['translated_text']}")
else:
    print("HTML translation failed.")
```

## 8. Shazam Core API

The Shazam Core API allows developers to access Shazam's music recognition capabilities. It can be used to identify songs, get song details, and retrieve related information.

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
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Usage
api_key = "YOUR_RAPIDAPI_KEY"
audio_url = "https://example.com/path/to/audio/file.mp3"

result = recognize_song(api_key, audio_url)

if result:
    print(f"Song Title: {result['track']['title']}")
    print(f"Artist: {result['track']['subtitle']}")
    print(f"Genre: {result['track']['genres']['primary']}")
else:
    print("Failed to recognize the song.")
```

## 9. Article Data Extraction and Text Mining API

The Article Data Extraction and Text Mining API by Ujeebu allows developers to extract meaningful data such as clean text from HTML regardless of the language used.

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
    
    response = requests.get(api_url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Usage
api_key = "YOUR_RAPIDAPI_KEY"
article_url = "https://example.com/path/to/article"

result = extract_article_data(api_key, article_url)

if result:
    print(f"Title: {result['title']}")
    print(f"Author: {result['author']}")
    print(f"Published Date: {result['published_date']}")
    print(f"Content: {result['content'][:200]}...") # Print first 200 characters of content
else:
    print("Failed to extract article data.")
```

## 10. ReCaptcha Solver API

The ReCaptcha Solver API helps developers automatically solve reCAPTCHA v2 & reCAPTCHA v3 challenges and get the g_recaptcha_response for all scraping and captcha-solving needs.

```python
import requests
import time

def solve_recaptcha(api_key, site_key, site_url):
    create_task_url = "https://api.capsolver.com/createTask"
    get_result_url = "https://api.capsolver.com/getTaskResult"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    create_task_payload = {
        "clientKey": api_key,
        "task": {
            "type": "ReCaptchaV2TaskProxyless",
            "websiteURL": site_url,
            "websiteKey": site_key
        }
    }
    
    response = requests.post(create_task_url, json=create_task_payload, headers=headers)
    
    if response.status_code == 200:
        task_id = response.json()["taskId"]
        
        while True:
            get_result_payload = {
                "clientKey": api_key,
                "taskId": task_id}
            
            result_response = requests.post(get_result_url, json=get_result_payload, headers=headers)
            
            if result_response.status_code == 200:
                result = result_response.json()
                if result["status"] == "ready":
                    return result["solution"]["gRecaptchaResponse"]
                elif result["status"] == "processing":
                    time.sleep(5)  # Wait for 5 seconds before checking again
                else:
                    return None
            else:
                return None
    else:
        return None

# Usage
api_key = "YOUR_CAPSOLVER_API_KEY"
site_key = "RECAPTCHA_SITE_KEY"
site_url = "https://example.com/page-with-recaptcha"

result = solve_recaptcha(api_key, site_key, site_url)

if result:
    print(f"ReCaptcha solved. Response: {result}")
else:
    print("Failed to solve ReCaptcha.")
```

## 11. Deezer API

The Deezer API gives developers access to Deezer's massive music database of over 30 million tracks and playlists.

```python
import requests

def search_deezer(query, type='track'):
    url = "https://api.deezer.com/search"
    params = {
        'q': query,
        'type': type
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Usage
search_query = "Bohemian Rhapsody"
results = search_deezer(search_query)

if results and 'data' in results:
    for item in results['data'][:5]:  # Print first 5 results
        print(f"Title: {item['title']}")
        print(f"Artist: {item['artist']['name']}")
        print(f"Album: {item['album']['title']}")
        print(f"Preview URL: {item['preview']}")
        print("---")
else:
    print("No results found or an error occurred.")
```

## 12. API-FOOTBALL

API-Football is a popular RESTful API for football (soccer) data. It covers over 960 football leagues and cups, providing live scores, pre-match odds, events, line-ups, standings, stats, and more.

```python
import requests

def get_league_standings(api_key, league_id, season):
    url = "https://api-football-v1.p.rapidapi.com/v3/standings"
    
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    
    params = {
        "league": league_id,
        "season": season
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Usage
api_key = "YOUR_RAPIDAPI_KEY"
league_id = 39  # English Premier League
season = 2023

results = get_league_standings(api_key, league_id, season)

if results and 'response' in results:
    standings = results['response'][0]['league']['standings'][0]
    for team in standings[:5]:  # Print top 5 teams
        print(f"Rank: {team['rank']}")
        print(f"Team: {team['team']['name']}")
        print(f"Points: {team['points']}")
        print(f"Played: {team['all']['played']}")
        print(f"Won: {team['all']['win']}")
        print(f"Drawn: {team['all']['draw']}")
        print(f"Lost: {team['all']['lose']}")
        print("---")
else:
    print("Failed to retrieve standings or an error occurred.")
```

## 13. ScrapTik API

ScrapTik is a social API that allows developers to scrape data from the TikTok mobile app. The API is used as a gateway for fetching trending videos, users, music, and more.

```python
import requests

def get_trending_videos(api_key):
    url = "https://scraptik.p.rapidapi.com/trending-feed"
    
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "scraptik.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Usage
api_key = "YOUR_RAPIDAPI_KEY"

results = get_trending_videos(api_key)

if results and 'data' in results:
    for video in results['data'][:5]:  # Print first 5 trending videos
        print(f"Author: {video['author']['nickname']}")
        print(f"Video Description: {video['description']}")
        print(f"Likes: {video['stats']['diggCount']}")
        print(f"Comments: {video['stats']['commentCount']}")
        print(f"Shares: {video['stats']['shareCount']}")
        print(f"Video URL: https://www.tiktok.com/@{video['author']['uniqueId']}/video/{video['id']}")
        print("---")
else:
    print("Failed to retrieve trending videos or an error occurred.")
```

## 14. Tiktok video no watermark API

The Tiktok video no watermark API allows developers to download Tiktok videos without watermarks, so they can be posted to other social platforms.

```python
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
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Usage
api_key = "YOUR_RAPIDAPI_KEY"
video_url = "https://www.tiktok.com/@username/video/1234567890123456789"

result = download_tiktok_video(api_key, video_url)

if result and 'data' in result:
    print(f"Author: {result['data']['author']['nickname']}")
    print(f"Video Title: {result['data']['title']}")
    print(f"No Watermark Video URL: {result['data']['play']}")
    print(f"Watermark Video URL: {result['data']['wmplay']}")
    print(f"Music: {result['data']['music']}")
else:
    print("Failed to retrieve video information or an error occurred.")
```

## 15. Rapid Translate Multi Traduction API

The Rapid Translate Multi Traduction API translates HTML, text, words, phrases, and paragraphs in real-time across more than 100 languages.

```python
import requests

def translate_multi(api_key, text, target_lang, source_lang=None):
    url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"
    
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "rapid-translate-multi-traduction.p.rapidapi.com"
    }
    
    payload = {
        "from": source_lang or "auto",
        "to": target_lang,
        "q": text
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Usage
api_key = "YOUR_RAPIDAPI_KEY"
text_to_translate = "Hello, how are you? This is a test of the translation API."
target_language = "fr"  # French

result = translate_multi(api_key, text_to_translate, target_language)

if result:
    print(f"Original text: {text_to_translate}")
    print(f"Translated text: {result}")
else:
    print("Translation failed or an error occurred.")
```

## 16. Youtube v3 API

The Youtube v3 API provides Youtube data without requiring a Youtube data API key.

```python
import requests

def search_youtube(api_key, query, max_results=5):
    url = "https://youtube-v31.p.rapidapi.com/search"
    
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "youtube-v31.p.rapidapi.com"
    }
    
    params = {
        "q": query,
        "part": "snippet,id",
        "regionCode": "US",
        "maxResults": str(max_results),
        "order": "date"
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Usage
api_key = "YOUR_RAPIDAPI_KEY"
search_query = "Python programming"

results = search_youtube(api_key, search_query)

if results and 'items' in results:
    for item in results['items']:
        print(f"Title: {item['snippet']['title']}")
        print(f"Channel: {item['snippet']['channelTitle']}")
        print(f"Description: {item['snippet']['description']}")
        print(f"Video ID: {item['id']['videoId']}")
        print(f"Thumbnail URL: {item['snippet']['thumbnails']['default']['url']}")
        print("---")
else:
    print("Failed to retrieve YouTube search results or an error occurred.")
```

These additional API examples cover a wide range of functionalities, from music and sports data to social media interactions and language translation. Remember to replace the placeholder API keys with your actual keys, handle errors appropriately, and always check the API documentation for the most up-to-date information on endpoints, rate limits, and usage terms.

This concludes our comprehensive guide on using various free APIs with Python. Remember to replace placeholder API keys with your actual keys, handle errors gracefully, and always check the API documentation for the most up-to-date information on endpoints, rate limits, and usage terms.

When using these APIs in your projects, consider the following best practices:

1. Error Handling: Always include proper error handling to manage cases where the API might be unavailable or return unexpected results.

2. Rate Limiting: Be aware of and respect the rate limits for each API to avoid being blocked or incurring unnecessary costs.

3. Data Validation: Validate the data received from the APIs before using it in your application to ensure it meets your expectations and requirements.

4. Caching: Implement caching mechanisms where appropriate to reduce the number of API calls and improve your application's performance.

5. Security: Keep your API keys secure and never expose them in client-side code or public repositories.

6. Asynchronous Requests: For applications that need to make multiple API calls, consider using asynchronous requests to improve performance.

7. Logging: Implement logging to track API usage and help with debugging and monitoring.

By following these practices and leveraging the power of these APIs, you can create robust and feature-rich applications in Python. Happy coding!