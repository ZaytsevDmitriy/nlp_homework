import re
from nltk.corpus import stopwords
from pymystem3 import Mystem

regex = re.compile("[А-Яа-я]+")

def words_only(text, regex=regex):
  # Оставляет только слова в нижнем регистре
    try:
        return " ".join(regex.findall(text)).lower()
    except:
        return ""

mystopwords = stopwords.words('russian') + ['это', 'наш' , 'тыс', 'млн', 'млрд', 'также', 'т', 'д', 'г']
def remove_stopwords(text, mystopwords=mystopwords):
  # Удаляет стопслова
    try:
        return " ".join([token for token in text.split() if not token in mystopwords])
    except:
        return ""

m = Mystem()

def lemmatize(text, mystem=m):
    try:
        return "".join(m.lemmatize(text)).strip()
    except:
        return " "

def pre_process(text):
  text = lemmatize(remove_stopwords(words_only(text)))
  return text