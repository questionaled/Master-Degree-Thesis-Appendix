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

    type_name, data, time_range = read_data('data.xlsx')
    
    print(type_name)
    # print(data)
    
    maxv, minv = -1, 10

    for line in data:
        maxv = max(maxv, max(line[2]))
        minv = min(minv, min(line[2]))

    for i in range(0, time_range):
        # 构建图
        G = nx.Graph()
        nodes = ["甲", "乙", "丙", "丁", "戊", "己", "庚"]
        edges_forward = []
        edges_flip = []

        w_forward = []
        w_flip = []
        
        for line in data:
            st, ed = line[0], line[1]
            if is_edge_forward(st, ed):
                edges_forward.append((st, ed))
                w_forward.append(line[2][i])
            else:
                edges_flip.append((ed, st))
                w_flip.append(line[2][i])


        G.add_nodes_from(nodes)

        # print(w_forward)

        # 画正向图
        G.add_edges_from(edges_forward)
        # # 绘制图
        pos = nx.circular_layout(G)
        nx.draw_networkx_nodes(G, pos, node_color="black", node_size=500)
        nx.draw_networkx_labels(G, pos, font_color="white", font_family="SimHei", labels={node: node for node in nodes})
        
        # 根据边权重映射颜色
        edge_colors = [plt.get_cmap('Reds')((w - minv) / (maxv - minv)) for w in w_forward]
        # 绘制边，按照权重颜色渐变
        drawe_dges = nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=5)

        plt.savefig(type_name + "_正向_" + str(i) + '.png', bbox_inches='tight')

        # 画反向图
        G.add_edges_from(edges_flip)
        # # 绘制图
        pos = nx.circular_layout(G)
        nx.draw_networkx_nodes(G, pos, node_color="black", node_size=500)
        nx.draw_networkx_labels(G, pos, font_color="white", font_family="SimHei", labels={node: node for node in nodes})
        
        # 根据边权重映射颜色
        edge_colors = [plt.get_cmap('Reds')((w - min(w_flip)) / (max(w_flip) - min(w_flip))) for w in w_flip]
        # 绘制边，按照权重颜色渐变
        drawe_dges = nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=5)

        # # 标记特殊字符
        # special_node = 'F'
        # nx.draw_networkx_edges(G, pos, edgelist=[('F', 'G')], style='dashed', width=2)
        # plt.text(pos[special_node][0]+0.08, pos[special_node][1], special_node, fontsize=20, color='blue')
        
        plt.savefig(type_name + "_反向_" + str(i) + '.png', bbox_inches='tight')


    # # 构建图
    # G = nx.Graph()
    # nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    # edges = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G')]
    # weights = {'A': 3, 'B': 4, 'C': 2, 'D': 5, 'E': 1, 'F': 0, 'G': 0}
    # G.add_nodes_from(nodes)
    # G.add_edges_from(edges)

    # # 绘制图
    # pos = nx.circular_layout(G)
    # node_colors = [weights[node] for node in G.nodes]
    # nx.draw_networkx_nodes(G, pos, node_color=node_colors, cmap=cm.get_cmap('Reds'), vmin=min(weights.values()), vmax=max(weights.values()), node_size=1000)
    # nx.draw_networkx_labels(G, pos, labels={node: node for node in nodes})
    # edge_colors = [weights[edge[0]] for edge in G.edges]
    # nx.draw_networkx_edges(G, pos, edge_color=edge_colors, edge_cmap=cm.get_cmap('Reds'), edge_vmin=min(weights.values()), edge_vmax=max(weights.values()), width=2)

    # # 标记特殊字符
    # special_node = 'F'
    # nx.draw_networkx_edges(G, pos, edgelist=[('F', 'G')], style='dashed', width=2)
    # plt.text(pos[special_node][0]+0.08, pos[special_node][1], special_node, fontsize=20, color='blue')

    # plt.axis('off')
    # plt.show()
