'''Read data from files on server'''

import numpy as np

def vec2mat(fc):
    n = len(fc)
    d = int(round((1+(1+8*n)**0.5)/2))
    a,b = np.triu_indices(d,1)
    mat = np.zeros((d,d))
    mat[a,b] = fc
    mat += mat.T
    ones = np.arange(d)
    mat[ones,ones] = 1
    return mat

def getfc(user, cohort, sub, task=None, ses=None):
    task = f'_task-{task}' if task is not None else ''
    ses = f'_ses-{ses}' if ses is not None else ''
    fname = f'data/{user}/cohorts/{cohort}/fc/{sub}{task}{ses}_fc.npy'
    return np.load(fname)