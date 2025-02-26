
class OrgLiv:
    def __init__(self):
        self.cn = []
        self.ch = []
        self.m = []
        self.l = []
        self.it = []
    
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
