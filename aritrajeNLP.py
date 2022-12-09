import spacy
from spacy.matcher import Matcher

def removeStopWords(text):
    sp = spacy.load('es_core_news_sm')
    all_stopwords = sp.Defaults.stop_words
    text_tokens = sp(text)
    tokens_without_sw= [word for word in text_tokens if not word.orth_ in all_stopwords]
    tokens_to_string=[word.text.strip() for word in tokens_without_sw]
    tokens_to_text= ' '.join(tokens_to_string)
    return tokens_to_text

def getParams(text):

    nlp = spacy.load("es_core_news_sm")
    matcher = Matcher(nlp.vocab)
    
    pattern = [{"LOWER": "licenciatura"}, {"IS_PUNCT": True}, {"LOWER": "derecho"}]
    pattern2 = [{"LOWER": "licenciatura"}, {"LOWER": "en"}, {"LOWER": "derecho"}]
    pattern3 = [{"LOWER": "lic."}, {"LOWER": "derecho"}]
    pattern4 = [{"LOWER": "derecho"}]
    pattern5 = [{"LOWER": "licenciatura"}, {"LOWER": "derecho"}]
    matcher.add("DER", [pattern,pattern2,pattern3,pattern4,pattern5])

    #Postgrado para 'Arbitraje'
    pattern = [{"LOWER": "postgrado"}, {"IS_PUNCT": True}, {"LOWER": "arbitraje"}]
    pattern2 = [{"LOWER": "postgrado"}, {"LOWER": "en"}, {"LOWER": "arbitraje"}]
    pattern3 = [{"LOWER": "postgrado"},{"LOWER": "arbitraje"}]
    pattern4 = [{"LOWER": "arbitraje"}]
    pattern5 = [{"LOWER": "inglés"}]
    matcher.add("DER-248", [pattern,pattern2,pattern3,pattern4,pattern5])

    text_without_sw=removeStopWords(text)
    params=[]
    doc = nlp(text_without_sw)
    matches = matcher(doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        span = doc[start:end]  # The matched span
        print(match_id, string_id, start, end, span.text)
        params.append({'string_id':string_id,'text':span.text})
    return params