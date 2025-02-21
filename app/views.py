from flask import request, render_template
from app import app
from book import OrgLiv

@app.route('/', methods=['GET', "POST"])
def homepage():
    livros = OrgLiv()
    context = None
    if request.method == "POST":

        print(request.form['f1'].split(' '))

        fisica = [request.form['f1'].split(' '), request.form["f2"].split(' ')]
        quimica = [request.form['q1'].split(' '), request.form['q2'].split(' ')]
        biologia = [request.form['b1'].split(' '), request.form['b2'].split(' ')]

        ch = [
            fisica,
            quimica,
            biologia
        ]

        

        livros.apd(ch)
        context = livros.display()


    return render_template('index.html', context=context)
