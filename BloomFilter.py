# Chaya Trapedo 
from BitHash import *
from BitVector import *


class BloomFilter(object):
    
    # Calculates the amount of bits needed to create the underlying BitVector
    # based on the number of keys, hash functions, and desired false positive rate
    def __bitsNeeded(self, numKeys, numHashes, maxFalsePositive):
        
        ratioStillZero = 1 - (maxFalsePositive**(1/numHashes))
        return numHashes / (1 - (ratioStillZero ** (1/numKeys)))
    
    # Initializes a Bloom filter that will store numKeys keys, using 
    # numHashes hash functions, and that will have a false positive 
    # rate of maxFalsePositive
    def __init__(self, numKeys, numHashes, maxFalsePositive):
        self.____numHashes = numHashes
        self.__maxFalsePositive = maxFalsePositive
        self.__vectorSize = round(self.__bitsNeeded(numKeys, numHashes, maxFalsePositive)) # has to be an int
        self.__array = BitVector(size=self.__vectorSize)
        self.__setBits = 0 # Track amount of bits set to calculate actual false positive rate 
    
    # insert the specified key into the Bloom filter
    def insert(self, key):
        
        # hash the key __numHashes times to find location in BitVector 
        for i in range(self.____numHashes):
            location = BitHash(key, hashFuncNum=(i+1)) % self.__vectorSize
            
            # Even if hashes overlap locations, only track new bits set
            if self.__array[location] != 1:
                self.__array[location] = 1
                self.__setBits += 1
    
    # Returns True if key MAY have been inserted, False if it definitely has not
    def find(self, key):
        for i in range(1, self.____numHashes+1):
            location = BitHash(key, i) % self.__vectorSize
            if self.__array[location] == 0: return False
        return True
       
    # Returns the project current false positive rate based on the
    # current number of bits actually set in this Bloom filter
    def falsePositiveRate(self): return (self.__setBits/self.__vectorSize)**self.____numHashes
       
    # Returns the current number of bits ACTUALLY set in this Bloom Filter
    def numBitsSet(self): return self.__setBits
            

# demonstrates functionality of Bloom filter with English words file      
def __main():
    numKeys = 100_000
    numHashes = 4
    maxFalse = .05
    
    # create the Bloom Filter
    engWords = BloomFilter(numKeys, numHashes, maxFalse)
    
    # read the first numKeys words from the file and insert them 
    # into the Bloom Filter
    wordlist = open("wordlist.txt")
    for i in range(numKeys):
        word = wordlist.readline()
        engWords.insert(word)
    # Close the input file.
    wordlist.close()
    
    # Print out what the PROJECTED false positive rate should 
    # THEORETICALLY be based on the number of bits that ACTUALLY ended up being set
    # in the Bloom Filter.
    print(f"The projected false positivity rate is {round(engWords.falsePositiveRate(),5)} ({round((engWords.falsePositiveRate()*100),2)}%)")

    # Re-openning the file and re-reading the same bunch of the first numKeys 
    # words from the file to check how many are missing from the Bloom Filter (will be 0)
    wordlist = open("wordlist.txt")
    numMissing = 0
    for i in range(numKeys):
        word = wordlist.readline()
        if not engWords.find(word): numMissing += 1
    print(f"There are {numMissing} keys missing from the Bloom Filter")
    
    # Reading the next numKeys words from the file, none of which 
    # have been inserted into the Bloom Filter, to count how many of the 
    # words can be (falsely) found in the Bloom Filter to compare projected 
    # false positive rate to actual false positive rate
    falsePositive = 0
    for i in range(numKeys):
        word = wordlist.readline()
        if engWords.find(word): falsePositive += 1
        
    print(f"The actual false positivity rate is {round(falsePositive/numKeys, 5)} ({round((falsePositive/numKeys)*100, 2)}%)")

    
if __name__ == '__main__':
    __main()       