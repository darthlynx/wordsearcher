# Word Searcher

This is the implementation of Word Search game<br>
This is a puzzle where words are hidden in a grid of seemingly random letters.

Words can be found along any diagonal, forwards, upwards, downwards or backwards

`word_searcher.py` module provides possibility to look for all words from the dictionary, which is given
as a list of words in standalone file


## Prerequisites

1. Python3.6 or higher
2. text file with dictionary (each line should have single word consists of lowercase English letters)


## Run

```bash
python3 word_searcher.py <N> <M> <PATH_TO_DICTIONARY>
```

where:
- N and M - dimension of board to be generated
- PATH_TO_DICTIONARY - path to file with dictionary

> NOTE: all arguments are required
 
For example:

```bash
python3 word_searcher.py 5 5 words.txt
```

## Output

Result of the output is the generated board (provided as a two-dimensional array), and the list of found words

## Test

```bash
python3 word_searcher_test.py
```

