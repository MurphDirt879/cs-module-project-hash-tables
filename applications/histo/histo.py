with open("robin.txt") as f:
    words = f.read()


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



counts = list(word_count(words).items())
longest =0
for count in counts: 
    count_lenght = len(count[0])
    if count_lenght > longest:
        longest = count_lenght



counts.sort(key=lambda element: (-element[1], element[0]))


for word in counts:
    space = ' ' * (longest - len(word[0]))
    numberOfHashes = '#' * word[1]
    print(word[0] + space + numberOfHashes)

