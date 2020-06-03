def no_dups(s):
    # Your code here
    w = s.split()

    singles = []
    duplicates = {}

    for x in w:
        if x not in duplicates:
            singles.append(x)
            duplicates[x] = True

    return " ".join(singles)
    




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))