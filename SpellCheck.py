# Chaya Trapedo
from BloomFilter import *
import string

# create a Bloom filter of all words
def importWords():
    
    numWords = 645_288
    numHashes = 5
    maxFalse = .0001
    
    # create the Bloom Filter
    engWords = BloomFilter(numWords, numHashes, maxFalse)
    
    # import all words into Bloom Filter
    wordlist = open("words.utf-8.txt")
    for i in range(numWords):
        word = wordlist.readline().strip()
        engWords.insert(word)
    
    # Close the input file
    wordlist.close() 
    return engWords
    

def checkSpelling(engWords):
    word = ""
    
    while word != "-1":
    
        word = input("Enter a word to check the spelling of: " )
        word = word.lower().strip()
        correct = engWords.find(word)
        
        if word != "-1":
            
            if correct: print(f"{word} is spelled correctly\n")
            else: print(f"{word} is not spelled correctly\n")


def __main():
    
    print("To quit, enter \"-1\"")
    engWords = importWords()
    checkSpelling(engWords)

        
if __name__ == '__main__':
    __main()    
