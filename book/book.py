from book.horario.ler import Horario
from book.arquivo.read import Read

class OrgLiv:
    def __init__(self):
        self.livros = {}
        self.cn_flag = ['fisica',
                   'quimica',
                   'biologia']
        
        self.ch_flag = ['sociologia',
                   'geografia',
                   'filosofia',
                   'historia']
        
        self.m_flag = ['matematica']

        self.l_flag = ['portugues',
                  'educacao fisica',
                  'ingles',
                  'literatura']
        
        self.cn = []
        self.ch = []
        self.m = []
        self.l = []
        
        self.dia = Horario()
        self.memory = Read('./book/arquivo/livros.txt')
    
    def horario_day(self):
        self.dia.today_day
        
        print(self.dia.extenso)



    # Limpa de fato os itens
    def limp(self, it:dict):
        it_ret = it
        flag = set()
        print(it_ret)

        for lista in it.items():
            if lista[1] == ['']:
                continue

            self.verification_ordenation(lista)

    def verification_ordenation(self, name:tuple):
        if name[0] in self.cn_flag:
            if name[1] not in self.cn:
                self.cn.append(name[1])
            else:
                return

        elif name[0] in self.ch_flag:
            if name[1] not in self.ch:
                self.ch.append(name[1])
            else:
                return 

        elif name[0] in self.m_flag:
            if name[1] not in self.m:
                self.m.append(name[1])
            else:
                return

        elif name[0] in self.l_flag:
            if name[1] not in self.l:
                self.l.append(name[1])
            else:
                return 
        


    # Deixa de forma apresentável
    @staticmethod 
    def apresent(values:list):
        ap_modulos = [ values[num][0]
                      for num in range(len(values)) 
                      if values[num][0] != ''
                     ]

        ap_nums = [ values[num][1]
                    for num in range(len(values))
                    if values[num][0] != ''
                  ]

        demonst = list(zip(ap_modulos, ap_nums))
        return demonst

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
