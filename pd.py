import pandas as pd

data = pd.read_excel('2021_1.xls',)
for m in data.loc:
    for n in data.loc:
        if m['s_name'] == n['s_name'] and abs(m['e_ranking'] - n['e_ranking']) >= 8000:
            print(m, '\n', n)
