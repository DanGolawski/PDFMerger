from PyPDF2 import PdfFileReader


class TextExtractor:

    @staticmethod
    def extract_text(path):
        with open(path, 'rb') as file:
            pdf = PdfFileReader(file)
            page = pdf.getPage(4)
            print('Page type: {}'.format(str(type(page))))

            text = page.extractText()
            print(text)