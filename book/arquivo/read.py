class Read:
    def __init__(self, arq):
        self.arq = arq

    def validation(self):
        gerator = self.reading()
        
        

    def reading(self):
        with open(self.arq) as arq:
            for linha in arq:
                valores = linha.rstrip().split('|')
                sla = list(linha.rstrip().split())
                print(sla)
    
leitor = Read('livros.txt')

print(leitor.reading())