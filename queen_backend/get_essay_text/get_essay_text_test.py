import unittest
import os

from get_essay_text import getFileFormat, getPDFText, getTXTText

class GetEssayTextTest(unittest.TestCase):
    def testPDFFile(self):
        print("\n\n\n")
        file = os.path.join(os.path.dirname(__file__), 'Propuesta de arquitectura.pdf')
        self.assertEqual(getFileFormat(file).lower(), 'pdf')
        text = getPDFText(file)
        print(text)
        self.assertGreater(len(text), 0)

    def testTXTFile(self):
        print("\n\n\n")
        file = os.path.join(os.path.dirname(__file__), 'Propuesta de arquitectura.txt')
        self.assertEqual(getFileFormat(file).lower(), 'txt')
        text = getTXTText(file)
        print(text)
        self.assertGreater(len(text), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)