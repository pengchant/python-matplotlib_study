from __future__ import (absolute_import, division, print_function, unicode_literals)

try:
    from urllib2 import urlopen 
except ImportError:
    from urllib.request import urlopen

import json  
import pygal
import math
from itertools import groupby
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
# response = urlopen(json_url)

# req = response.read()
# with open('btc_close_2017_urllib.json', 'wb') as f:
#     f.write(req)
# file_urllib = json.loads(req)

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

# 创建5个列表
dates = []
months = []
weeks = []
weekdays = []
closes = []

for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))
    dates.append(date)
    months.append(month)
    weeks.append(week)
    weekdays.append(weekday)
    closes.append(close)

my_style = LS("#333366", base_style=LCS)

# 生成折线图
line_chart = pygal.Line(style=my_style, x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = "收盘价(￥)"
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in closes]
line_chart.add('收盘价', close_log)
line_chart.render_to_file("收盘价折线图(￥).svg")


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _:_[0]):  
        y_list = [v for i,v in y]
        xy_map.append([str(x), sum(y_list) / len(y_list)]) 
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line(style=my_style)
    line_chart.title = title        
    line_chart.x_labels = x_unique 
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], closes[:idx_month], '收盘价月日均值(￥)', '月日均值')

idx_week = dates.index('2017-12-11') 
line_chart_week = draw_line(weeks[1:idx_week], closes[1:idx_week],"收盘价周日均值(￥)", "周日均值")

idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w)+1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, closes[1:idx_week], "收盘价星期均值(￥)", "星期均值")
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file("收盘价星期均值(￥).svg")

with open('收盘价Dahsboard.html', 'w', encoding='utf-8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title></head><meta charset="utf-8"></head><body><div style="text-align:center;">\n')
    for svg in [
        '收盘价折线图(￥).svg', '收盘价月日均值(￥).svg', '收盘价周日均值(￥).svg', '收盘价星期均值(￥).svg'
    ]:
        html_file.write('<object type="image/svg+xml" data="{0}" width=600 height=650></object>\n'.format(svg))
    html_file.write('</div></body></html>')