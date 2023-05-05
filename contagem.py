# Define uma função para encontrar os buracos em cada objeto
def extracao_comp_conexos(img):
    rotulos = [[0] * len(img[0]) for i in range(len(img))]
    num_rotulos = 0

    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] == 1 and rotulos[i][j] == 0:
                num_rotulos += 1
                pilha = [(i, j)]

                while pilha:
                    x, y = pilha.pop()
                    rotulos[x][y] = num_rotulos

                    if x > 0 and img[x-1][y] == 1 and rotulos[x-1][y] == 0:
                        pilha.append((x-1, y))
                    if x < len(img)-1 and img[x+1][y] == 1 and rotulos[x+1][y] == 0:
                        pilha.append((x+1, y))
                    if y > 0 and img[x][y-1] == 1 and rotulos[x][y-1] == 0:
                        pilha.append((x, y-1))
                    if y < len(img[0])-1 and img[x][y+1] == 1 and rotulos[x][y+1] == 0:
                        pilha.append((x, y+1))

    return num_rotulos
