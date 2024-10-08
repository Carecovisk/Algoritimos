import matplotlib.pyplot as plt
import json, pandas as pd, numpy as np

with open('comparacoes_trocas.json') as json_file:
    comparacoes_trocas: dict = json.load(json_file)

sizes = [1_000, 10_000, 50_000, 100_000]
x = np.arange(len(sizes)) * 8 # Posições das barras
width = 1.0



for algoritimo, resultados in comparacoes_trocas.items():

    fig,ax = plt.subplots(layout='constrained')
    multiplier = 0
    resultados = pd.DataFrame([x for x in resultados.values()]).T
    resultados.columns = resultados.loc[0]
    resultados.drop(0, inplace=True)

    for i in range(1, 4):
        # comparacoes = [r[1] for r in resultados.loc[i]]
        label = resultados.loc[i][0][0]
        offset = multiplier * width
        trocas = [r[2] for r in resultados.loc[i]]

    
        rects = ax.barh(x + offset, trocas, width, label=label)
        ax.bar_label(rects)
        multiplier += 1.25

    ax.set_xlabel('Trocas')
    ax.set_ylabel('Tamanho do input')
    ax.set_title(f"Numero de trocas {algoritimo}")
    ax.set_yticks(x + width * 1.25, [1_000, 10_000, 50_000, 100_000])
    ax.legend(loc='upper left', ncols=3)
    ax.invert_yaxis()
    plt.show()