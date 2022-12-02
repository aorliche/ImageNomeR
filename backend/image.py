'''View data as images'''

import matplotlib.pyplot as plt
import io
import base64
import numpy as np

def tobase64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return base64.b64encode(buf.read()).decode()

def imshow(fc, colorbar=True):
    fig, ax = plt.subplots()
    im = ax.imshow(fc)
    if colorbar:
        fig.colorbar(mappable=im, ax=ax)
    return tobase64(fig)

def histogram(ys, ylabels, bins=20, density=True):
    fig, ax = plt.subplots()
    for y, lab in zip(ys, ylabels):
        ax.hist(y, label=lab, bins=bins, density=density)
    return tobase64(fig)
    
