from app import db, app
from app.models import Livros_A
from app.models import Livros_B

class Write:
    def __init__(self):
        self.items = {}
    
    def writing_A(self, items:dict):
        self.items = items
        final = {i[0]: str(i[1]) for i in self.items.items()}

        
        with app.app_context():

            livrosdb = Livros_A.query.get(1)

            livrosdb.fisica = final['fisica']
            livrosdb.quimica = final['quimica']
            livrosdb.biologia = final['biologia']

            livrosdb.sociologia = final['sociologia']
            livrosdb.geografia = final['geografia']
            livrosdb.filosofia = final['filosofia']
            livrosdb.historia = final['historia']

            livrosdb.matematica = final['matematica']

            livrosdb.portugues = final['portugues']
            livrosdb.ed = final['ed']
            livrosdb.ingles = final['ingles']
            livrosdb.literatura = final['literatura']
            livrosdb.artes = final['artes']

            db.session.commit()
    
    def writing_B(self, items:dict):
        self.items = items
        final = {i[0]: str(i[1]) for i in self.items.items()}

        with app.app_context():

            livrosdb = Livros_B.query.get(1)

            livrosdb.fisica = final['fisica']
            livrosdb.quimica = final['quimica']
            livrosdb.biologia = final['biologia']

            livrosdb.sociologia = final['sociologia']
            livrosdb.geografia = final['geografia']
            livrosdb.filosofia = final['filosofia']
            livrosdb.historia = final['historia']

            livrosdb.matematica = final['matematica']

            livrosdb.portugues = final['portugues']
            livrosdb.ed = final['ed']
            livrosdb.ingles = final['ingles']
            livrosdb.literatura = final['literatura']
            livrosdb.artes = final['artes']
            
            db.session.commit()
    