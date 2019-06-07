from copy import deepcopy
import unittest
from random import random

class Node:
    def __init__(self, key, value, priority):
        self.key = key
        self.value = value #habe value nicht entfernt, wäre mehr Aufwand gewesen, die Funktion zu entfernen, als sie zu behalten
        self.priority = priority
        self.left = self.right = None

    def __repr__(self):
        return f'({self.key}: {self.value})'


class RandomTreap:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def __insert(self, node, key, value):
        if node is None:
            self.size += 1 # key not yet in tree, hence size is increased
            return Node(key, value, random()) #zufällige priorität aus random package
        elif key < node.key:
            node.left = self.__insert(node.left, key, value)
            if node.left.priority > node.priority: #rotation falls priority größer als die von Papa
                node=self.__rotateRight(node)
            return node
        elif key > node.key:
            node.right = self.__insert(node.right, key, value)
            if node.right.priority > node.priority: #rotation falls priority größer als die von Papa
                node=self.__rotateLeft(node)
            return node
        elif key == node.key:
            node.value = value
            return node
        else:
            raise RuntimeError(f'Keys {key} and {node.key} do not compare')

    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value)

    def __remove(self, node, key):
        if node is None:
            raise KeyError(f'Key {key} not in tree')
        elif key < node.key:
            # the Node to remove is in the left subtree
            node.left = self.__remove(node.left, key)
            return node
        elif key > node.key:
            # the Node to remove is in the right subtree
            node.right = self.__remove(node.right, key)
            return node
        elif key == node.key:
            # node must be removed
            if node.left is None and node.right is None:
                # node is replaced by None
                return None
            elif node.left is None:
                # node is replaced by node.right
                return node.right
            elif node.right is None:
                # node is replaced by node.left
                return node.left
            else:
                # pred is the Node below node with the next smaller key, i.e.
                # n.key < pred.key < node.key for all n in the subtree with
                # root node.left
                pred = node.left
                while pred.right is not None:
                    pred = pred.right
                # remove pred from left subtree as it will replace node
                left = self.__remove(node.left, pred.key)
                pred.left = left
                pred.right = node.right
                return pred
        else:
            raise RuntimeError(f'Keys {key} and {node.key} do not compare')

    def remove(self, key):
        self.root = self.__remove(self.root, key)
        self.size -= 1

    def __find(self, node, key):
        if node is None:
            return None
        elif key < node.key:
            return self.__find(node.left, key)
        elif key > node.key:
            return self.__find(node.right, key)
        elif key == node.key:
            return node
        else:
            raise RuntimeError(f'Keys {key} and {node.key} do not compare')

    def find(self, key):
        return self.__find(self.root, key)

    def __depth(self, node):
        if node is None:
            return 0
        else:
            return max(self.__depth(node.left), self.__depth(node.right)) + 1

    def depth(self):
        return self.__depth(self.root)

    def __rotateRight(self, node):
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node
        return newRoot
        
    def __rotateLeft(self, node):
        newRoot = node.right
        node.right = newRoot.left
        newRoot.left = node
        return newRoot

    def show(self, node):
        print(node.key,node.priority, node.left, node.right)
        if node.left:
            self.show(node.left)
        if node.right:
            self.show(node.right)

class DynamicTreap:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def __insert(self, node, key, value):
        if node is None:
            self.size += 1 # key not yet in tree, hence size is increased
            return Node(key, value, 1) #yay, hier ist ne 1 neu
        elif key < node.key:
            node.left = self.__insert(node.left, key, value)
            if node.left.priority > node.priority:
                node=self.__rotateRight(node)
            return node
        elif key > node.key:
            node.right = self.__insert(node.right, key, value)
            if node.right.priority > node.priority:
                node=self.__rotateLeft(node)
            return node
        elif key == node.key:
            node.value = value
            node.priority+=1
            return node
        else:
            raise RuntimeError(f'Keys {key} and {node.key} do not compare')

    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value)

    def __remove(self, node, key):
        if node is None:
            raise KeyError(f'Key {key} not in tree')
        elif key < node.key:
            # the Node to remove is in the left subtree
            node.left = self.__remove(node.left, key)
            return node
        elif key > node.key:
            # the Node to remove is in the right subtree
            node.right = self.__remove(node.right, key)
            return node
        elif key == node.key:
            # node must be removed
            if node.left is None and node.right is None:
                # node is replaced by None
                return None
            elif node.left is None:
                # node is replaced by node.right
                return node.right
            elif node.right is None:
                # node is replaced by node.left
                return node.left
            else:
                # pred is the Node below node with the next smaller key, i.e.
                # n.key < pred.key < node.key for all n in the subtree with
                # root node.left
                pred = node.left
                while pred.right is not None:
                    pred = pred.right
                # remove pred from left subtree as it will replace node
                left = self.__remove(node.left, pred.key)
                pred.left = left
                pred.right = node.right
                return pred
        else:
            raise RuntimeError(f'Keys {key} and {node.key} do not compare')

    def remove(self, key):
        self.root = self.__remove(self.root, key)
        self.size -= 1

    def __find(self, node, key):
        if node is None:
            return None
        elif key < node.key:
            return self.__find(node.left, key)
        elif key > node.key:
            return self.__find(node.right, key)
        elif key == node.key:
            return node
        else:
            raise RuntimeError(f'Keys {key} and {node.key} do not compare')

    def find(self, key):
        return self.__find(self.root, key)

    def __depth(self, node):
        if node is None:
            return 0
        else:
            return max(self.__depth(node.left), self.__depth(node.right)) + 1

    def depth(self):
        return self.__depth(self.root)

    def __rotateRight(self, node):
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node
        return newRoot
        
    def __rotateLeft(self, node):
        newRoot = node.right
        node.right = newRoot.left
        newRoot.left = node
        return newRoot
    
    def show(self, node): #zeigt baum
        print(node.key,node.priority, node.left, node.right)
        if node.left:
            self.show(node.left)
        if node.right:
            self.show(node.right)


