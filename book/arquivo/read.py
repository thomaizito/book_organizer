class Read:
    def __init__(self, arq):
        self.arq = arq
        self.items:dict = {
            'fisica': [],
            'quimica': [],
            'biologia': [],
            'sociologia': [],

            'geografia': [],
            'filosofia': [],
            'historia': [],

            'matematica': [],
            
            'lingua portuguesa': [],
            'educacao fisica': [],
            'ingles': [],
            'literatura': []
        }
        

    def reading(self):
        with open(self.arq) as arq:
            listinha = {}
            for linha in arq:
                item1, item2 = None, None
                linha = linha.rstrip().split(':')
                lista = linha[1].split(';')
                if not len(lista) <= 1:
                    item2 = tuple(lista[1].split(','))
                
                item1 = tuple(lista[0].split(','))

                listinha[linha[0]] = [item1, item2] if item2 else [item1]
            
            return listinha
