'''THis is the module for translating english to french and french to english
'''

from deep_translator import MyMemoryTranslator


def english_to_french(english_text):

    '''
    convert english to french
    >>>english_to_french('Hello')
    >>>'Bonjour'
    '''

    french_text = MyMemoryTranslator(source='english', target='french').translate(text=english_text)
    return french_text


def french_to_english(french_text):

    '''
    convert english to french
    >>>english_to_french('Bonjour')
    >>>'Hello'
    '''
    english_text = MyMemoryTranslator(source='french', target='english').translate(text=french_text)
    return english_text
