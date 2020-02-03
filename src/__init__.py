from services.MetadataExtractor import MetadataExtractor
from services.TextExtractor import TextExtractor
from services.MergingService import MergingService

# METADATA EXTRACTION
# MetadataExtractor.extract_metadata("resource/reportlab-sample.pdf")
# MetadataExtractor.extract_metadata("resource/CV_DanGolawski.pdf")
# MetadataExtractor.extract_metadata("resource/NSK - cwiczenia nr 1.pdf")

# TEXT EXTRACTION
# TextExtractor.extract_text("resource/NSK - cwiczenia nr 1.pdf")

# DOCUMENTS MERGING
print("Wprowadz nazwe pierwszego pliku :")
first_file = input()
print("Wprowadz nazwe drugiego pliku :")
second_file = input()
MergingService.merge_service("mergedFile", [first_file, second_file])