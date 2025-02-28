from openpyxl import load_workbook

class Horario:
    def __init__(self):
        self.seg = []
        self.ter = []
        self.qua = []
        self.qui = []
        self.sex = []
        self.cur = None
        self.arq = load_workbook('Horario.xlsx')

    def esc(self):
        escolha = int(input("1. A\n 2. B"))
        if escolha == 1:
            self.cur = self.arq['A']

        elif escolha == 2:
            self.cur = self.arq['B']

        else:
            print("Erro! COloque um valor válido")
    

    def dia(self, i, j, day):
        match day:
            case 'SEG':
                if not day:
                    day = 'SEG'
                self.seg.append(j[i].value)

            case 'TER':
                if not day:
                    day = 'TER'
                self.ter.append(j[i].value)

            case 'QUA':
                if not day:
                    day = 'QUA'
                self.qua.append(j[i].value)

            case 'QUI':
                if not day:
                    day = 'QUI'
                self.qui.append(j[i].value)

            case 'SEX':
                if not day:
                    day = 'SEX'
                self.sex.append(j[i].value)
            
            case _:
                day = j[i].value

        return day
            

    def main(self):
        self.esc()

        for i in range(5):
            cont=0
            day = None
            for j in self.cur.rows:
                if cont <= 0:
                    cont += 1
                    continue
                if not j[i].value:
                    continue

                day = self.dia(i, j, day)
        
        print(self.seg, self.ter, self.qua, self.qui, self.sex)
                
        
        
sla = Horario()
sla.main()