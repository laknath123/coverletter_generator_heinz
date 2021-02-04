# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 12:30:30 2021

@author: lakna
"""
def enter_job_descrip():
    import nltk
    from nltk import sent_tokenize
    from nltk import word_tokenize
    from nltk.corpus import stopwords
        
    sent= input("Enter the Internship Description :")
    
    words = word_tokenize(sent)
    
    words_no_punc=[]
    
    for w in words:
        if w.isalpha():
            words_no_punc.append(w.lower())
            
    stopwords = stopwords.words("english")
    
    clean_words= []
    
    for w in words_no_punc:
        if w not in stopwords:
            clean_words.append(w)
     
    descrip=nltk.ne_chunk(clean_words,True)
    print(descrip)


if __name__ == "__main__": # two underscores each
    enter_job_descrip()