# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    words = text.split()
    
    language_guess = ''
    valid_word_max = 0
    num_words = {}
    for language in languages:
        # The languages are stored in a list of dictionaries
        # we will go through each language checking for valid words.
        valid_words = 0
        for word in words:
            word = word.lower()
            word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
            
            if word in language['common_words']:
                valid_words += 1
                
        #compares valid_words to select the largest and updates language_guess 
        if valid_words > valid_word_max: 
            valid_word_max = valid_words
            language_guess = language['name']
        
    return language_guess
        
        
