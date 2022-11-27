
from pathlib import Path

def ls_cohorts(user):
    return [f.name for f in Path(f'data/{user}/cohorts').iterdir() if f.is_dir()]

def get_cohort(user, cohort):
    p = Path(f'data/{user}/cohorts/{cohort}')
    data = {}
    if (p/'fc').is_dir():
        data['fc'] = [f.name for f in Path(p/'fc').iterdir() if not f.is_dir()]
    return data
    
