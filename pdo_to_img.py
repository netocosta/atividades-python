sudo apt-get install poppler-utils

https://chocolatey.org/install
choco install poppler

pip install pdf2image



from pdf2image import convert_from_path
import os

diretorio = 'C:\\meu_diretorio\\'

for file in dirs:
    print(diretorio+file)
    images = convert_from_path(diretorio+file)

    for image in images:
        image.save(diretorio+"%s-page%d.jpg" %
                   (file, images.index(image)), "JPEG")
