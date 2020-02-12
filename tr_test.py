from translate import Translator





def rus_ua(word):
    translator = Translator(to_lang="en", from_lang='ru')
    translation = translator.translate(f"{word}")
    return translation

print(rus_ua('Рождения народа'))