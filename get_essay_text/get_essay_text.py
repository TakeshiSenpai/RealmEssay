from pypdf import PdfReader

def getFileFormat(file):
    return file.split('.')[-1]

def getPDFText(file):
    pdf = PdfReader(file)
    text = ''
    for page in pdf.pages:
        pageText = ' '.join(page.extract_text().splitlines())
        text += pageText + ' '
    return text

def getTXTText(file):
    with open(file, 'r') as f:
        return f.read()