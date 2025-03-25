from app import db, app
from app.models import Livros_A
from app.models import Livros_B

class Write:
    def __init__(self):
        self.items = {}
    
    # Função para modificar os livros no banco de dados
    def writing(self, items:dict, turma=None):
        self.items = items
        final = {i[0]: str(i[1]) for i in self.items.items()}
        
        if turma == 'A':
            Model = Livros_A
        elif turma == "B":
            Model = Livros_B
        else:
            raise ValueError("O valor não foi atendido corretamente, A ou B")

        with app.app_context():

            livrosdb = Model.query.get(1)

            print(livrosdb)

            if not livrosdb:
                add = Model(
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
                return

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
    