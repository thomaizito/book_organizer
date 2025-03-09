from app import db

class Livros_A(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fisica = db.Column(db.String, nullable=True)
    quimica = db.Column(db.String, nullable=True)
    biologia = db.Column(db.String, nullable=True)

    sociologia = db.Column(db.String, nullable=True)
    geografia = db.Column(db.String, nullable=True)
    filosofia = db.Column(db.String, nullable=True)
    historia = db.Column(db.String, nullable=True)

    matematica = db.Column(db.String, nullable=True)

    portugues = db.Column(db.String, nullable=True)
    ed = db.Column(db.String, nullable=True)
    ingles = db.Column(db.String, nullable=True)
    literatura = db.Column(db.String, nullable=True)
    artes = db.Column(db.String, nullable=True)

class Livros_B(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fisica = db.Column(db.String, nullable=True)
    quimica = db.Column(db.String, nullable=True)
    biologia = db.Column(db.String, nullable=True)

    sociologia = db.Column(db.String, nullable=True)
    geografia = db.Column(db.String, nullable=True)
    filosofia = db.Column(db.String, nullable=True)
    historia = db.Column(db.String, nullable=True)

    matematica = db.Column(db.String, nullable=True)

    portugues = db.Column(db.String, nullable=True)
    ed = db.Column(db.String, nullable=True)
    ingles = db.Column(db.String, nullable=True)
    literatura = db.Column(db.String, nullable=True)
    artes = db.Column(db.String, nullable=True)