def treeEqual(t1, t2):
    """
    Hilfsfunktion für die Unittests
    """
    if t1 is None and t2 is None:
        return True
    elif not t1 is None and not t2 is None:
        return t1.key == t2.key and treeEqual(t1.left, t2.left) and treeEqual(t1.right, t2.right)
    else:
        return False

#nur tests für dynamic, random ist schwierig vorauszuplanen
class TreeTests(unittest.TestCase):

    def __init__(self, *args):
        super().__init__(*args)
        self.keyValue = 7              # Im Test soll key == value/keyValue sein 

    
    def buildTree1(self):
        """Baut einen Testbaum"""
        #Benutze kein treeInsert da wir dies explizit testen wollen
        t = Node(2,2*self.keyValue,3)
        t.left = Node(1,1*self.keyValue,2)
        t.left.left= Node(0,0,1)
        t.right= Node(5,5*self.keyValue,2)
        t.right.left= Node(4,4*self.keyValue,1)
        t.right.left.left=Node(3,3*self.keyValue,1)
        return t
       
    def  buildTree_native(self):
        t = DynamicTreap()
        t.insert(0,0)
        t.insert(4,4*self.keyValue)   # Im Test soll key == value/keyValue sein 
        t.insert(2,2*self.keyValue)
        t.insert(5,5*self.keyValue)
        t.insert(1,1*self.keyValue)
        t.insert(3,3*self.keyValue)
        t.insert(2,2*self.keyValue)
        t.insert(5,5*self.keyValue)
        t.insert(1,1*self.keyValue)
        t.insert(2,2*self.keyValue)
        return t

    def test_insert(self):
        t=self.buildTree_native()
        self.assertEqual(2, t.root.key)
        self.assertEqual(1, t.root.left.key)
        self.assertEqual(0, t.root.left.left.key)
        self.assertEqual(5, t.root.right.key)
        self.assertEqual(4, t.root.right.left.key)
        self.assertEqual(3, t.root.right.left.left.key)
        
        self.assertEqual(None, t.root.left.right)
        self.assertEqual(None, t.root.left.left.right)
        self.assertEqual(None, t.root.left.left.left)
        self.assertEqual(None, t.root.right.right)
        self.assertEqual(None, t.root.right.left.right)
        self.assertEqual(None, t.root.right.left.left.right)
        self.assertEqual(None, t.root.right.left.left.left)

        self.assertTrue(treeEqual(t.root, self.buildTree1()))

    def test_remove1(self):
        t = self.buildTree_native()
        t.remove(5)
        t.remove(4)
        
        self.assertEqual(2, t.root.key)
        self.assertEqual(3, t.root.right.key)
        self.assertEqual(1, t.root.left.key)
        self.assertEqual(0, t.root.left.left.key)
        self.assertRaises(KeyError, t.remove, 10)
        
    def test_find(self):
        t = self.buildTree_native()
        for ii in range(6):
            node = t.find(ii)
            self.assertTrue(isinstance(node, Node),"did not find %u in tree" % ii)
            self.assertEqual(node.key, ii, "tree.find returned wrong node")
        for ii in range(6, 10):
            self.assertIs(t.find(ii), None, "found %u in tree" % ii)
        for ii in range(1, 10):
            self.assertIs(t.find(-ii), None, "found %d in tree" % -ii)

    def test_depth(self):
        t = self.buildTree_native()
        self.assertEqual(4, t.depth())
        self.assertEqual(0, DynamicTreap().depth())



#zum selbst gucken
"""
def  buildTree_native(keyValue):
        t = DynamicTreap()
        t.insert(0,0)
        t.insert(4,4*keyValue)   # Im Test soll key == value/keyValue sein 
        t.insert(2,2*keyValue)
        t.insert(5,5*keyValue)
        t.insert(1,1*keyValue)
        t.insert(3,3*keyValue)
        t.insert(2,2*keyValue)
        t.insert(5,5*keyValue)
        t.insert(1,1*keyValue)
        t.insert(2,2*keyValue)
        return t
t=buildTree_native(7)
t.show(t.root)
t.remove(5)
t.remove(4)
t.show(t.root)
"""

#Aufgabe c) (liest nur ein)
"""
import sys, os #um den richtigen pfad zu bekommen
filename =  os.path.join(sys.path[0], 'die-drei-musketiere.txt')
s = open(filename, encoding="latin-1").read()
for k in ',;.:-"\'!?':
    s = s.replace(k, '') # Sonderzeichen entfernen
s = s.lower() # Alles klein schreiben
text = s.split() # String in Array von Wörtern umwandeln
#Die Wörter in text werden nun in die beiden Treaps eingefügt:
rt = RandomTreap()
dt = DynamicTreap()
for word in text:
    rt.insert(word,0)
    dt.insert(word,0)
"""

#rt und dt anzeigen lassen
"""
rt.show(rt.root)
print("------------------------------------------------")
dt.show(dt.root)
"""

if __name__ == '__main__':
    unittest.main()
