from nltk.tokenize import sent_tokenize
# load text from 1st chapter
with open('18043-0.txt', 'r') as f: 
    data = f.read()
    paragraphs = data.split("\n\n")
