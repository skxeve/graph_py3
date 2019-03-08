import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# データ
data = [1011, 530, 355, 200, 40, 11]
label = ['hoge', 'fuga', 'piyo', 'pugya', 'dododododododo', 'ga']

# 綺麗に書くためのおまじない
plt.style.use('ggplot')
plt.rcParams.update({'font.size': 15})

# 各種パラメータ
size = (9, 5)  # 凡例を配置する関係でsizeは横長にしておきます。
col = cm.Spectral(
        np.arange(len(data)) / float(len(data))
        )  # color指定はcolormapから好みのものを。

# pie
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html

# create a new figure
plt.figure(figsize=size, dpi=100)
# plot a pie chart
plt.pie(
        data,
        colors=col,
        counterclock=False,
        # if default None, start right to under. 90, start top to right.
        startangle=90,
        # in graph string to show each numeric values.
        autopct=lambda p: '{:.1f}%'.format(p) if p >= 5 else ''
        )
# Tune the subplot layout
plt.subplots_adjust(left=0, right=0.7)
# Place a legend on the axes.
plt.legend(label, fancybox=True, loc='center left', bbox_to_anchor=(0.9, 0.5))
# Convenience method to get or set some axis properties.
plt.axis('equal')
# Save the current figure.
plt.savefig('figure.png', bbox_inches='tight', pad_inches=0.05)
