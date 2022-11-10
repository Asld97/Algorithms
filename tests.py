import unittest
from binary_search import binary_search

class TestAlgorithms(unittest.TestCase):
    
    def test_binary_Search(self):        
        self.assertEqual(binary_search([1,2,3,4,5,6,7,8], 5), 5, 4)


if __name__ == "__main__":
    unittest.main()
    
