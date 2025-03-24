from app import app, db
from app.models import Livros_A, Livros_B

class Read:
    def __init__(self):
        self.items = {}
    
    # Função para pegar todos os itens do banco de dados do flask
    def reading(self, turma):
        with app.app_context():
            if turma == "A":
                livros = Livros_A.query.get(1)
            else:
                livros = Livros_B.query.get(1)

            self.items:dict = {
                'fisica': livros.fisica,
                'quimica': livros.quimica,
                'biologia': livros.biologia,

                'sociologia': livros.sociologia,
                'geografia': livros.geografia,
                'filosofia': livros.filosofia,
                'historia': livros.historia,

                'matematica': livros.matematica,

                'portugues': livros.portugues,
                'ed': livros.ed,
                'ingles': livros.ingles,
                'literatura': livros.literatura,
                'artes': livros.artes
            }
            
            return self.items