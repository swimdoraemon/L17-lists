def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of word with the first and last character is same\n", lst)
    return ctr
count = match_words(['abc','cfc','xyz','aba', '1221'])
print("Numbers of words having the first and last character same:", count)