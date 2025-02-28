from openpyxl import load_workbook

arq = load_workbook('HorarioB.xlsx')
cur = arq['Plan1']

ter = []
qua = []
qui = []
seg = []
sex = []

for i in range(5):
    cont=0
    day = None
    for j in cur.rows:
        if cont <= 0:
            cont += 1
            continue
        if not j[i].value:
            continue
        
        
        
        match day:
            case 'SEG':
                if not day:
                    day = 'SEG'
                    continue
                seg.append(j[i].value)

            case 'TER':
                if not day:
                    day = 'TER'
                ter.append(j[i].value)

            case 'QUA':
                if not day:
                    day = 'QUA'
                qua.append(j[i].value)

            case 'QUI':
                if not day:
                    day = 'QUI'
                qui.append(j[i].value)

            case 'SEX':
                if not day:
                    day = 'SEX'
                sex.append(j[i].value)
            
            case _:
                day = j[i].value
    
    print(seg, ter, qua, qui, sex)