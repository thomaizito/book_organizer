from flask import request, render_template
from app import app
from book.book import OrgLiv

@app.route('/', methods=['GET', "POST"])
def homepage():
    livros = OrgLiv()
    context = None
    if request.method == "POST":

        fisica = [request.form['f1'].split(' '), request.form["f2"].split(' ')]
        quimica = [request.form['q1'].split(' '), request.form['q2'].split(' ')]
        biologia = [request.form['b1'].split(' '), request.form['b2'].split(' ')]

        sociologia = [request.form['s1'].split(' '), request.form["s2"].split(' ')]
        geografia = [request.form['g1'].split(' '), request.form['g2'].split(' ')]
        filosofia = [request.form['fi1'].split(' '), request.form['fi2'].split(' ')]
        historia = [request.form['h1'].split(' '), request.form['h2'].split(' ')]

        matematica = [request.form['m1'].split(' '), request.form['m2'].split(' ')]

        portugues = [request.form['p1'].split(' '), request.form['p2'].split(' ')]
        ed = [request.form['ed1'].split(' '), request.form['ed2'].split(' ')]
        ingles = [request.form['i1'].split(' '), request.form['i2'].split(' ')]
        literatura = [request.form['li1'].split(' '), request.form['li2'].split(' ')]
        
        items:dict = {
            'fisica': fisica,
            'quimica': quimica,
            'biologia': biologia,
            'sociologia': sociologia,

            'geografia': geografia,
            'filosofia': filosofia,
            'historia': historia,

            'matematica': matematica,
            
            'portugues': portugues,
            'ed': ed,
            'ingles': ingles,
            'literatura': literatura
        }
        

         

        livros.items(items)

        livros.apd()

        print(livros.horario_day)

        context = livros.display()


    return render_template('index.html', context=context)
