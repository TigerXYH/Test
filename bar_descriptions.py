import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python projects'
chart.x_labels = ['X', 'Y', 'H']

plot_dicts = [
    {'value': 16101, 'label': 'P_X'},
    {'value': 15028, 'label': 'P_Y'},
    {'value': 14789, 'label': 'P_H'}
]

chart.add('', plot_dicts)
chart.render_to_file('ls/bar_descriptions.svg')