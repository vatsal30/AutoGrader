#PREPROCESSING STAGE 2
'''The first calling function for this file will be process2 having two file arguments. The first arguments denotes the input file (file to read from) and the second argument denotes the output file (file to write on)'''

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import pandas as pd

def get_part_of_speech(tokens,index):

    pos = nltk.pos_tag(tokens)
    
    if pos[index][1].startswith('V'):
        return str(wordnet.VERB)
    elif pos[index][1].startswith('N'):
        return str(wordnet.NOUN)
    elif pos[index][1].startswith('J'):
        return str(wordnet.ADJ)
    elif pos[index][1].startswith('R'):
        return str(wordnet.ADV)
    else:
        return 'n'
        
#function gets called from process2
def cleantext(text, lemmatizer):
    
    sentences = nltk.sent_tokenize(text)
    
    text = ''
    
    punctuations="?:!.,;"
    for sentence in sentences:
        word_count = 0
        words = nltk.word_tokenize(sentence)
        for word in words:
            if word in punctuations: text = text + " " + word
            else: text = text + " " + lemmatizer.lemmatize(word,get_part_of_speech(words,word_count))
            word_count += 1
            
    return text
    
#function to be called to initiate lemmatization
def process2( nameFileIn, nameFileOut):
    lemmatizer = WordNetLemmatizer()
    
    print 'PREPROCESSING STAGE 2: Lemmatization'
    reader = open(nameFileIn, 'r' )
    fi = open( nameFileOut , "w")
    for row in reader:
       line = row.split('\t')
       for i in range(len(line)-1):
            if i == 1:
                print 'Processing SET: ' + line[i] + ' EssayID: ' + line[i-1]
            
            fi.write( line[i] + '\t' )
           
       text =  cleantext( line[len(line) - 1] , lemmatizer)
       fi.write( text + '\n')
       

process2('output_train_processed1.tsv','output_train_processed2.tsv')

