import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import pandas as pd

import time


def read_data(path):
    df = pd.read_excel(path)

    res = []

    # 遍历每行数据并打印
    for index, row in df.iterrows():
        type_name, st, ed = row[0], row[1], row[2]
        cur_weights = []
        for i in range(3, 23):
            cur_weights.append(row[i])

        line = [st, ed, cur_weights]
        res.append(line)

    time_range = len(res[0][2])

    return type_name, res, time_range


def is_edge_forward(a, b):
    if (a == "甲" and b == "乙") or (a == "乙" and b == "丙") or (a == "丙" and b == "丁") or (a == "丙" and b == "戊") or (a == "戊" and b == "己") \
            or (a == "乙" and b == "庚"):
        return True
    else:
        return False


if __name__ == "__main__":

    type_name, data, time_range = read_data('raw_data.xlsx')

    print(type_name)
    # print(data)
    # input()

    maxv, minv = -1, 10

    for line in data:
        maxv = max(maxv, max(line[2]))
        minv = min(minv, min(line[2]))

    for i in range(0, time_range):
        # 构建图
        G = nx.Graph()
        nodes = ["甲", "丁", "己", "庚", "戊", "丙", "乙"]
        special_nodes = ["甲", "丁", "己", "庚"]
        edges = [("甲", "乙"), ("乙", "丙"), ("乙", "庚"), ("丙", "丁"), ("丙", "戊"), ("戊", "己")]
        node_weights = []
        
        for line in data:
            # print(line)
            node_weights.append(line[2][i])
            # input()
            
        # print(node_weights)

        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        # # 绘制图
        pos = nx.spring_layout(G, seed=40)
        
        node_colors = []
        for j in range(0, 4):
            color = plt.get_cmap('Reds')((node_weights[j] - minv) / (maxv - minv))
            node_colors.append(color)
        for t in range(4, 7):
            node_colors.append("white")

        # 画点
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1000)
        nx.draw_networkx_labels(G, pos, font_color="black", font_family="SimHei", labels={node: node for node in nodes})
        
        drawe_dges = nx.draw_networkx_edges(G, pos, edge_color="black", width=5)

        plt.savefig(type_name + "_发出_" + str(i) + '.png', bbox_inches='tight')
        plt.clf()

        # 画反向图
        pos = nx.spring_layout(G, seed=40)
        
        node_colors = []
        for j in range(4, 8):
            color = plt.get_cmap('Reds')((node_weights[j] - minv) / (maxv - minv))
            node_colors.append(color)
        for t in range(4, 7):
            node_colors.append("white")

        # 画点
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1000)
        nx.draw_networkx_labels(G, pos, font_color="black", font_family="SimHei", labels={node: node for node in nodes})
        
        drawe_dges = nx.draw_networkx_edges(G, pos, edge_color="black", width=5)

        plt.savefig(type_name + "_接收_" + str(i) + '.png', bbox_inches='tight')
        plt.clf()

