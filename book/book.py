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

    # Verifica os itens que foram passados do frontend e adiciona eles em seus respectivos lugares
    def verification_ordering(self, livros:dict):
        for lista in livros.items():
            if lista[0] in self.cn_flag:
                for i in lista[1]:
                    self.cn.add(tuple(i)) if not i == [''] else 0

            elif lista[0] in self.ch_flag:
                for i in lista[1]:
                    self.ch.add(tuple(i)) if not i == [''] else 0

            elif lista[0] in self.m_flag:
                for i in lista[1]:
                    self.m.add(tuple(i)) if not i == [''] else 0

            elif lista[0] in self.l_flag:
                for i in lista[1]:
                    self.l.add(tuple(i)) if not i == [''] else 0

        
    # Retorna o context para ser adicionado no frontend
    def display(self):
        
        if self.cn or self.ch or self.l or self.m:
            context = {'cn': self.cn, 'ch': self.ch, 'm': self.m, 'l': self.l}
            return context

    # Upa os itens no banco de dados
    def up_books_db(self, items, turma):
        self.livros = items
        self.writedb.writing(self.livros, turma)

    # Pega os itens do banco de dados
    def down_books_db(self, turma):
        try:
            self.livros = Read().reading(turma)
            flag = {}

            for i in self.livros.items():
                flag[i[0]] = eval(i[1])
            self.livros = flag

            return self.livros
        
        except AttributeError or Exception:
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
    