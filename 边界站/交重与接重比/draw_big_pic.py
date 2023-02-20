import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 创建一个 5x4 的图像网格
fig, ax = plt.subplots(5, 4, figsize=(16, 20))

# 加载图片并将其放置在相应的网格位置中
for i in range(20):
    row = i // 4
    col = i % 4
    path = "交重与接重比例_" + str(i) + ".png"
    img = mpimg.imread(path)
    ax[row][col].imshow(img)
    ax[row][col].axis('off')

    # 显示时刻
    ax[row][col].set_title("t " + str(i + 1))

# 添加 colorbar
cax = fig.add_axes([0.95, 0.1, 0.02, 0.8])
plt.colorbar(plt.cm.ScalarMappable(cmap=plt.get_cmap('Reds')), cax=cax)

# 保存合并后的图像
# fig.suptitle('正点率趋势图', fontproperties="SimHei", fontsize=32)
plt.savefig('merged_pic.png', bbox_inches='tight')