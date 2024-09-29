import unittest
import os
import requests

from get_essay_text import getFileFormat, getPDFText, getTXTText

def downloadFile(url, filename):
    print(f"Attempting to download file from: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully: {filename}")
    except requests.exceptions.Timeout:
        raise Exception(f'Timeout occurred while downloading file: {url}')
    except requests.exceptions.RequestException as e:
        raise Exception(f'Error downloading file: {e}')

class GetOnlineEssayTextTest(unittest.TestCase):
    def testPDFFile(self):
        print("\n\n\n")
        url = 'https://css4.pub/2015/icelandic/dictionary.pdf'
        filename= os.path.join(os.path.dirname(__file__), 'test.pdf')
        
        downloadFile(url=url, filename=filename)

        # Probar formato PDF
        self.assertEqual(getFileFormat(filename).lower(), 'pdf')

        # Obtener texto del PDF
        text = getPDFText(filename)
        print(text)
        self.assertGreater(len(text), 0)

        os.remove(filename)

    def testTXTFile(self):
        print("\n\n\n")
        url = 'https://filesamples.com/samples/document/txt/sample3.txt'
        filename= os.path.join(os.path.dirname(__file__), 'test.txt')
        
        downloadFile(url=url, filename=filename)

        # Probar formato TXT
        self.assertEqual(getFileFormat(filename).lower(), 'txt')

        # Obtener texto del TXT
        text = getTXTText(filename)
        print(text)
        self.assertGreater(len(text), 0)

        os.remove(filename)

if __name__ == '__main__':
    unittest.main(verbosity=2)