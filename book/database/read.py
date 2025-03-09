from app import app, db
from app.models import Livros_A, Livros_B

class Read:
    def __init__(self):
        self.items = {}
    
    def reading(self, turma):

        with app.app_context():
            if turma == "A":
                livros = Livros_A.query.get(1)
            else:
                livros = Livros_B.query.get(1)

            self.items = {
                'fisica': livros.fisica,
                'quimica': livros.quimica,
                'biologia': livros.biologia,

                'sociologia': livros.sociologia,
                'geografia': livros.geografia,
                'filosofia': livros.filosofia,
                'historia': livros.historia,

                'matematica': livros.matematica,

                'lingua portugues': livros.portugues,
                'educacao fisica': livros.ed,
                'ingles': livros.ingles,
                'literatura': livros.literatura,
                'artes': livros.artes
            }
            
            return self.items