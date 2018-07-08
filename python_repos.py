import requests   
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS   

# 1.采集数据
URL="https://api.github.com/search/repositories?q=language:python&sort=starts"
r = requests.get(URL)
print("status code:", r.status_code)
response_dir = r.json()
print("total repositories:", response_dir['total_count'])

# 2.获取项目的数据仓库
repo_dicts = response_dir['items']

# 3.获取项目名称和star的数量
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name']) 
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':repo_dict['description'],
        'xlink':repo_dict['html_url'],
    } 
    plot_dicts.append(plot_dict)

# 4.Pygal可视化
my_config = pygal.Config() # 获取配置变量
my_config.x_label_rotation = 45 # 旋转x轴文字
my_config.show_legend=False # 是否显示图例
my_config.title_font_size=24 # 标题文字大小
my_config.label_font_size=14 # 轴线上文字大小
my_config.major_label_font_size=18 # 主刻度文字大小
my_config.truncate_label=15 # 截取字符串
my_config.show_y_guides=True # 是否显示y辅助线
my_config.width=1000 # 宽度

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(my_config, style=my_style)
chart.title="Most-started python projects on github"
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file("python_repos.svg")