#!/usr/bin/env python3

# Nick Stucchi
# 03/23/2017
# Filter out words and replace with dashes

def replaceWord(sentence, word):
    wordList = sentence.split()
    newSentence = []
    for w in wordList:
        if w == word:
            newSentence.append("-" * len(word))
        else:
            newSentence.append(w)
    return " ".join(newSentence)
    




def main():
    sentence = input("Enter a sentence: ")
    word = input("Enter a word to replace: ")
    result = input("The resulting string is: " + "\n" + replaceWord(sentence, word))
    print(result)
    
    



if __name__ == "__main__":
    main()
