def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    for c1 in word1:
        for c2 in word2:
            if c1 == c2:
                word2 = word2.replace(c2, '', 1)
                break
    return word2 == ''

def is_anagram_recursive(word1, word2):
    if word1 != '':
        c1 = word1[0]
        if c1 in word2:
            word2 = word2.replace(c1, '', 1)
            return is_anagram_recursive(word1[1:], word2)
        else:
            return False
    if word1 == '' and word2 == '':
        return True


if __name__ == '__main__':
    word1 = input('Введите первое слово: ')
    word2 = input('Введите второе слово: ')
    is_anagram(word1, word2)
