import pandas as pd
path_a = r'c:\Users\Nahuel\Desktop\Facultad\VS Code\TP-Proyectos--Python-\2021 - TP2 - Ingresos.xlsx'
path_b = r'c:\Users\Nahuel\Desktop\Facultad\VS Code\TP-Proyectos--Python-\2021 - TP2 - Ingresos modificado.xlsx'
for s in ['cloaca','ptar']:
    print('\nSHEET', s)
    a = pd.read_excel(path_a, sheet_name=s, header=None)
    b = pd.read_excel(path_b, sheet_name=s, header=None)
    print('A head:')
    print(a.head(5).to_string(index=False, header=False))
    print('B head:')
    print(b.head(5).to_string(index=False, header=False))
    for skip in [1,2]:
        aa = a.iloc[skip:].fillna('<<NA>>').astype(str).reset_index(drop=True)
        bb = b.iloc[skip:].fillna('<<NA>>').astype(str).reset_index(drop=True)
        same = aa.equals(bb)
        diff = (aa != bb).any(axis=1)
        print(' compare after skip', skip, 'same=', same, 'diff rows count=', diff.sum())
        if not same:
            for i in diff[diff].index[:5]:
                print('   row', i, 'A=', aa.iloc[i].tolist()[:5], 'B=', bb.iloc[i].tolist()[:5])
