import unittest
from unittest.mock import patch
import translator


class TestManager(unittest.TestCase):

    def setUp(self):
        self.tl = translator.Translator()

    def test_print_ticket(self):
        pass

    
if __name__ == '__main__':
    unittest.main()