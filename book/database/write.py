from app import db, app
from app.models import Livros_A
from app.models import Livros_B

class Write:
    def __init__(self):
        self.items = {}
    
    def writing_A(self, items:dict):
        self.items = items
        final = {i[0]: str(i[1]) for i in self.items.items()}

        try:
            with app.app_context():

                livrosdb = Livros_A.query.get(1)

                if not livrosdb:
                    add = Livros_A(
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

                    db.session.add(add)
                    db.session.commit()
                    return True

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
                return True
        except Exception as e:
            print(e)
    
    def writing_B(self, items:dict):
        self.items = items
        final = {i[0]: str(i[1]) for i in self.items.items()}
        try:
            with app.app_context():

                livrosdb = Livros_B.query.get(1)

                if not livrosdb:
                    add = Livros_B(
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

                    db.session.add(add)
                    db.session.commit()
                    return True

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
                return True
        except Exception as e:
            print(e)
        