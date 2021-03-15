import random
import string
import sys
from typing import List


class TrieNode:
    """Trie Node implementation"""

    def __init__(self):
        self.children = [None] * 26
        self.word = None


class WordSearcher:
    """Word Search implementation"""
    found_words = []

    def find_words(self, board: List[List[str]], root: TrieNode) -> List[str]:
        """Looking for words in a board, which are provided in dictionary
            which is implemented as a TrieNode"""
        if not board:
            return []

        for i in range(len(board)):
            for j in range(len(board[0])):
                ch = board[i][j]
                if root.children[ord(ch) - ord('a')] is not None:
                    self.dfs(board, i, j, root)

        return self.found_words

    def dfs(self, board: List[List[str]], i, j, node: TrieNode):
        """Depth First Search implementation
            to find required words in TrieNode"""
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return

        checked = '!'
        ch = board[i][j]

        if ch == checked or node.children[ord(ch) - ord('a')] is None:
            return

        node = node.children[ord(ch) - ord('a')]
        if node.word is not None:
            self.found_words.append(node.word)
            node.word = None  # mark as None to avoid words duplication

        board[i][j] = checked
        self.dfs(board, i-1, j, node)  # check left neighbour
        self.dfs(board, i+1, j, node)  # check right neighbour
        self.dfs(board, i, j-1, node)  # check top neighbour
        self.dfs(board, i, j+1, node)  # check bottom neighbour
        self.dfs(board, i+1, j-1, node)  # check top right (/) diagonal neighbour
        self.dfs(board, i+1, j+1, node)  # check bottom right (\) diagonal neighbour
        # NOTE: I didn't include [i-1,j-1] and [i-1,j+1] directions intentionally,
        # because this behavior isn't clearly stated in the assignment.
        # In case you need those directions as well, you may uncomment next two lines:
        # self.dfs(board, i-1, j-1, node) # top left (\) neighbour
        # self.dfs(board, i-1, j+1, node) # bottom left (/) neighbour
        board[i][j] = ch


def get_random_letter():
    """Generates the random lower case letter"""
    return random.choice(string.ascii_lowercase)


def generate_board(n, m):
    """Generates the board of random letters with a given size"""
    a = []
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(get_random_letter())
        a.append(tmp)
    return a


def insert_word(root: TrieNode, word: str):
    """Insert new word into TrieNode"""
    node = root
    for ch in word.rstrip("\n"):
        if node.children[ord(ch) - ord('a')] is None:
            node.children[ord(ch) - ord('a')] = TrieNode()
        node = node.children[ord(ch) - ord('a')]
    node.word = word


def prepare_dictionary(file_name: str, root: TrieNode):
    """Prepare dictionary of searched words from the provided file
        This method reads every line in the provided file and put them into TrieNode

        Note: it may be time consuming if file is big"""
    with open(file_name, 'r') as words:
        lines = words.readlines()
        for line in lines:
            insert_word(root, line)


def strip_output(arr: List[str]) -> List[str]:
    """Truncate trailing new line character in list elements"""
    stripped_words = []
    for w in arr:
        stripped_words.append(w.strip())
    return stripped_words


if __name__ == '__main__':
    if len(sys.argv) < 4:
        sys.exit("Insufficient number of arguments")
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        words_path = sys.argv[3]

    game_board = generate_board(n, m)
    print("Generated board:")
    for ar in game_board:
        print(ar)

    root_node = TrieNode()
    prepare_dictionary(words_path, root_node)

    searcher = WordSearcher()
    print("Found words:")
    found_words = strip_output(searcher.find_words(game_board, root_node))
    print(found_words)
