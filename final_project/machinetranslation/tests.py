import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertRaises(ValueError, english_to_french, None) \
            # test when null input
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  \
            # test when hello is given as input and the output is bonjour
        
class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertRaises(ValueError, french_to_english, None) \
            # test when null input
        self.assertEqual(french_to_english('Bonjour'), 'Hello') \
            # test when bonjour is given as input and the output is hello

unittest.main()