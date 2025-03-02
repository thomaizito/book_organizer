from book.horario.ler import Horario

class OrgLiv:
    def __init__(self):
        self.livros = []
        self.dia = Horario()
    

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
    def apd(self, livros):
        
        if livros:
            self.livros = self.limp(livros)
        


    def display(self):
        contexto = self.livros
        
        return contexto
