
"""Lists all available languages."""
from google.cloud import translate_v2 as translate

translate_client = translate.Client()

results = translate_client.get_languages()

for language in results:
    print("{name} ({language})".format(**language))


