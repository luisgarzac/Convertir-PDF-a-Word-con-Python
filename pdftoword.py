# Convertiremos un archivo word a PDF
# Importaremos Convert de la librería pdf2docx
from pdf2docx import Converter

pdf_file = 'archivo1.pdf' # Asignamos el nombre del archivo PDF a la variable pdf_file
docx_file = 'archivo1_pdf2word.docx' # Asignamos el nombre del archivo word a la variable docx_file

# usamos Converter para convertir el archivo PDF a docx
cv = Converter(pdf_file)
cv.convert(docx_file) # Todas las páginas por default
cv.close()


