cache = {}
​
def fib(n):
    if n <= 1:
        return n
​
    if n not in cache:   # if n is not a key in the cache
        cache[n] = fib(n-1) + fib(n-2)
​
    return cache[n]
​
for i in range(95):
    print(f'{i:3} {fib(i)}')







def expensive_function(x, y):
    key = (x, y)
    if key not in cache:   # if n is not a key in the cache
        cache[key] = whatever_expensive_thing_here()
    return cache[key]
    nv_sqrt = {}
​
​
​
def build_lookup_table():
​
    for i in range(1, 1000):
        inv_sqrt[i] = 1 / math.sqrt(i)
​
build_lookup_table()
​
​
​
​
print(inv_sqrt[3])
print(inv_sqrt[12])

d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}
​
print(d.values())
items = list(d.items())
​
# Sort ascending by key
items.sort()
​
print(items)
​
# Sort decending by key
items.sort(reverse=True)
​
print(items)
# Sort ascending by value
​
"""
def get_key(e):  # e is going to be the tuple
    # Return the thing that we want to sort by
    return e[1]
​
items.sort(key=get_key)
"""
items.sort(key=lambda e: e[1])
​
print(items)

def print_letter_count(s):
    counts = {}
​
    for c in s:
        #c = c.lower()  # case insensitive
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
​
    items = list(counts.items())
    items.sort(key=lambda e: e[1])
​
    print(items)
​
print_letter_count("aaabbcbcaAA!")

# Caesar Cipher
​
encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}
​
decode_table = {}
​
def build_decode_table():
    for key, value in encode_table.items():
        decode_table[value] = key
​
def encode(s):
    r = ""
​
    for c in s:
        if c in encode_table:
            r += encode_table[c]
        else:
            r += c
​
    return r
​
​
def decode(s):
    r = ""
​
    for c in s:
        if c in decode_table:
            r += decode_table[c]
        else:
            r += c
​
    return r
​
build_decode_table()
​
print(encode("HELLO, WORLD!"))
​
print(decode("DOGGE, BEUGW!"))
​