'''View data as images'''

import matplotlib.pyplot as plt
import io
import base64
import numpy as np

def imshow(fc, colorbar=True):
    fig, ax = plt.subplots()
    im = ax.imshow(fc)
    if colorbar:
        fig.colorbar(mappable=im, ax=ax)
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    print('okay')
    buf.seek(0)
    return base64.b64encode(buf.read()).decode()