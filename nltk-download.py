from nltk.tokenize import sent_tokenize
import nltk

# nltk.download('punkt_tab')

text = "This is sentence one. This is sentence two."
print(sent_tokenize(text))