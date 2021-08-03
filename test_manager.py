import unittest
from unittest.mock import patch
import manager


class TestManager(unittest.TestCase):

    def setUp(self):
        self.repl = manager.Manager()
    
    def test_query_api(self):
        pass
        # response = self.repl.query_api()
        # self.assertIsNotNone(response)

    
if __name__ == '__main__':
    unittest.main()
