# Implementation of Trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        curr = self.root
        for char in string:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEnd = True

    def search(self, string):
        curr = self.root
        for char in string:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isEnd

# Driver code 
trie = Trie()
trie.insert("Hello")
trie.insert("gringer")
trie.insert("geology")
trie.insert("welcome")
print(trie.search("Hello"))
print(trie.search("welcomr"))

