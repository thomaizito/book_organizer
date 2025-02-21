livros = {
    'cnatureza':
    {
    'FGB': None, 
    "FIC": None
    },

    'chumanas': 
    {
    "FGB": None,
    "FIC": None
    },

    'matematica':
    {
    "FGB": None,
    "FIC": None,
    },

    "linguagens":
    {
    'FGB': None,
    "FIC": None
    }

}

class OrgLiv:
    def __init__(self):
        self.cn = []
        self.ch = []
        self.m = []
        self.l = []
        self.it = []
    

    @staticmethod
    def limp(it:list):
        
        print(it)

        if not it:
            return False
        
        if len(it[1]) <= 1:
            it_ret = [
                [it[0][0], int( it[0][1])],
                ['', '']
            ]
            return it_ret

        it_ret = [
            [it[0][0], int( it[0][1] )],
            [it[1][0], int( it[1][1] )]
        ]

        return it_ret

    @staticmethod
    def apresent(values:list):
        ap_modulos = [values[num][0] for num in range(len(values))]
        ap_nums = [values[num][1] for num in range(len(values))]
        demonst = list(zip(ap_modulos, ap_nums))
        print(demonst)


    def apd(self, cn=None, ch=None, m=None, l=None, it=None):
        if cn:
            self.cn = self.limp(cn)

        if ch:
            self.ch = self.limp(ch)

        if m:
            self.m = self.limp(m)

        if l:    
            self.l = self.limp(l)
        
    
    def display(self):
        self.apresent(self.cn)
        contexto = {'cn': self.cn, "ch": self.ch, "m": self.m, "l": self.l}
        
        return contexto
