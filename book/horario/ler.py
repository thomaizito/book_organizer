from openpyxl import load_workbook
from datetime import date

class Horario:
    # self.seg -- self.sex == Matérias dos dias da semana
    # self.cur == Matéria do dia que foi executado
    # self.arq == Arquivo excell
    # self.week_day == Objeto date
    # self.today = 
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

    # Adicionar qual a turma que o programa vai pegar no arquivo
    def esc(self, turma):
        if turma == 'A':
            self.cur = self.arq['A']

        elif turma == 'B':
            self.cur = self.arq['B']

        else:
            raise ValueError("SEM turma")
    
    #Match case interno para adicionar os valores em seus respectivos lugares
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
    def Materias_Horario(self):
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
    
    # Funcão interna para caso tenha um dia específico selecionado
    @staticmethod
    def Dia_Específico(day:int, dia_especifico:str):
        match dia_especifico.lower():
                case 'segunda':
                    day = 1
                case 'terça':
                    day = 2
                case 'quarta':
                    day = 3
                case 'quinta':
                    day = 4
                case 'sexta':
                    day = 5
                case _:
                    return None
        return day


    # Adicionar o dia de hoje por extenso e pegar o horário do dia
    def Dia_Horario(self, dia_especifico=None) -> str: 
        self.Materias_Horario()

        flag = self.week_day.isoweekday() + 1
        day = 1 if flag > 7 else day = flag

        if dia_especifico:
            day = self.Dia_Específico(day, dia_especifico)

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
                self.extenso = None
        return self.today
        