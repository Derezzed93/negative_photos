' Carlos Gomes - 05-12-2019 '
" codigo de conversao de imagens para cores negativas em faixas "
import easygui
from PIL import Image

arquivo = easygui.fileopenbox()
im = Image.open(arquivo)
im = im.copy()
pixel = im.load()
largura = im.width
altura = im.height
fator = 255
for linha in range(altura):
    for coluna in range(largura):
        if((coluna <= largura//4) or (coluna >= largura//2 and coluna <= 3*largura//4)):
            r,g,b = pixel[coluna,linha]
            r = fator - r
            g = fator - g
            b = fator - b
            pixel[coluna,linha] = r,g,b

im.save(arquivo[:-4] + "_negative_modified.jpg")
im.show()
            