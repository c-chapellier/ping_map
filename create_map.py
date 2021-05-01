import sys
import pygal
import pandas as pd

if len(sys.argv) != 2:
    print('usage: python3 create_map.py data_file.csv')
    exit(1)

df = pd.read_csv(sys.argv[1])

s = set(df['country'])

d = {}
for c in s:
    sum = 0
    n = 0
    for i in df.index:
        if df['country'][i] == c:
            sum += float(df['time'][i])
            n += 1
    if n != 0: # sometimes a nan appears in set, short patch
        d[c.lower()] = sum / n

worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Ping'
worldmap_chart.add('ping', d)

# worldmap_chart.render()
# worldmap_chart.render_to_file('line_chart.svg')
worldmap_chart.render_in_browser()