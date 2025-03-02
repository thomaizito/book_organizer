from openpyxl import load_workbook
from datetime import date

class Horario:
    def __init__(self):
        self.seg = []
        self.ter = []
        self.qua = []
        self.qui = []
        self.sex = []
        self.cur = None
        self.arq = load_workbook('Horario.xlsx')
        self.week_day = date.today()
        self.us = None
        self.extension_day = ''

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
            

    def apd(self):
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
    
    def week_day_extension(self) -> str:
        day = self.week_day.isoweekday()
        extension_day = ''
        if not isinstance(day, int):
            raise ValueError('O valor deve ser INT!')

        match day:
            case 1:
                self.extension_day += "segunda"
                self.us = self.seg

            case 2:
                self.extension_day += 'terça'
                self.us = self.ter

            case 3:
                self.extension_day += 'quarta'
                self.us = self.qua

            case 4:
                self.extension_day += 'quinta'
                self.us = self.qui

            case 5:
                self.extension_day += 'sexta'
                self.us = self.sex

            case 6:
                self.extension_day += 'sábado'
                self.us = 'None2'

            case 7:
                self.extension_day += 'domingo'
                self.us = 'Nonse'

            case _:
                self.extension_day = None
        

    
dia = Horario()
dia.apd()
dia.week_day_extension()
print(dia.us, dia.extension_day)
