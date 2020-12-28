from collections import defaultdict
text = open("2600-0.txt", "r")

def word_count(f):

    words = f.read().split(" ")
    word_freq = defaultdict(int)
    for word in words:
        if word.endswith("\n"):
            word_freq[word[:-2]] += 1
        if word != ".!,:/;-&)(" or word != "\n":
            word_freq[word] += 1


    return sorted(word_freq.items(), key = lambda a: a[1])[::-1]

def top_ten():
    req = word_count(text)[:10]
    for word,freq in req:
        print(word, freq)


print(top_ten())
