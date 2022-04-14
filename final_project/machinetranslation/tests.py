import unittest
from translator import french_to_english, english_to_french
 
class TestTranslator_f2e(unittest.TestCase):
    def test_french_to_english(self):
        self.assertNotEqual(french_to_english("None"), '')
        self.assertNotEqual(french_to_english(0), 0)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
 
 
class TestTranslator_e2f(unittest.TestCase):
    def test_english_to_french(self):
        self.assertNotEqual(english_to_french("None"), '')
        self.assertNotEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
 
 
unittest.main()
