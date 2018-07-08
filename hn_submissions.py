import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

from operator import itemgetter

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print("Status Code", r.status_code)

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:3]:
    url = ("https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) + ".json")
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'label':response_dict['title'],
        'link':"http://news.ycombinator.com/item?id=" + str(submission_id),
        'value':response_dict.get('descendants', 0)
    }    
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('value'), reverse=True)

for submission_dict in submission_dicts:
    print("\nTile:", submission_dict['label'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['value'])


my_style = LS("#333366", base_style=LCS)
bar_chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
bar_chart.title="top artical"
bar_chart.x_labels = [str(x) for x in range(1, len(submission_dicts) + 1)]
bar_chart.add('',submission_dicts)
bar_chart.render_to_file('hn_topartical.svg')