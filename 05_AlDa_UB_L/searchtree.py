import unittest
from random import randint
import copy


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None

class SearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def treeInsert_(self, node, key, value):
        if node is None:
            self.size += 1
            return Node(key, value)

        if node.key == key:
            node.value = value
            #return node
        elif key < node.key:
            node.left = self.treeInsert_(node.left, key, value)
        else:
            node.right = self.treeInsert_(node.right, key, value)

        return node

    def searchTree_(self, node, key):
        if node is None:
            return None
        elif node.key == key:
            return node
        elif key < node.key:
            return self.searchTree_(node.left, key)
        else:
            return self.searchTree_(node.right, key)

    def treePredecessorleft(self, node):
        '''Finde '''
        node = node.left
        while node.right is not None:
            node = node.right
        return node

    def treeRemove_(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self.treeRemove_(node.left, key)
        elif key > node.key:
            node.right = self.treeRemove_(node.right, key)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                pred = self.treePredecessorleft(node)
                node.key = pred.key
                node.left = self.treeRemove_(node.left, pred.key)

        return node

    def insert(self, key, value):
        self.root = self.treeInsert_(self.root, key, value)

    def remove(self, key):
        self.root = self.treeRemove_(self.root, key)
        self.size -= 1

    def find(self, key):
        return self.searchTree_(self.root, key)

    def depth(self):
        return self.preOrderDepth_(self.root, 0)

    def preOrderDepth_(self, node, depth):
        depth1, depth2 = 0, 0
        if node.left is not None:
            depth1 = self.preOrderDepth_(node.left, depth + 1)
        if node.right is not None:
            depth2 = self.preOrderDepth_(node.right, depth + 1)
        return max(depth1, depth2, depth)






class TestSearchTree(unittest.TestCase):

    def setUp(self):
        self.randDataTree = SearchTree() #Testbaum
        self.size = randint(10,100) #zufüllige Groesse

        # abspeichern der zufälligen keys
        self.randkey_list = []

        for i in range(0, self.size):
            randkey = randint(100, 1000)
            # keine keys sollen doppelt vorkommen
            while self.randkey_list.count(randkey) is not 0:
                randkey = randint(100, 1000)

            self.randkey_list.append(randkey)
            self.randDataTree.insert(randkey, i)

        # Sortierte Liste der keys erstellen zum späteren 'zufälligen' Zugriff auf die Baumstruktur
        self.randkey_list_sorted = copy.deepcopy(self.randkey_list)
        self.randkey_list_sorted.sort()

        # geplanten Tree erstellen zum überprüfen von depth()
        self.cusDataTree = SearchTree()
        cuskey_list = [3,56,2,5,9,7,12]
        for key in cuskey_list:
            self.cusDataTree.insert(key, key)


    def testSize(self):
        '''Testcase'''
        self.assertTrue(self.size is self.randDataTree.size, 'Size not equal')

    def testDepth(self):
        self.assertTrue(self.cusDataTree.depth() is 4, 'Err in depth()')

    def testFind(self):
        for key in self.randkey_list:
            self.assertTrue(self.randDataTree.find(key) is not None, 'Set key could not be found, error in tree.find()')
        self.assertTrue(self.randDataTree.find(randint(0, 99)) is None, 'Not existing key was found, error in tree.find()')

    def testOverwrite(self):
        key = self.randkey_list[int(self.size / 2)]
        old = self.randDataTree.find(key).value
        self.randDataTree.insert(key, old+1)

        self.assertTrue(self.randDataTree.find(key).value is old + 1, 'overwrite of existing key did not work')

    def testRemove(self):
        for key in self.randkey_list_sorted: # sorted, weil so nicht der reihenfolge nach im Baum gelöscht wird, sondern 'zufällig'
            size = self.randDataTree.size
            self.randDataTree.remove(key)
            self.assertTrue(self.randDataTree.find(key) is None, 'Err in remove(), key not removed')
            self.assertTrue(self.randDataTree.size is size - 1, 'Err in remove(), size not correct')

        self.assertTrue(self.randDataTree.root is None, 'Deleting everything did not result in empty Tree')



dataTree = SearchTree()

dataTree.insert(1, 'eins')
dataTree.insert(2, 'zwei')
dataTree.insert(3, 'drei')
dataTree.insert(4, 'vier')
dataTree.insert(1.5, 'eineinhalb')
dataTree.remove(4)
print(dataTree.depth())




unittest.main()

if __name__ is '__main__':
    unittest.main()