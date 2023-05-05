def abrir(dir):
  """Abre a imagem pgm, dado o diretório e retorna uma matriz
    OBS: cada valor de píxel na imagem deve estar em uma linha sozinho"""
  try:
    with open(dir, 'r') as arq:
      lines = arq.readlines()
    if not lines[0].startswith('P1'):
      print('Imagem inválida, o tipo da pgm deve ser P1')
      return None
    i = 1
    while lines[i].startswith('#'):
      # Pula comentários
      i += 1
    tamanhos = lines[i].replace(r'\n', '').split()
    tamanho = int(tamanhos[0]), int(tamanhos[1])
    matriz = [[] for j in range(tamanho[0])]
    cont = r = 0
    inicio = i + 1
    # Itera sobre a imagem e armazena os valores em matriz
    for i in range(inicio, (tamanho[0] * tamanho[1]) + inicio):
      matriz[r].append(int(lines[i]))
      cont += 1
      if cont == tamanho[1]:
        r, cont = r + 1, 0
    return matriz

  except Exception as e:
    print('Não foi possível abrir tal imagem, ocorreu o seguinte erro:\n', e)
    return None


def salvar(matriz, dir):
  """"Salva a imagem contida na matriz, dado o diretório"""
  try:
    with open(dir, 'w') as arq:
      # Adição do cabeçalho
      arq.write('P1\n')
      arq.write(f'{len(matriz)} {len(matriz[0])}\n')
      # Adicao de cada item da matriz
      for row in matriz:
        for column in row:
          arq.write(str(column) + '\n')
      return True

  except Exception as e:
    print('Não foi possível salvar a imagem, ocoreu o seguinte erro:\n', e)
    return False
