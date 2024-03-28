# Bloom Filter and Spell Check Demonstration
## What's a Bloom filter?
A Bloom filter is a tunable probabilistic data structure that performs memory-efficient membership queries. On the backend, a Bloom filter is a hash table that stores the hashes of elements in a set, and because it does not store the keys, it is incredibly memory efficient - Bloom filters only need the amount of space to store the number of underlying bits and insertion and sort are always accomplished in O(1) time. Bloom filters have the possibility of returning a false positive if keys are hashed to the same locations, however, a Bloom filter can't return a false negative. [Learn more about Bloom filters.](https://en.wikipedia.org/wiki/Bloom_filter#)
## See it in action!
Early spell checkers were implemented with Bloom filters. Download the files and run `SpellCheck.py` to interact with a Bloom filter's spell-checking abilities in the shell.
## Resources
- `words.utf-8.txt` and `wordlist.txt` from [Princeton CS Real-World Data Sets](https://introcs.cs.princeton.edu/java/data/)
- `BitHash.py` from Professor Alan J. Broder
- `BitVector.py` from Avinash Kak
