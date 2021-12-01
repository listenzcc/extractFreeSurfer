'''
FileName: obj2csv.py
Author: Chuncheng
Version: V0.0
Purpose: Convert OBJ file into CSV format
'''

# %%
import os
import sys
import numpy as np
import pandas as pd
import plotly.express as px

# %%
path = sys.argv[1]
assert os.path.isfile(path), 'File not exists: %s' % path

# %%
content = open(path).read()
lines = content.split('\n')

# %%
vertex = [e[1:].split() for e in lines if e.startswith('v')]
vertex = pd.DataFrame(vertex, columns=['x', 'y', 'z'])

# %%
surface = [e[1:].split() for e in lines if e.startswith('f')]
surface = pd.DataFrame(surface, columns=['a', 'b', 'c'])

# %%
vertex.to_csv(path + '.vertex.csv')
surface.to_csv(path + '.surface.csv')

print(f'CSV files are generated: {path}, .vertex.csv, .surface.csv')
# %%
