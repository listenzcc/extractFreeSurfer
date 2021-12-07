'''
FileName: mkSubjectCSV.py
Author: Chuncheng
Version: V0.0
Purpose: Make csv for the subject
'''

# %%
import os
import numpy as np
import pandas as pd
from tqdm.auto import tqdm

# %%
pwd = os.path.dirname(__file__)

# %%
# ! Make sure the ./src/[subject] and ./csv/[subject] folders are ready
subject = 'fsaverage'
hemi = 'lh'

# %%
containFiles = dict(
    pial=('surfer', 'Origin Cortex'),
    inflated=('surfer', 'Inflated Cortex'),
    sphere=('surfer', 'Sphere Cortex'),
    curv=('scalar', 'Curv values'),
    sulc=('scalar', 'Sulc values'),
    thickness=('scalar', 'Thickness values')
)

file_table = pd.DataFrame(containFiles).transpose()
file_table.columns = [['type', 'desc']]
file_table['name'] = file_table.index


def fullPath(name):
    return '{}.{}.asc'.format(os.path.join(pwd, 'src', subject, hemi), name)


def fileLength(name):
    return len(open(fullPath(name), 'r').read())


def readSurf(name):
    content = open(fullPath(name), 'r').read()
    lines = content.split('\n')

    num_positions = int(lines[1].split()[0])
    num_cells = int(lines[1].split()[1])

    print('File {} has {} positions and {} cells'.format(
        name, num_positions, num_cells))

    positions = np.array([e.split()
                         for e in lines[2:2+num_positions]])
    cells = np.array([e.split()
                     for e in lines[2+num_positions:2+num_positions+num_cells]])

    print('Read {} positions and {} cells'.format(positions.shape, cells.shape))
    return positions, cells


def readScalar(name):
    content = open(fullPath(name), 'r').read()
    lines = content.split('\n')

    num_lines = len(lines)

    print('File {} has {} lines'.format(name, num_lines))

    values = np.array([e.split() for e in lines if e])

    print('Read {} values'.format(values.shape))
    return values


file_table['file'] = file_table['name'].applymap(fullPath)

file_table['length'] = file_table['name'].applymap(fileLength)

print(file_table)

# %%
for i in tqdm(range(len(file_table))):
    se = file_table.iloc[i]
    name = se['name']

    print(f'\nWorking with {name}')

    if se['type'] == 'surfer':
        positions, cells = readSurf(name)
        pd.DataFrame(positions).to_csv(os.path.join(
            pwd, 'csv', subject, f'{hemi}-{name}.positions.csv'))
        pd.DataFrame(cells).to_csv(os.path.join(
            pwd, 'csv', subject, f'{hemi}-{name}.cells.csv'))

    if se['type'] == 'scalar':
        values = readScalar(name)
        pd.DataFrame(values[:, -1]).to_csv(os.path.join(
            pwd, 'csv', subject, f'{hemi}-{name}.values.csv'))


print('Done.')

# %%
