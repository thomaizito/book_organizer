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


    #Match case interno para adicionar os valores em seus respectivos lugares
    def _dia(self, i, j, day):
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

    # Funcão interna para caso tenha um dia específico selecionado
    @staticmethod
    def _Dia_Específico(dia_especifico:str):
        match dia_especifico.lower():
                case 'segunda':
                    flag = 1
                case 'terça':
                    flag = 2
                case 'quarta':
                    flag = 3
                case 'quinta':
                    flag = 4
                case 'sexta':
                    flag = 5
                case _:
                    flag =  None
        return flag

    # Pegar os itens do arquivo Horario
    def _Materias_Horario(self):
        for i in range(5):
            cont=0
            day = None
            for j in self.cur.rows:

                if cont <= 0:
                    cont += 1
                    continue
                
                if not j[i].value:
                    continue
                
                day = self._dia(i, j, day)
    
    # Adicionar qual a turma que o programa vai pegar no arquivo
    def _esc(self, turma):
        if turma == 'A':
            self.cur = self.arq['A']

        elif turma == 'B':
            self.cur = self.arq['B']

        else:
            raise ValueError("SEM turma")

    # Adicionar o dia de hoje por extenso e pegar o horário do dia
    def Dia_Horario(self, dia_especifico=None, turma=None) -> str: 
        self._esc(turma)
        self._Materias_Horario()

        # Se for sábado | domingo, ele seleciona o dia verificado pelo usuário
        if dia_especifico:
            day = self._Dia_Específico(dia_especifico)

            if not isinstance(day, int):
                raise ValueError('O valor deve ser INT!')
            
        else:
            flag = self.week_day.isoweekday() + 1

            # Verifica se é domingo ou não
            if flag > 7:
                day = 1
            else:
                day = flag

        # confere o dia que foi selecionado seja pelo usuário ou pelo própio sistema
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
                #self.extenso += 'sábado'
                self.extenso += ''
                self.today = None

            case 7:
                #self.extenso += 'domingo'
                self.extenso += ""
                self.today = None

            case _:
                self.extenso = None
        return self.today
        