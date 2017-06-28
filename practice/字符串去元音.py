def anti_vowel(text):
    ret = ""
    for char in text:
        if char.lower() in "aeiou" :
            char = ""
        ret += char
    return ret