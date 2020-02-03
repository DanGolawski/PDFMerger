from PyPDF2 import PdfFileReader


class MetadataExtractor:

    @staticmethod
    def extract_metadata(path):
        with open(path, 'rb') as file:
            pdf = PdfFileReader(file)
            info = pdf.getDocumentInfo()
            # number_of_pages = pdf.getNumberPages()

        print(info)

        print("Author : " + str(info.author))
        print("Creator : " + str(info.creator))
        print("Producer : " + str(info.producer))
        print("Subject : " + str(info.subject))
        print("Title : " + str(info.title) + '\n')
