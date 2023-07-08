from deep_translator import MyMemoryTranslator
 

def englishToFrench(englishText):
    '''
    docstring for this function
    '''

    frenchText = MyMemoryTranslator(source='en', target='fr').translate(text=englishText)
    return frenchText


def frenchToEnglish(frenchText):
    '''
    docstring forthe function
    '''
    englishText = MyMemoryTranslator(source='fr', target='en').translate(text=englishText)
    return englishText