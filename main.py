from googletrans import Translator

translator = Translator()
text = translator.translate('Hello', src='en', dest='ro')
print(text.text)
