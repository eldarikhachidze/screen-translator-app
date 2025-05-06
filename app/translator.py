import requests
from app.config import GOOGLE_TRANSLATE_API_KEY

def translate_text(text, target_lang="en"):
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        'q': text,
        'target': target_lang,
        'format': 'text',
        'key': GOOGLE_TRANSLATE_API_KEY,
    }
    response = requests.post(url, data=params)
    result = response.json()
    return result['data']['translations'][0]['translatedText']