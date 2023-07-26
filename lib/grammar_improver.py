

def grammar_improver(text):
    if text == "":
        raise Exception("No text input provided")
    punctuation_list = [".","?","!"]
    last_letter = text[-1]
    
    if last_letter in punctuation_list and text[0].isupper():
        return "Correct use of grammar"
    else:
        return "Incorrect use of grammar"
        
        
    
    