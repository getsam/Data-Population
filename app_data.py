import matplotlib.pyplot as plt

dados = open("DATA/populacao-brasileira.csv").readlines()

eixo_x = []
eixo_y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        eixo_x.append(int(linha[0]))
        eixo_y.append(int(linha[1]))

plt.plot(eixo_x,eixo_y)
plt.bar(eixo_x,eixo_y)

plt.show()
