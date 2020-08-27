from googletrans import Translator

f = open('source.txt', 'r')
sentence = f.read()
f.close()

translator = Translator()
text = translator.translate(sentence, src='nl', dest='ro')

print(text.text)
