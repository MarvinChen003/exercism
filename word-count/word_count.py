import re


def count_words(sentence):
    words = re.split(r'\s|\n|,|_', sentence)
    words_formatted = reformat_list(words)
    return count_formatted_words(words_formatted)


def clear_header(word):
    for i in range(len(word)):
        if word[i].isnumeric() or word[i].isalpha():
            return word[i:]


def clear_tailer(word):
    for i in range(len(word)-1,-1,-1):
        if word[i].isnumeric() or word[i].isalpha():
            return word[:i+1]


def count_formatted_words(words):
    words_count = {}
    for word in words:
        word_count = words.count(word)
        words_count[word] = word_count
    return words_count


def reformat_list(words):
    reformated_words=[]
    for word in words:
        word=clear_header(word)
        if not word:
            continue
        word=clear_tailer(word)
        reformated_words.append(word.lower())
    return reformated_words


# Solution from others

# Solution 1
# Nice to use enumerate and strip functions
# setdefault is also nice to be used
# def count_words(sentence):
#     words = sentence.lower().replace(',', ' ').replace('_', ' ').split()
#     wordCount = {}
#     for i, word in enumerate(words):
#         cleanedWord = word.strip('?!,\'\".:;/~$()-@#%^&')
#         wordCount.setdefault(cleanedWord, 0)
#         wordCount[cleanedWord] += 1
#     return wordCount


# Solution 2
# strinng sub
# Counter collection
# import re
# from collections import Counter
#
# def count_words(sentence):
#     words = re.split('\s|,|\.|_', sentence)  # split on whitespace or specific characters
#     words = [w.lower() for w in words if len(w) > 0]  # lowercase & drop empty words
#     words = [re.sub(r"[^a-z'0-9]", '', w) for w in words]  # strip punctuation
#     words = [re.sub(r"^'+", '', w) for w in words]  # strip leading apostrophe's
#     words = [re.sub(r"'+$", '', w) for w in words]  # strip trailing apostrophe's
#     return Counter(words)
