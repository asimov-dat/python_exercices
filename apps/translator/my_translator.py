from translate import Translator

translator = Translator(to_lang='fr')

try:
    with open('/home/dat/code/python/python_exercices/apps/translator/o_file.txt', mode = 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as err:
    print('file not found')