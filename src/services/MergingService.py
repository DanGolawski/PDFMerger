from PyPDF2 import PdfFileReader, PdfFileWriter


class MergingService:

    @staticmethod
    def merge_service(new_file_name, input_path):
        pdf_writer = PdfFileWriter()

        for path in input_path:
            pdf_reader = PdfFileReader("C:/Users/User/Desktop/" + path + ".pdf")
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

        with open("C:/Users/User/Desktop/" + new_file_name + ".pdf", 'wb') as new_file:
            pdf_writer.write(new_file)

        print("Merged")
