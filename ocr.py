from PIL import Image

import pytesseract

print(pytesseract.image_to_string(Image.open('/home/brian/PythonPrograms/Comics/test2.tiff')))