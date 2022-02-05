import sys
sys.path.append("..")
import unittest

from translator.py import french_to_english, english_to_french

class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('pomme'), 'Apple')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')


class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('man'), 'Homme')
        self.assertEqual(english_to_french('woman'), 'Femme')
        self.assertNotEqual(english_to_french('man'), 'Man')

unittest.main()