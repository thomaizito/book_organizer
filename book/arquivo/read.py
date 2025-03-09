class Read:
    def __init__(self, arq):
        self.arq = arq

    def validation(self):
        gerator = self.reading()
        
        

    def reading(self):
        with open(self.arq) as arq:
            for linha in arq:
                item1, item2 = None, None
                linha = linha.rstrip().split(':')
                lista = linha[1].split(';')
                if not len(lista) <= 1:
                    item2 = tuple(lista[1].split(','))
                
                item1 = tuple(lista[0].split(','))

                listinha[linha[0]] = [item1, item2] if item2 else [item1]
            
            print(listinha)
                
                


            
            
            
    
leitor = Read('./book/arquivo/livros.txt')

leitor.reading()