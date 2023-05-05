from abrir_salvar import abrir, salvar
from contagem import extracao_comp_conexos
from op_morfologicas import grad_externo, inverter_matriz

entrada_imagem = 'imagens/imagens/6.pgm'

img = abrir(entrada_imagem)


masca1 = [[0, 1, 0],
          [1, 1, 1],
          [0, 1, 0]]

objetos = extracao_comp_conexos(img)


img_grand = grad_externo(img, masca1)

img_invertida = inverter_matriz(img_grand)

buracos = extracao_comp_conexos(img_invertida)

print(f'O numero de objetos é {objetos-1}')
print(f'O numero de buracos é {buracos - objetos}')
salvar(img_grand, 'imagens/grand.pgm')
salvar(img_invertida, 'imagens/invertida.pgm')
