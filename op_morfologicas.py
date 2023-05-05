def dilatacao(img, mascara):
    """Recebe a matriz de uma imagem, a martiz de uma máscara, faz a operação de dilatação e retorna a matriz"""
    altura, largura = len(img), len(img[0])
    mascara_altura, mascara_largura = len(mascara), len(mascara[0])
    offset_altura, offset_largura = mascara_altura // 2, mascara_largura // 2

    matriz_saida = [[0] * largura for _ in range(altura)]

    for i in range(offset_altura, altura - offset_altura):
        for j in range(offset_largura, largura - offset_largura):
            if img[i][j] == 1:
                matriz_saida[i][j] = 1
                continue
            for k in range(mascara_altura):
                for l in range(mascara_largura):
                    if mascara[k][l] == 1:
                        if img[i - offset_altura + k][j - offset_largura + l] == 1:
                            matriz_saida[i][j] = 1
                            break
    return matriz_saida


def erosao(img, mascara):
    """Recebe a matriz de uma imagem, a martiz de uma máscara, faz a operação de erosão e retorna a matriz"""
    altura, largura = len(img), len(img[0])
    mascara_altura, mascara_largura = len(mascara), len(mascara[0])
    offset_altura, offset_largura = mascara_altura // 2, mascara_largura // 2

    matriz_saida = [[0] * largura for _ in range(altura)]

    for i in range(offset_altura, altura - offset_altura):
        for j in range(offset_largura, largura - offset_largura):
            erodido = True
            for k in range(mascara_altura):
                for l in range(mascara_largura):
                    if mascara[k][l] == 1:
                        if img[i - offset_altura + k][j - offset_largura + l] == 0:
                            erodido = False
                            break
                if not erodido:
                    break
            matriz_saida[i][j] = int(erodido)

    return matriz_saida


def subtracao(m1, m2):
    """"Subtrai duas matrizes, retorna o resultado"""
    row = column = 0
    max_i, max_j = min(len(m1), len(m2))-1, min(len(m1[0]), len(m2[0]))-1
    while True:
        m1[row][column] = max(0, m1[row][column] - m2[row][column])
        if column == max_j:
            # Pula para a proxima linha ou encerra
            column = 0
            row += 1
            if row > max_i:
                break
        else:
            # Continua na mesma coluna
            column += 1
    return m1


def fechamento(img, masc):
    return erosao(dilatacao(img, masc), masc)


def abertura(img, masc):
    return dilatacao(erosao(img, masc), masc)


def grad_externo(img, masc):
    """"Retorna o gradiente externo da imagem pela mascara"""
    return subtracao(dilatacao(img, masc), img)


def intersecao(img1, img2):
    # Obtém as dimensões das imagens
    linhas = len(img1)
    colunas = len(img1[0])

    # Cria uma nova imagem para armazenar o resultado
    img_resultado = [[0 for j in range(colunas)] for i in range(linhas)]

    # Percorre os pixels das imagens e faz a interseção
    for i in range(linhas):
        for j in range(colunas):
            if img1[i][j] == 1 and img2[i][j] == 1:
                img_resultado[i][j] = 1

    return img_resultado


def complemento(img):
    # cria uma cópia da imagem com o mesmo tamanho
    img_complementar = [[0]*len(img[0]) for _ in range(len(img))]

    # inverte o valor de cada pixel
    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] == 0:
                img_complementar[i][j] = 1

    return img_complementar


def inverter_matriz(matriz):
    """
    Inverte 0 e 1 em uma matriz.
    """
    nova_matriz = []
    for linha in matriz:
        nova_linha = []
        for elemento in linha:
            novo_elemento = 1 - elemento
            nova_linha.append(novo_elemento)
        nova_matriz.append(nova_linha)
    return nova_matriz
