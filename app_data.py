import matplotlib.pyplot as plt

dados = open("DATA/populacao-brasileira.csv").readlines()

eixo_x = []
eixo_y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        eixo_x.append(int(linha[0]))
        eixo_y.append(int(linha[1]))

plt.plot(eixo_x,eixo_y, color='k', linestyle='--')
plt.bar(eixo_x,eixo_y, color='#e4e4e4')

plt.title("Crescimento da População Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
#plt.show()
plt.savefig('populacao-brasileira.png', dpi=800)
