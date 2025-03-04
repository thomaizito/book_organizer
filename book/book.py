from book.horario.ler import Horario

class OrgLiv:
    def __init__(self):
        self.livros = {}
        self.cn = []
        self.ch = []
        self.m = []
        self.l = []
        self.dia = Horario()
    

    def horario_day(self):
        self.dia.today_day
        
        print(self.dia.extenso)

    # Limpa de fato os itens
    @staticmethod
    def limp(it:list):
        it_ret = it
        flag = set()

        for lista in it:
            for inner in lista:
                flag.add(tuple(inner))
        
        it_ret = list(flag)
        return it_ret

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
        print(self.livros)
        return self.livros
