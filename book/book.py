from book.horario.ler import Horario
from book.arquivo.read import Read

class OrgLiv:
    def __init__(self):
        self.livros = {}
        self.cn_flag = ['fisica',
                   'quimica',
                   'biologia'
                   ]
        
        self.ch_flag = ['sociologia',
                   'geografia',
                   'filosofia',
                   'historia'
                   ]
        
        self.m_flag = ['matematica']

        self.l_flag = ['portugues',
                  'educacao fisica',
                  'ingles',
                  'literatura'
                  ]
        
        self.cn = set()
        self.ch = set()
        self.m = set()
        self.l = set()
        
        self.dia = Horario()
        self.memory = Read('./book/arquivo/livros.txt')
    
    def horario_day(self):
        self.dia.today_day
        
        print(self.dia.extenso)

    # Limpa de fato os itens
    def limp(self, it:dict):
        for lista in it.items():
            if lista[1] == ['']:
                continue
            self.verification_ordering(lista)

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
    def apd(self, livros):
        if livros:
            self.livros = self.limp(livros)
        
    def display(self):
        
        print(self.cn,
              self.ch,
              self.m,
              self.l)
        context = {'cn': self.cn, 'ch': self.ch, 'm': self.m, 'l': self.l}
        return context

    def memory_books(self):
        listinha = self.memory.reading()
        for i in listinha.items():
            print(i)
            self.verification_ordering(i)

    
sla = OrgLiv()

sla.memory_books()
