"""translator english to french and vice-versa"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('Wfdx5CQazUQ2nD-Sw-G-GRH-G6izo7rbPdEzoA5NydEi')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """english to French translation"""
    translation= language_translator.translate(text=english_text, model_id="en-fr").get_result()
    french_text=translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """french to English translation"""
    translation= language_translator.translate(text=french_text, model_id="fr-en").get_result()
    english_text=translation['translations'][0]['translation']
    return english_text
