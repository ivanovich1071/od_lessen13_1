# дерево
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self, root_key):
        self.root = Node(root_key)

    def insert(self, key):
        self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)

    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

# тест для дерева с проверкой
import unittest

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        # Установка дерева для тестов
        self.tree = BinaryTree(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(12)
        self.tree.insert(17)

    def test_inorder_traversal(self):
        # Проверка правильности обхода дерева
        expected_result = [3, 5, 7, 10, 12, 15, 17]
        self.assertEqual(self.tree.inorder_traversal(self.tree.root), expected_result)

    def test_insert(self):
        # Проверка вставки нового элемента
        self.tree.insert(6)
        expected_result = [3, 5, 6, 7, 10, 12, 15, 17]
        self.assertEqual(self.tree.inorder_traversal(self.tree.root), expected_result)

if __name__ == '__main__':
    unittest.main()