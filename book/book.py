from book.horario.ler import Horario
from book.database.write import Write
from book.database.read import Read

class OrgLiv:
    def __init__(self):
        self.livros = {}
        self.cn_flag = [
                   'fisica',
                   'quimica',
                   'biologia'
                   ]
        
        self.ch_flag = [
                   'sociologia',
                   'geografia',
                   'filosofia',
                   'historia'
                   ]
        
        self.m_flag = ['matematica']

        self.l_flag = [
                  'portugues',
                  'ed',
                  'ingles',
                  'literatura'
                  ]
        
        self.cn = set()
        self.ch = set()
        self.m = set()
        self.l = set()
        
        self.dia = Horario()
        self.writedb = Write()
        self.readdb = Read()

    def horario_day(self):
        if not self.dia.today_day():
            self.dia.extenso = False
        
        return self.dia.extenso    


    def verification_ordering(self, name:tuple):
        if name[0] in self.cn_flag:
            for i in name[1]:
                self.cn.add(tuple(i)) if not i == [''] else 0

        elif name[0] in self.ch_flag:
            for i in name[1]:
                self.ch.add(tuple(i)) if not i == [''] else 0

        elif name[0] in self.m_flag:
            for i in name[1]:
                self.m.add(tuple(i)) if not i == [''] else 0

        elif name[0] in self.l_flag:
            for i in name[1]:
                self.l.add(tuple(i)) if not i == [''] else 0

    # Limpar todos os livros
    def apd(self, livros:dict):
        for lista in livros.items():
            if lista[1] == ['']:
                continue
            self.verification_ordering(lista)
        

    def display(self):
        
        if self.cn or self.ch or self.l or self.m:
            context = {'cn': self.cn, 'ch': self.ch, 'm': self.m, 'l': self.l}
            return context
        
        return None


    def up_books_db(self, items, turma):
        self.livros = items

        if turma == "A":
            self.writedb.writing_A(self.livros)
            return True
        self.writedb.writing_B(self.livros)


    def down_books_db(self, turma):
        try:
            self.livros = Read().reading(turma)
            flag = {}

            for i in self.livros.items():
                flag[i[0]] = eval(i[1])
            self.livros = flag

            return self.livros
        
        except AttributeError:
            self.livros = {
            'fisica': [[''], ['']],
            'quimica': [[''], ['']],
            'biologia': [[''], ['']],
            'sociologia': [[''], ['']],

            'geografia': [[''], ['']],
            'filosofia': [[''], ['']],
            'historia': [[''], ['']],

            'matematica': [[''], ['']],
            
            'portugues': [[''], ['']],
            'ed': [[''], ['']],
            'ingles': [[''], ['']],
            'artes': [[''], ['']],
            'literatura': [[''], ['']]
        }
    
    

        