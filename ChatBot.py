import nltk
from chatterbot import ChatBot
from chatterbot.trainers import  ListTrainer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
text="natural language proceesing (nlp) is a field of computer since , artificial intelligence"
print(word_tokenize(text))
lemmataizer = WordNetLemmatizer()
print("rocks: ",lemmataizer.lemmatize("Rocks"))
live=['goods','nice','awsome']
ps= PorterStemmer()
my_bot=ChatBot(name="pybot",read_only=True,logic_adapters=['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])
