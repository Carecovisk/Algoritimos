import matplotlib.pyplot as plt
import numpy as np, json

with open('./resultados/mergeSort_tempos.json') as json_file:
    saida_json: dict = json.load(json_file)

x = np.arange(1) * 8 # Posições das barras
width = 1.0


for algoritimo, resultados in saida_json.items():
    fig, ax = plt.subplots(layout='constrained')
    resultados = np.transpose([x for x in resultados.values()])
    multiplier = 0
    for i in range(3):
        label = resultados[1][i][0]
        tempos = resultados[2][i].astype(np.float32) * 1000 # Tempo em milisegundos
        tempos = list(map(lambda i: round(i, 2), tempos))
        offset = width * multiplier
        rects = ax.bar(x + offset, tempos, width, label=label)

        ax.bar_label(rects, padding=3)
        multiplier += 1.25
    
    tick = resultados[0][i][0]
    ax.set_ylabel('Tempo em milisegundos')
    ax.set_xlabel('Tamanho do input')
    ax.set_title(f"Tempo de execução {algoritimo}")
    ax.set_xticks(x + width * 1.25, [tick])
    ax.legend(loc='upper left', ncols=3)
    plt.show()
    # plt.savefig(f"./results/{algoritimo}")