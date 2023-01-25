#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

#Examples
#pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    split_text = text.split()
    text = []
    
    for word in split_text:
        if word.isalpha():
            word = word[1:] + word[0:1] + "ay"
            text.append(word)
        else:
            text.append(word)
        
    return " ".join(text) 