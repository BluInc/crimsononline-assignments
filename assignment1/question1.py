"""
Question 1

objectives
    - get more comfortable with Python
    - learn how to handle exceptions
    - work with the file system
"""
import re

def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    f = open(filename)
    wordDict = {}

    for line in f.readlines():
        for word in line.split():
            mod_word = re.sub(r'[^a-z]','',word.lower())
            if(mod_word in wordDict):
                wordDict[mod_word] += 1
            else:
                wordDict[mod_word] = 1

    f.close()

    print sorted(wordDict, key=wordDict.get)[::-1]

def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    f = open(filename)
    wordDict = {}

    for line in f.readlines():
        for word in line.split():
            mod_word = re.sub(r'[^a-z]','',word.lower())
            if(len(mod_word) >= min_chars):
                if(mod_word in wordDict):
                    wordDict[mod_word] += 1
                else:
                    wordDict[mod_word] = 1

    f.close()

    print sorted(wordDict, key=wordDict.get)[::-1]

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    f = open(filename)
    wordDict = {}

    for line in f.readlines():
        for word in line.split():
            mod_word = re.sub(r'[^a-z]','',word.lower())
            if(len(mod_word) >= min_chars):
                if(mod_word in wordDict):
                    wordDict[mod_word] += 1
                else:
                    wordDict[mod_word] = 1

    f.close()

    print sorted(wordDict.items(), key=lambda x: x[1])[::-1]

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    try:
        f = open(filename)
    except IOError:
        print 'cannot open file', filename
    else:

        wordDict = {}

        for line in f.readlines():
            for word in line.split():
                mod_word = re.sub(r'[^a-z]','',word.lower())
                if(len(mod_word) >= min_chars):
                    if(mod_word in wordDict):
                        wordDict[mod_word] += 1
                    else:
                        wordDict[mod_word] = 1

        f.close()

        print sorted(wordDict.items(), key=lambda x: x[1])[::-1]