from app import db, app
from app.models import Livros_A
from app.models import Livros_B

class Write:
    def __init__(self):
        self.items = {}
    
    def writing_A(self, items:dict):
        self.items = items
        final = {i[0]: str(i[1]) for i in items.values()}

        with app.app_context():

            final_livros = Livros_A(
                fisica = final['fisica'],
                quimica = final['quimica'],
                biologia = final['biologia'],

                sociologia = final['sociologia'],
                geografia = final['geografia'],
                filosofia = final['filosofia'],
                historia = final['historia'],

                matematica = final['matematica'],

                portugues = final['portugues'],
                ed = final['ed'],
                ingles = final['ingles'],
                literatura = final['literatura'],
                artes = final['artes']
            )

            db.session.add(final_livros)
            db.session.commit()
    
    def writing_B(self, items:dict):
        self.items = items
        final = {i[0]: str(i[1]) for i in items.values()}

        with app.app_context():

            final_livros = Livros_B(
                fisica = final['fisica'],
                quimica = final['quimica'],
                biologia = final['biologia'],

                sociologia = final['sociologia'],
                geografia = final['geografia'],
                filosofia = final['filosofia'],
                historia = final['historia'],

                matematica = final['matematica'],

                portugues = final['portugues'],
                ed = final['ed'],
                ingles = final['ingles'],
                literatura = final['literatura'],
                artes = final['artes']
            )

            db.session.add(final_livros)
            db.session.commit()
    