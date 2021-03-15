import unittest

from word_searcher import WordSearcher
from word_searcher import TrieNode
from word_searcher import insert_word


class WordSearcherTest(unittest.TestCase):

    def test_insert_word_into_trie_node(self):
        root = TrieNode()
        insert_word(root, 'a')
        self.assertEqual(root.children[0].word, 'a', "word in last node of chain should equal to initial word")

    def test_word_searcher(self):
        board = [['a', 'c'], ['b', 'd']]
        expected_words = ['ab', 'a']

        root = TrieNode()
        insert_word(root, 'ab')
        insert_word(root, 'a')

        searcher = WordSearcher()
        searcher.find_words(board, root)

        self.assertTrue(set(searcher.found_words) == set(expected_words))


if __name__ == '__main__':
    unittest.main()
