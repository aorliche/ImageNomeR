
import numpy as np

def correlate_feat(feats, var):
    if isinstance(feats, list):
        feats = torch.stack(feats)
    mu = torch.mean(feats, dim=0, keepdims=True)
    feats -= mu
    var -= torch.mean(var)
    sigma_fv = torch.einsum('ab,a->b',feats,var)
    sigma_ff = torch.einsum('ab,ab->b',feats,feats)
    sigma_vv = torch.einsum('a,a->',var,var)
    rho = sigma_fv/(sigma_ff*sigma_vv)**0.5
    return rho.numpy()

def correlate_var(var1, var2):
    return np.corrcoef(var1, var2)[0,1]