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
        it_ret = it

        for lista in it_ret:
            if len(lista[1]) <= 1:
                lista[1] = [
                    lista[1][0], lista[1][0]
                ]

            if not lista[1][0] or not lista[1][1]:
                lista[1] = [lista[1][0], lista[1][1]]
                continue

            lista[0] = [
                lista[0][0], lista[0][1]
            ]

            lista[1] = [
                lista[1][0], lista[1][1]
            ]

        flag = set()

        for _ in it:
            for i in _:
                flag.add(tuple(i))
        
        it_ret = list(flag)
        return it_ret

    @staticmethod
    def apresent(values:list):
        ap_modulos = [ values[num][0]
                      for num in range(len(values)) 
                     ]

        ap_nums = [ values[num][1]
                    for num in range(len(values))
                  ]

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
        contexto = {
            'cn': self.cn,
            "ch": [ self.ch[0],
                    self.ch[1],
                    self.ch[2] ],
            "m": self.m,
            "l": self.l
            }
        
        return contexto
