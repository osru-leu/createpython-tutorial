




max_tries = 5    
tries = 0    

while tries < max_tries:

    WORD = input('Type a word: ')
    tries += 1
    if not WORD.endswith('ing'):
        print('I dont understand that')
        #WORD = w(WORD)
       
    else:
        print('You got your adverb')
        break

else:
    print('You hit 5 tries')
    
    