from book.horario.ler import Horario

class OrgLiv:
    def __init__(self):
        self.cn = []
        self.ch = []
        self.m = []
        self.l = []
        self.it = []
        self.dia = Horario()
    
    def items(
            self,
            items:dict
        ):
        
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

    def horario_day(self):
        self.dia.today_day
        
        print(self.dia.extenso)

    # Limpa de fato os itens
    @staticmethod
    def limp(it:list):
        it_ret = it
        flag = set()

        for lista in it_ret:
            if len(lista[1]) <= 1:
                lista[1] = [
                    lista[1][0], lista[1][0]
                ]

            if not lista[1][0] or not lista[1][1]:
                lista[1] = [lista[1][0], lista[1][1]]
                continue
            
            if lista[0] == '':
                print(lista[0])
                lista[0] = [
                    lista[0][0], lista[0][1]
                ]

            if lista[1] != '':
                lista[1] = [
                    lista[1][0], lista[1][1]
                ]

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
    def apd(self, cn=None, ch=None, m=None, l=None):
        for _ in range(2):
            if cn:
                self.cn = self.limp(cn)

            if ch:
                self.ch = self.limp(ch)

            if m:
                self.m = self.limp(m)

            if l:    
                self.l = self.limp(l)
        
    
    def display(self):
        dcn = self.apresent(self.cn)
        dch = self.apresent(self.ch)
        dm = self.apresent(self.m)
        dl = self.apresent(self.l)
        contexto = {
            'ch': dch,
            'cn': dcn,
            'm': dm,
            'l': dl
            }
        
        return contexto
