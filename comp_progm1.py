def length_of_last_word(s):
    #splitting the sentance into parts words and spaces 
    words = s.split()
    
    
    if len(words) == 0:
        return 0
    
    
    last_word = words[-1]
    return len(last_word)


s = input("Enter a sentence: ")
l = length_of_last_word(s)
print( l)
