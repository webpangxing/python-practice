def censor(text,word):
    text = text.split(' ')
    length = len(word)
    for i in text:
        print(i)
        if i == word:
           text[text.index(i)] = "*" * length
    text = ' '.join(text)
    print (text)
    return text
censor('hello world','hello')