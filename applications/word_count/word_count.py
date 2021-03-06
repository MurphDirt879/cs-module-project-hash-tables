import re

def word_count(s):
    # Your code here
    counts = {}
    
    ignoreList = str.maketrans('', '', '":;,.-+=/\\|[]{}()*^&')

    words = s.translate(ignoreList).lower().split()
    
    for word in words : 
        if word in counts: 
            counts[word] += 1
        else:
            counts[word] = 1
    
    
    return(counts)


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))