from book.horario.ler import Horario
from book.arquivo.read import Read

class OrgLiv:
    def __init__(self):
        self.livros = {}
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
    @staticmethod
    def limp(it:list):
        it_ret = it
        flag = set()

<<<<<<< HEAD
        for lista in it.items():
            if lista[1] == ['']:
                continue

            self.verification_ordenation(lista)
=======
        for lista in it:
            for inner in lista:
                flag.add(tuple(inner))
        
        it_ret = list(flag)
        return it_ret
>>>>>>> parent of db17f0d (Funcionou mais ou menos)

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
        
    def all_books_apd(self, items):
                
        self.cn = [
            items['fisica'],
            items['quimica'],
            items['biologia']
        ]

        self.ch = [
            items['sociologia'],
            items['geografia'],
            items['filosofia'],
            items['historia']
        ]       

        self.m = [
            items['matematica']
        ]

        self.l = [
            items['portugues'],
            items['ed'],
            items['ingles'],
            items['literatura']
        ]

    def display(self):
<<<<<<< HEAD
        
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
=======
        print(self.livros)
        return self.livros
>>>>>>> parent of db17f0d (Funcionou mais ou menos)
