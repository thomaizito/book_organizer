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
        self.arq = load_workbook(r'book/horario/Horario.xlsx')
        self.week_day = date.today()
        self.today = None
        self.extenso = ''

    def esc(self, turma):
        if turma == 'A':
            self.cur = self.arq['A']

        elif turma == 'B':
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
            
    # Pegar os itens do arquivo Horario
    def apd(self):

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
    
    # Adicionar o dia de hoje por extenso e pegar o horário do dia
    def today_day(self) -> str:
        self.apd()

        day = self.week_day.isoweekday() + 2

        if not isinstance(day, int):
            raise ValueError('O valor deve ser INT!')

        match day:
            case 1:
                self.extenso += "segunda"
                self.today = self.seg

            case 2:
                self.extenso += 'terça'
                self.today = self.ter

            case 3:
                self.extenso += 'quarta'
                self.today = self.qua

            case 4:
                self.extenso += 'quinta'
                self.today = self.qui

            case 5:
                self.extenso += 'sexta'
                self.today = self.sex

            case 6:
                self.extenso += 'sábado'
                self.today = None

            case 7:
                self.extenso += 'domingo'
                self.today = None

            case _:
                self.extenso = False
        